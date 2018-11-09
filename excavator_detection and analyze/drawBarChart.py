import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import cv2

def drawBarChartNumOfWorkers(count): 
	objects = ('Form Workers', 'Rebar Workers', 'Concerete Workers')
	y_pos = np.arange(len(objects))
	
	plt.figure(figsize=(15,5))
	plt.xticks(np.arange(0, 10, 1))
	plt.barh(y_pos, count, align='center', alpha=0.5)
	plt.yticks(y_pos, objects)
	plt.xlabel('Count')
	plt.title('Number of Workers')
	plt.savefig('books_read.png')
	#plt.show()
	
	image = cv2.imread('books_read.png')
	cv2.imshow("title",image)
	cv2.waitKey(1000)
	return image

count = [0,1,2]
drawBarChartNumOfWorkers(count)
