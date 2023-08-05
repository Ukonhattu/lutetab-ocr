# import the necessary packages
from PIL import Image
import argparse
import cv2 as cv
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

img = cv.imread(args["image"])

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window