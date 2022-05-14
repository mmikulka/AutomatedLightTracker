# Auotmated Light Tracker


## Introduction
This repository contains an GUI driven open CV based tracker to that allows the tracking of a subject on a stage with only a camera, capture card and computer. The Trackingn algorithm is based on [Mike-Bronstrom's implementation of the YOLOv5 and Deep Sort with OSNet repository](https://github.com/mikel-brostrom/Yolov5_DeepSort_OSNet). The application is still in the early stages of development, so not all functionality is implemented.

## Before you run the tracker

1. clone the repository:
`git clone https://github.com/mmikulka/AutomatedLightTracker.git`
2. make sure that all the requirements have been fulfilled:
      - python 3.8 or later and all dependencies within requirements.txt and pytorch
      `pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113`
      `pip install -r requirements.txt`

## Running the Applictaion

`python AutoLightTracker.py`

## Instructions

### Startup Window:
<div align="center">
<img src="Screen Captures/Startup.png" width="300"/>
</div>

This window gives you the choice to open an already saved file, open a new project, or Calibrate a camera

### Tracking Area Setup:
<div align="center">
<img src="Screen Captures/Space Setup.png" width="400"/>
</div>
In This window you set up the area that the tracking area will be the most accurate in. To do this
you must first take a reference picture with the camera in the exact position the camera will  be
in when using it to track actors. find 4 points that mark the boundary of the tracking area. By selecting the radio button
associated with the placement onstage of and then clicking the point in the reference image that
corresponds with the real world point the pixel placement information will be automatically added
to the correct text field. Once that is complete the height and width of the tracking area in Feet must
be entered into the height and width field.


### Fixture List:
<div align="center">
<img src="Screen Captures/fixture list.png" width="300"/>
</div>
The fixture list will list all the fixtures that are currently in the project. For testing purposes a SoloSpot
2000 fixture is listed in the fixture list when opening a new show. Adding a fixture, editing, and removing a
fixture is still be worked on.

### Main Window:

<div align="center">
<img src="Screen Captures/Main Window.png" width="300"/>
</div>

This is the main window of the application. The image in the middle of the window is the camera view
This shows all the subjects that are currently being tracked.
the upper right button will allow  you to recalibrate the tracking area via the tracking area window.
The button in the bottom left will allow you to assign what lights will be used to track. The bottom
left drop down menu. allows the user to select the subject they wish to track. The drop down menu in
upper left will allow the user to select the camera they wish to use. The menu bar at the top allows 
you to access the sACN prtocal window, Camera calibration Window, Fixture list, and file system information.
*Note: not all features are currently working*

### Camera Calibration
<div align="center">
<img src="Screen Captures/camera Calibration.png" width="300"/>
</div>

<lb>Calibration Instructions</lb>

<ol>
<li> Print out Provided Calibration Imagee</li>
<li> Put the camera on a tripod or similar</li>
<li> Place camera facing a blank wall with enough distance so the paper is approximately 1/8 the size of the image</li>
<li> Tape the paper to the wall, so it is located in the top right corner of the image.</li>
<li> Once a complete circle has been completed take 3 pictures with the chess board pattern in th
middle of the frame all at slightly different positions.</li>
<li> load images into the calibration folder.</li>
<li> Run calibration test on the folder</li>
</ol>

This will calibrate a camera to remove any distortions  found in the image resulting from the lens of the camera
