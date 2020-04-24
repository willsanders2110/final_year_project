# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="image to test CNN on")
ap.add_argument("-m", "--model", required=True, help="path to pre-trained CNN")
ap.add_argument("-s", "--save", required=True, help="save image as")
args = vars(ap.parse_args())

model = load_model(args["model"])

img = cv2.imread(args["image"])
frame_width = 300
frame_height = 200

# resize the frame, convert it to grayscale, and then clone the
# original frame so we can draw on it later in the program
img = imutils.resize(img, width=frame_width)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

roi = cv2.resize(img, (32, 32))
roi = roi.astype("float") / 255.0
roi = img_to_array(roi)
roi = np.expand_dims(roi, axis=0)

(class_1, class_2, class_3) = model.predict(roi)[0]

class_1 = round(class_1, 2)
class_2 = round(class_2, 2)
class_3 = round(class_3, 2)

print("{}\t{}\t{}".format(class_1, class_2, class_3))

# # print("Scores: {}, {}, {}, {}".format(basil, mint, rosemary, thyme))
# if (class_1 > class_2) and (class_1 > class_3) and (class_1 > 0.8):
#     label = "basil"
# elif (class_2 > class_1) and (class_2 > class_3) and (class_2 > 0.8):
#     label = "not basil"
# elif (class_3 > class_1) and (class_3 > class_2) and (class_3 > 0.8):
#     label = "unhealthy basil"
# else:
#     label = ""

if (class_1 > class_2) and (class_1 > class_3) and (class_1 > 0.6):
    label = "basil"
elif (class_2 > class_1) and (class_2 > class_3) and (class_2 > 0.6):
    label = "not basil"
elif (class_3 > class_1) and (class_3 > class_2) and (class_3 > 0.6):
    label = "unhealthy basil"
else:
    label = ""

# print(label)
# display the label and bounding box rectangle on the output
# frame
cv2.putText(img, label, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
# cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH), (0, 0, 255), 2)

cv2.imshow("Plant", img)
cv2.imwrite(args["save"], img)
cv2.waitKey(0)
cv2.destroyAllWindows()
