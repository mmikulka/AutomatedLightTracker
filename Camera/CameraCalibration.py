import numpy as np
import cv2
import glob


class Camera:
    def __init__(self, chessboardSize=(9, 6), frameSize=(4592, 3448)):
        self.chessboardSize = chessboardSize
        self.frameSize = frameSize
        self.termCriteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    def findCorners(self, imageDrectories, showImages=False):
        objp = np.zeros((self.chessboardSize[0] * self.chessboardSize[1], 3), np.float32)
        objp[:, :2] = np.mgrid[0:self.chessboardSize[0], 0:self.chessboardSize[1]].T.reshape(-1, 2)

        # Arrays to store object points and image points from all the images.
        objpoints = []  # 3d point in real world space
        imgpoints = []  # 2d points in image plane.

        images = glob.glob('*.jpg')

        for image in images:

            print(image)
            img = cv2.imread(image)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Find the chess board corners
            ret, corners = cv2.findChessboardCorners(gray, self.chessboardSize, None)
            print(ret)

            # If found, add object points, image points (after refining them)
            if ret:

                objpoints.append(objp)
                corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), self.termCriteria)
                imgpoints.append(corners)

                # Draw and display the corners
                if showImages:
                    cv2.drawChessboardCorners(img, self.chessboardSize, corners2, ret)
                    cv2.imshow('img', img)
                    cv2.waitKey(500)

        cv2.destroyAllWindows()
        return objpoints, imgpoints

    def CalibrateCameras(self, objPts, imgPts):

        self.ret, self.cameraMatrix, self.dist, self.rvecs, self.tvecs = cv2.calibrateCamera(objPts, imgPts,
                                                                                             self.frameSize, None, None)

    def undistortImage(self, img):
        # Grab image to undistort

        h, w = img.shape[:2]
        newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(self.cameraMatrix, self.dist, (w, h), 1, (w, h))

        # Undistort
        dst = cv2.undistort(img, self.cameraMatrix, self.dist, None, newCameraMatrix)

        # crop the image
        x, y, w, h = roi
        dst = dst[y:y + h, x:x + w]

        # Reprojection Error
        mean_error = 0

        for i in range(len(self.objPts)):
            imgpoints2, _ = cv2.projectPoints(self.objPts[i], self.rvecs[i], self.tvecs[i], self.cameraMatrix,
                                              self.dist)
            error = cv2.norm(self.imgPts[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
            mean_error += error

        print("total error: {}".format(mean_error / len(self.objPts)))

        return dst



