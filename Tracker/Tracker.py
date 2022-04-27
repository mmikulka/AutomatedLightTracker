import os

import sys

import argparse
import os
import platform
import shutil
import time
from pathlib import Path
import cv2
import torch
import torch.backends.cudnn as cudnn

#from yolov5.models.experimental import attempt_load
#from yolov5.utils.downloads import attempt_download
from Tracker.yolov5.models.common import DetectMultiBackend
from Tracker.yolov5.utils.datasets import LoadImages, LoadStreams, LoadWebcam
from Tracker.yolov5.utils.general import (LOGGER, check_img_size, non_max_suppression, scale_coords,
                                  check_imshow, xyxy2xywh, increment_path)
from Tracker.yolov5.utils.torch_utils import select_device, time_sync
from Tracker.yolov5.utils.plots import Annotator, colors
from Tracker.deep_sort.utils.parser import get_config
from Tracker.deep_sort.deep_sort import DeepSort

class Tracker:
    def __init__(self, yoloModel, deepSortModel, deepSortConfig, source, classes, device, imgsz, half) -> None:
        self.yoloModel = yoloModel
        self.deepSortModel = deepSortModel
        self.deepSortConfig = deepSortConfig
        self.source = source
        self.classes = classes
        self.device = device
        self.imgsz = imgsz
        self.half = half

    def setup(self):
        with torch.no_grad():
            #configure Deepsort
            cfg = get_config()
            cfg.merge_from_file(self.deepSortConfig)
            self.deepSort = DeepSort(self.deepSortModel, max_dist = cfg.DEEPSORT.MAX_DIST,
                                max_iou_distance = cfg.DEEPSORT.MAX_IOU_DISTANCE,
                                max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
                                use_cuda=True)

            #setup Device to do calculations on
            self.device = select_device(self.device)
            self.half &= self.device.type != 'cpu'

            #load YOLO Model
            self.model = DetectMultiBackend(self.yoloModel, device = self.device, dnn=True)
            stride, names, pt, jit, _ = self.model.stride, self.model.names, self.model.pt, self.model.jit, self.model.onnx
            self.imgsz = check_img_size(self.imgsz, s=stride) #check image`

            self.half = pt and self.device.type!= 'cpu'
            if pt:
                self.model.model.half() if self.half else self.model.model.float()

            self.webcam = self.source.isnumeric() or self.source.startswith('rtsp') or self.source.startwith('http') or self.source.endswith('.txt')

            if self.webcam:
                self.show_vid = check_imshow()
                cudnn.benchmark = True
                self.dataset = LoadWebcam(pipe=self.source, img_size=self.imgsz, stride=stride)
                bs = len(self.dataset)
            else:
                self.dataset = LoadImages(self.source, img_size=self.imgsz, stride=stride, auto=pt and not jit)
                bs = 1

            self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names

            return self.dataset



    def detect(self, frame_idx, path, img, im0s, vid_cap, s, dt, seen, save_dir):
        #self.model(torch.zeros(1, 3, *self.imgsz).to(self.device).type_as(next(self.model.model.parameters()))) # WarmUP
        t1 = time_sync()

        img = torch.from_numpy(img).to(self.device)
        img = img.half() if self.half else img.float()
        img /= 255.0 # 0-255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img[None]
        t2 = time_sync()
        dt[0] += t2 - t1

        #inference
        #visualize = increment_path(save_dir / Path(path).stem, mkdir = True) if True else False
        pred = self.model(img, augment=True)
        t3 = time_sync()
        dt[1] += t3 - t2

        pred = non_max_suppression(pred, 0.3, 0.5, self.classes, True, 1000)
        dt[2] += time_sync() - t3
        outputs = None
        
        for i, det in enumerate(pred):
            seen += 1
            if self.webcam:
                p, im0, _ = path[i], im0s.copy(), self.dataset.count
                s += f'{i}: '
            else:
                p, im0, _ = path, im0s.copy(), getattr(self.dataset, 'frame', 0)
            
            p = Path(p)
            #save_path = str(save_dir / p.name)
            s += '%gx%g ' % img.shape[2:] #print string

            annotator = Annotator(im0, line_width=2, pil=not ascii)

            if det is not None and len(det):
                #rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords( img.shape[2:], det[:, :4], im0.shape).round()
                #print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {self.names[int(c)]}{'s' * (n > 1)}, "  # add to string

                xywhs = xyxy2xywh(det[:, 0:4])
                confs = det[:, 4]
                clss = det[:, 5]

                #pass detections to deepsort
                t4 = time_sync()
                outputs = self.deepSort.update(xywhs.cpu(), confs.cpu(), clss.cpu(), im0)
                t5 = time_sync()
                dt[3] += t5 - t4

                #drawboxes for visualization
                if len(outputs) > 0:
                    for j, (output, conf) in enumerate(zip(outputs, confs)):
                        
                        bboxes = output[0:4]
                        id = output[4]
                        cls = output[5]

                        c = int(cls)
                        label = f'{id} {self.names[c]} {conf:.2f}'
                        annotator.box_label(bboxes, label, color=colors(c, True))

                LOGGER.info(f'{s}Done. YOLO:({t3 - t2:.3f}s), DeepSort:({t5 - t4:.3f}s)')
            
            else:
                self.deepSort.increment_ages()
                LOGGER.info("No detections")

            im0 = annotator.result()
            if self.show_vid:
                return im0, outputs

            






