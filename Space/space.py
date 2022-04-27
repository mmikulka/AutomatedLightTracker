import cv2
import numpy as np
import logging


class Space:
    def __init__(self):
        self.birdMatrix = None
        self.widthInchPerPixel = None
        self.heightInchPerPixel = None
        self.transformWidth = 0
        self.transformHeight = 0
        self._setup = False

    def calcBirdsEye(self, image, cornerPts, stageLength, stageWidth):

        self.length = stageLength
        self.width = stageWidth

        print(cornerPts)

        cornerPtsArray = self.__order_points(cornerPts)

        (tl, tr, br, bl) = cornerPtsArray

        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        maxWidth = max(int(widthA), int(widthB))

        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        maxHeight = max(int(heightA), int(heightB))

        img_params = np.array([
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1]], dtype="float32")

        self.birdMatrix = cv2.getPerspectiveTransform(cornerPtsArray, img_params)
        resizeImg = cv2.resize(image, (1280, 720))
        img_transformed = cv2.warpPerspective(resizeImg, self.birdMatrix, (maxWidth, maxHeight))
        self.transformHeight = maxHeight
        self.transformWidth = maxWidth

        self.heightInchPerPixel = stageLength / maxHeight
        self.widthInchPerPixel = stageWidth / maxWidth



        self._setup = True

        cv2.imwrite(
            "C:\\Users\\mattm\\OneDrive - CSULB\\School\\Final Project\\OpenCV test\\Camera calibration test\\resized.png",
            resizeImg)
        cv2.imwrite("C:\\Users\\mattm\\OneDrive - CSULB\\School\\Final Project\\OpenCV test\\Camera calibration test\\thrustWarp.png", img_transformed)

        logging.info("transform matrix successfully created")

        return img_transformed

    def getxyCoordinates(self, pts):
        if self._setup:
            list_points_to_detect = np.float32(pts).reshape(-1, 1, 2)
            print(list_points_to_detect)
            transformed_points = cv2.perspectiveTransform(list_points_to_detect, self.birdMatrix)
            # Loop over the points and add them to the list that will be returned
            transformed_points_list = list()
            for i in range(0, transformed_points.shape[0]):
                transformed_points_list.append([transformed_points[i][0][0], transformed_points[i][0][1]])

            print("transformed pts: " + str(transformed_points_list))

            xyCoord = list()
            for pt in transformed_points_list:
                xyCoord.append((pt[0] * self.widthInchPerPixel))
                xyCoord.append(pt[1] * self.heightInchPerPixel)

            logging.info('xy coordinates: ' + str(xyCoord))
            print('xy coordinates: ' + str(xyCoord))

            return xyCoord
        logging.error(
            "transformations not set up correctly, Must calculate birds eye view before you can get xy coordinates")
        print("ERROR: Must calculate birds eye view before utilizing getxyCoordinates")

    def __order_points(self, pts):
        rect = np.zeros((4, 2), dtype='float32')

        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]

        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]

        return rect

    @property
    def setup(self):
        return self._setup

    @setup.setter
    def setup(self, value):
        self._setup = value


if "__main__" == __name__:
    image = cv2.imread(
        "C:\\Users\\mattm\\OneDrive - CSULB\\School\\Final Project\\OpenCV test\\Camera calibration test\\studio3.png")
    pts = np.array([(416, 55), (193, 626), (1151, 621), (966, 35)])

    space = Space()

    warped = space.calcBirdsEye(image, pts, 20, 26)

    space.getxyCoordinates((574, 184))

    cv2.imshow("original", cv2.resize(image, (1280, 720)))
    cv2.imshow('warped', warped)
    cv2.imwrite(
        "C:\\Users\\mattm\\OneDrive - CSULB\\School\\Final Project\\OpenCV test\\Camera calibration test\\thrustWarp.png",
        warped)
    cv2.waitKey(0)
