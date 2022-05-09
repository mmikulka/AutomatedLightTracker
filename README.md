# Auotmated Light Tracker


## Introduction
This repository conntains an GUI driven open CV based tracker to that allows the tracking of a subject on a stage with only a camera, capture card and computer. The Trackingn algorithm is based on [Mike-Bronstrom's implementation of the YOLOv5 and Deep Sort with OSNet repository](https://github.com/mikel-brostrom/Yolov5_DeepSort_OSNet). The application is still in the early stages of development, so not all functionality is implemented.

## Before you run the tracker

1. clone the repository:
'git clone https://github.com/mmikulka/AutomatedLightTracker.git'
2. make sure that all the requirements have been fulfilled:
      - python 3.8 or later and all dependencies within requirements.txt
      'pip install -r requirements.txt'

## Running the Applictaion

'python main.py' if python 3 is the only version installed on the device 
if not: 'python3 main.py'
