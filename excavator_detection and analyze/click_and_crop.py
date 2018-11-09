# USAGE
# python click_and_crop.py --image ML_frames_noInfo/ml_frame_22.png

# import the necessary packages
import argparse
import cv2

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping,s

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		x1,y1=refPt[0]
		x2,y2=refPt[1]
		#print(x1,y1,x2,y2)
		#s={"x2": 235, "y1": 296, "x1": 197, "object": "PERSON", "y2": 346}
		s=","+"{\"x2\": "+str(x2)+ ", \"y1\": "+str(y1) +", \"x1\": "+str(x1)+", \"object\": \"PERSON\", \"y2\": "+str(y2)+"}"
		index1=fileName.rfind("_")+1
		index2=fileName.find(".")
		jsonFile="/home/indusai/code/indus.ai-applyingDetector/Jsonfiles/frame"+fileName[index1:index2]+".txt"
		print(s)
		print(jsonFile)
		with open(jsonFile, 'r') as myfile:
    			data=myfile.read().replace('\n', '')
			print(data)
		index = data.rfind(']')
 		output_line = data[:index] + s + data[index:]
		print("***********************")
		print(output_line)
		f = open(jsonFile, 'r+')
		f.truncate(0)
		f.write(output_line)
		f.close()
	
		cv2.imshow("image", image)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
fileName=args["image"]
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# keep looping until the 'q' key is pressed
s=""
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF

	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()

	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break

# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(refPt) == 2:
	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imshow("ROI", roi)
	cv2.waitKey(0)

# close all open windows
cv2.destroyAllWindows()
