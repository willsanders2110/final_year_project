# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True, help="path to pre-trained smile detector CNN")
args = vars(ap.parse_args())

model = load_model(args["model"])

camera = cv2.VideoCapture(1)
frame_width = 300
frame_height = 200

# Define the codec and create VideoWriter object.The output is stored in 'output.avi' file.
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'P', 'E', 'G'), 10, (frame_width, frame_height))

# keep looping
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()

	# if we are viewing a video and we did not grab a frame, then we
	# have reached the end of the video
	if args.get("video") and not grabbed:
		break

	# resize the frame, convert it to grayscale, and then clone the
	# original frame so we can draw on it later in the program
	frame = imutils.resize(frame, width=frame_width)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	roi = cv2.resize(frame, (32, 32))
	roi = roi.astype("float") / 255.0
	roi = img_to_array(roi)
	roi = np.expand_dims(roi, axis=0)

	(basil, mint, rosemary, thyme) = model.predict(roi)[0]

	basil = round(basil, 2)
	mint = round(mint, 2)
	rosemary = round(rosemary, 2)
	thyme = round(thyme, 2)

	print("{}\t{}\t{}\t{}".format(basil, mint, rosemary, thyme))

	# print("Scores: {}, {}, {}, {}".format(basil, mint, rosemary, thyme))
	if (basil > mint) and (basil > rosemary) and (basil > thyme) and (basil > 0.8):
		label = "basil"
	elif mint > basil and mint > rosemary and mint > thyme and mint > 0.8:
		label = "mint"
	elif rosemary > basil and rosemary > mint and rosemary > thyme and rosemary > 0.8:
		label = "rosemary"
	elif thyme > basil and thyme > mint and thyme > rosemary and thyme > 0.8:
		label = "thyme"
	else:
		label = ""

	# print(label)
	# display the label and bounding box rectangle on the output
	# frame
	cv2.putText(frame, label, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
	# cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH), (0, 0, 255), 2)

	cv2.imshow("Plant", frame)

	# if the 'q' key is pressed, stop the loop
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# cleanup the camera and close any open windows
camera.release()
out.release()
cv2.destroyAllWindows()
