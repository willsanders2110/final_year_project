# University of Sheffield
# Project: Individual Project
# Author: Will Sanders
# Date: 22/10/19
# Version: 1.0
# Description: Script that takes a video and saves the individual frames as separate images.
#              Useful when making a data set of images for deep learning techniques.

import cv2
import argparse

# Argument parsing setup
# Initialises both the file to be split, and the name, and path of the
# images that will be saved
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="path to the video file")
ap.add_argument("-n", "--name", required=True, help="name to save images as")
args = vars(ap.parse_args())

# Grabs the specified video
video = cv2.VideoCapture(args["video"])

# Sets the image save location and file name
save_location = args["name"]

# Set a counter to 0 for the start of the video
counter = 3261

# Loops over all the frames in the video
while True:
    # Grabs the current frame
    (grabbed, frame) = video.read()

    # Breaks while loop if no new frame is grabbed
    if args.get("video") and not grabbed:
        break

    # Increase the counter by one to save the frame as a new image
    counter += 1

    # Saves the frame as a new image in the specified location
    cv2.imwrite("{}_{}.jpg".format(save_location, counter), frame)

# Displays to the screen the total number of frames saves
print("{} frames saves".format(counter))
