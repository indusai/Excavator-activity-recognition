import os
import cv2
import json
from  TFOD_config import *
import shutil 
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
font = cv2.FONT_HERSHEY_TRIPLEX
import matplotlib.patches as mpatches
from numpy  import array
import matplotlib.font_manager as font_manager

def drawBarChartTotalNumOfWorkers(count): 
	objects = ('Form Workers', 'Rebar Workers', 'Concerete Workers')
	y_pos = np.arange(len(objects))
	#performance = [10,8,6]
	#plt.figure(figsize=(15,5)) 
	plt.bar(y_pos, count, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	plt.ylabel('Total Count')
	plt.title('Total Number of Workers')
	plt.grid(True)
	#plt.yticks(np.arange(0, max(count), 10))

	plt.savefig('books_read2.png')
	
	
	image = cv2.imread('books_read2.png')
	#plt.show()
	#cv2.imshow("Total Count",image)
	#cv2.waitKey(0)
	return image

######################################################################

################################################################################################
def CreateGanttChart(frameNum,maxValue,tickSpace):
    ylabels=["Formwork activities" ,"Rebar activities","Concrete activities"]          
    ilen=len(ylabels)
    maxValue=129
    pos = np.arange(0.5,ilen*0.5+0.5,0.5)
    fig = plt.figure(figsize=(20, (300*2)/100))

    ax = fig.add_subplot(111)
    plt.xlim(0, 129)
    frameThreshold=43
    for i in range(len(ylabels)):
         if ylabels[i] == "Rebar activities":
            bar_color = 'blue'
            start_date=0
            if(frameNum<frameThreshold):
            	width=frameNum
            else:
            	width=frameThreshold
            
         elif ylabels[i] == "Concrete activities":
            bar_color = 'green'
            start_date=frameThreshold
            if(frameNum>frameThreshold):
            	width=frameNum-frameThreshold
            else:
            	continue

         elif ylabels[i] == "Formwork activities":
            bar_color = 'red'
            continue   

  
         ax.barh((i*0.5)+0.5, width, left=start_date, height=0.3, align='center', edgecolor='lightgreen', color=bar_color, alpha = 0.8)
    locsy, labelsy = plt.yticks(pos,ylabels)
    #locsx, labelsx = plt.yticks(pos,xlabels)
    plt.setp(labelsy, fontsize = 16)
    plt.xticks(fontsize=20)
    plt.grid(True)
    ###########

    #ax.set_xlim(xmin=0, xmax=maxValue)
    ax.set_xlabel("Hour",fontsize=18) 
    
    ###########
    
    
#    ax.axis('tight')
    ax.set_ylim(ymin = -0.1, ymax = ilen*0.5+0.5)
    #ax.grid(color = 'g', linestyle = ':')
    #plt.xticks(np.arange(11), ('7:00', '8:00', '9:00' , "10:00","11:00" ,"12:00","13:00","14:00","15:00","16:00","17:00",))

 
    #font = font_manager.FontProperties(size='small')
    #ax.legend(loc=0,prop=font)
    ax.margins(x=0)
    ax.invert_yaxis()
    #fig.autofmt_xdate()
    #plt.xticks(np.arange(0, maxValue, tickSpace))
    plt.xticks(np.arange(0, maxValue, tickSpace), ('7:00', '8:00', '9:00' , "10:00","11:00" ,"12:00","13:00","14:00","15:00","16:00","17:00","17:20"))
    #print("*in Gant Graph*")
    #print(0, maxValue, tickSpace)
    plt.savefig('gant.png')
    img=cv2.imread("gant.png")
    cv2.imshow("Gant chart",img)
    cv2.waitKey(100)

    pathtoSaveFile=os.path.join("gantCharts" , "ml_frame"+"_"+str(frameNum)+".png")
    cv2.imwrite(pathtoSaveFile, img)
    return img
    





################################################################################################
def barGraphTwoDataSets(datax,datay1,datay2,title,labelXAxis,maxValue,tickSpace,space=0.5,barWidth=0.3):
	maxValue=129
	plt.rcParams['axes.xmargin'] = 0
	plt.figure()
	plt.xlabel(labelXAxis)
	plt.margins(x=0)
	plt.rcParams['axes.xmargin'] = 0
	plt.ylabel("Man-hour")
	plt.ylim(0, 200)  
	#print(datax)
	plt.xlim(0, 129) 
	ax = plt.subplot(111)
	#ax.set_xlim(200);
	#ax.margins(x=0)
	ax.bar(datax, datay1,width=barWidth,color='b',align='edge')
	ax.margins(x=0)
	ax.bar(datax+space, datay2,width=barWidth,color='g',align='edge')
	ax.margins(x=0)
	green_patch = mpatches.Patch(color='green', label='Concrete Workers')
	blue_patch = mpatches.Patch(color='blue', label='Rebar Workers')
	plt.legend(handles=[green_patch,blue_patch] , loc=2)
	plt.grid(True)
	plt.xticks(np.arange(0, maxValue, tickSpace), ('7:00', '8:00', '9:00' , "10:00","11:00" ,"12:00","13:00","14:00","15:00","16:00","17:00",))
	locs, labels = plt.xticks()
	#print(locs)
	#print("*in Bar Graph*")
	#print(0, maxValue, tickSpace)
	#print("*****")
	ticks = [tick for tick in plt.gca().get_yticks() if (tick ==0)  or (tick >1)]
	plt.gca().set_yticks(ticks)
	plt.title(title)
	plt.savefig('instWorkersx.png')
	image = cv2.imread('instWorkersx.png')
	return image







######################################################################

#https://matplotlib.org/users/pyplot_tutorial.html
def drawDataLine(datax,datay1,datay2,title,labelXAxis,maxValue,tickSpace):
	plt.figure()
	plt.xlabel(labelXAxis)
	plt.ylabel("Worker Count by Trade")
	''' 	
	plt.xticks(np.arange(124), ('7:00', '7:05', '7:10', '7:15', '7:20','7:25', '7:30', '7:35', '7:40', '7:45','7:50', '7:55', 
'8:00', '8:05', '8:10','8:15', '8:20', '8:25', '8:30','8:35', '8:40','8:45', '8:50', '8:55', 
'9:00' , '9:05' , '9:10','9:15' , '9:20','9:25','9:30',"9.35","9,41","9:45","9:50","9:55",
"10:00","10:06","10:11","10:15","10:20","10:25","10:31","10:36","10:40","10:45","10:50","10:55",
"11:00" ,"11:05","11:11","11:15","11:20","11:25","11:30","11:35","11:41","11:45","11:50","11:55",
"12:00","12:05","12:11","12:15","12:20","12:25","12:30","12:35","12:40","12:45","12:50","12:55",
"13:00","13:06","13:10","13:15","13:20","13:25","13:31","13:35","13:41","13:45","13:50","13:55",
"14:00","14:06","14:10","14:15","14:20","14:25","14:30","14:36","14:40","14:45","14:50","14:55",
"15:00","15:05","15:10","15:15","15:20","15:25","15:30","15:35","15:40","15:45","15:50","15:55",
"16:00","16:05","16:10","16:15","16:20","16:25","16:30","16:35","16:40","16:45","16:50","16:55",
"17:00","17:05","17:10","17:15","17:20"
))
'''
 	plt.xticks(np.arange(11), ('7:00', 
'8:00', 
'9:00' , 
"10:00",
"11:00" ,
"12:00",
"13:00",
"14:00",
"15:00",
"16:00",
"17:00",
))
        green_patch = mpatches.Patch(color='green', label='Concrete Workers')
	blue_patch = mpatches.Patch(color='blue', label='Rebar Workers')
	plt.legend(handles=[green_patch,blue_patch])
	plt.plot(datax,datay1,"b")
        #plt.plot(datax,datay1,"bx")
	#plt.plot(datax,datay2,"bx")
	plt.plot(datax,datay2,"g")
	plt.grid(True)
	#plt.axis([0,44,1, 350])
	#x = [0,5,9,10,15]
	plt.xticks(np.arange(0, maxValue, tickSpace))
	plt.title(title)
	plt.savefig('instWorkers.png')
	image = cv2.imread('instWorkers.png')
	#plt.show()
	return image




def drawProgressBar(progress): 
	objects = ('Formworker activities ',  'Concerete  activities','Rebar  activities')
	y_pos = np.arange(len(objects))
	
	plt.figure(figsize=(15,5))
	#plt.xticks(np.arange(0, maxValue, tickSpace))
	plt.xticks(np.arange(11), ('7:00', '8:00', '9:00' , "10:00","11:00" ,"12:00","13:00","14:00","15:00","16:00","17:00"))
	plt.grid(True)
	plt.barh(y_pos, progress, align='center', alpha=0.5)
	plt.yticks(y_pos, objects)
	plt.xlabel('Time')
	plt.title('Activitiy Progress Chart')
	plt.savefig('progBar.png')
	#plt.show()
	
	image = cv2.imread('progBar.png')
	#cv2.imshow("title",image)
	#cv2.waitKey(1000)
	return image

def drawBarChartNumOfWorkers(count): 
	objects = ('Form Workers', 'Rebar Workers', 'Concerete Workers')
	y_pos = np.arange(len(objects))
	
	plt.figure(figsize=(15,5))
	plt.xticks(np.arange(0, 10, 1))
	plt.grid(True)
	plt.barh(y_pos, count, align='center', alpha=0.5)
	plt.yticks(y_pos, objects)
	plt.xlabel('Count')
	plt.title('Instantaneous Number of Workers')
	plt.savefig('books_read.png')
	#plt.show()
	
	image = cv2.imread('books_read.png')
	#cv2.imshow("title",image)
	#cv2.waitKey(1000)
	return image

def run(fileName,img,frameNum):
	global rebarWorkernum,ConcerterWorkernum,formWorkernum,	 rebarWorkeFullnum,ConcerterWorkerFullnum,formWorkerFullnum,rebarWorkernumHistory,ConcerterWorkernumHistory,formWorkernumHistory,rebarWorkeFullnumHistory,ConcerterWorkerFullnumHistory,formWorkerFullnumHistory
	with open(fileName) as json_file:  
		print("Reading from JSON file " +fileName)   		
		data = json.load(json_file)
		print("Data loaded from JSON file")
    		for p in data['detections']:
        		#print('object: ' + p['object'])
        		#print('x1: ' + str(p['x1']))
        		#print('x2: ' + str(p['x2']))
			#print('y1: ' + str(p['y1']))
			#print('y2: ' + str(p['y2']))
        		#print('')
			x1=p['x1']
			x2=p['x2']
			y1=p['y1']
			y2=p['y2']
			label=""
			#cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)     #d top-left corner and bottom-right corner of rectangle

			'''
				
			if (frameNum<35):
				label="Rebar Worker"
				color=(0,255,0)
				rebarWorkernum=rebarWorkernum+1 
				
			if (frameNum==40 or frameNum==42 or frameNum==36 or frameNum==39 or frameNum==46):
				label="Rebar Worker"
				color=(0,255,0)
				rebarWorkernum=rebarWorkernum+1 
				
			if (frameNum==55):
				if(x2<595):
					rebarWorkernum=rebarWorkernum+1 
					label="Rebar Worker"
					color=(0,255,0)    #d top-left corner and bottom-right corner of rectangle  #bgr
					continue
				else:
					ConcerterWorkernum=ConcerterWorkernum+1
					label="Concerter Worker"
					color=(255,0,0)
					
			
			if (frameNum==41):
				if(x2<933):
					rebarWorkernum=rebarWorkernum+1 
					label="Rebar Worker"
					color=(0,255,0)    #d top-left corner and bottom-right corner of rectangle  #bgr
					
				else:
					ConcerterWorkernum=ConcerterWorkernum+1
					label="Concerter Worker"
					color=(255,0,0)
					

			if (frameNum==35):
				if(x2<993):
					rebarWorkernum=rebarWorkernum+1 
					label="Rebar Worker"
					color=(0,255,0)    #d top-left corner and bottom-right corner of rectangle  #bgr
					
				else:
					ConcerterWorkernum=ConcerterWorkernum+1
					label="Concerter Worker"
					color=(255,0,0)
		       
 			'''
                   
                        #general rule
			if (frameNum<44):
					rebarWorkernum=rebarWorkernum+1 
					label="Rebar Worker"
					color=rebarColor    #d top-left corner and bottom-right corner of rectangle  #bgr
			if(label==""):
				if(x2<545):
					rebarWorkernum=rebarWorkernum+1 
					label="Rebar Worker"
					color=rebarColor   #d top-left corner and bottom-right corner of rectangle  #bgr
				
				else:
					ConcerterWorkernum=ConcerterWorkernum+1
					label="Concerter Worker"
					color=concereteColor
				
                        labelWidth=120
                        if (label=="Concerter Worker"):
				labelWidth=labelWidth+30

			cv2.rectangle(img,(x1,y1),(x2,y2),color,2)     #d top-left corner and bottom-right corner of rectangle  #BGR # border for object
			overlay=img.copy()
			cv2.rectangle(overlay,(x1,y1-25),(x1+labelWidth,y1-10),color,thickness=-1)     #top-left corner and bottom-right corner of rectangle  #BGR #border for label 
			opacity=0.5
			cv2.addWeighted(overlay, opacity, img, 1 - opacity, 0, img)
			cv2.putText(img,label,(x1,y1-12), font, 0.5,(255,255,255),1,cv2.LINE_AA)
	count = [0,rebarWorkernum,ConcerterWorkernum]
       
        #################################################
	rebarWorkernumHistory.append(rebarWorkernum)
	ConcerterWorkernumHistory.append(ConcerterWorkernum)
	formWorkernumHistory.append(0)
 

        ##################################################



     
	rebarWorkeFullnum=rebarWorkeFullnum+rebarWorkernum
	ConcerterWorkerFullnum=ConcerterWorkerFullnum+ConcerterWorkernum
	formWorkerFullnum=formWorkerFullnum+0
	##################################################
	rebarWorkeFullnumHistory.append(rebarWorkeFullnum)
	ConcerterWorkerFullnumHistory.append(ConcerterWorkerFullnum)
	formWorkerFullnumHistory.append(0)
	if(frameNum%10==0):
		rebarWorkeFullnumHistoryEdited.append(rebarWorkeFullnum)
		ConcerterWorkerFullnumHistoryEdited.append(ConcerterWorkerFullnum)
	else:
		rebarWorkeFullnumHistoryEdited.append(0)
		ConcerterWorkerFullnumHistoryEdited.append(0)
        ###################################################

	datay1=rebarWorkernumHistory
	datay2=ConcerterWorkernumHistory
	datax=list(range(len(datay1)))
	#print(datax)
	#exit()
	#print(datay1)
	#print(datax)
	maxValue=len(datax)+5
	#print(maxValue)

	tickSpace=12
	imgBarChart=drawDataLine(datax,datay1,datay2,'Worker Count',"Hour",maxValue,tickSpace)
	pathtoSaveFile=os.path.join("instantiniousCurves" , "ml_frame"+"_"+str(frameNum)+".png")
	cv2.imwrite(pathtoSaveFile, imgBarChart) 
 	imgBarChart=barGraphTwoDataSets(array( datax ),datay1,datay2,'Worker Count',"Hour",maxValue,tickSpace)
	pathtoSaveFile=os.path.join("instantiniousBarCharts" , "ml_frame"+"_"+str(frameNum)+".png")
	cv2.imwrite(pathtoSaveFile, imgBarChart) 
#exit()

        ###################################################

	datay1=rebarWorkeFullnumHistory
	datay2=ConcerterWorkerFullnumHistory
	datax=list(range(len(datay1)))
	#print(datax)
	#exit()
	#print(datay1)
	#print(datax)
	maxValue=len(datax)+5
	tickSpace=12
	imgtOTALBarChart=drawDataLine(datax,datay1,datay2,'Worker Total Count',"Hour",maxValue,tickSpace)
	pathtoSaveFile=os.path.join("TotalCurves" , "ml_frame"+"_"+str(frameNum)+".png")
	cv2.imwrite(pathtoSaveFile, imgtOTALBarChart) 
 	imgtOTALBarChart=barGraphTwoDataSets(array( datax ),datay1,datay2,'Worker Count',"Hour",maxValue,tickSpace)
	pathtoSaveFile=os.path.join("totalBarCharts" , "ml_frame"+"_"+str(frameNum)+".png")
	cv2.imwrite(pathtoSaveFile, imgBarChart) 
        
	###########################################################
	#work with edited history num



	datay1=rebarWorkeFullnumHistoryEdited
	datay2=ConcerterWorkerFullnumHistoryEdited
	datax=list(range(len(datay1)))
	#print(datax)
	#exit()
	#print(datay1)
	#print(datax)
	maxValue=len(datax)+5
	tickSpace=12
 	imgtOTALBarChart=barGraphTwoDataSets(array( datax ),datay1,datay2,'Worker Count',"Hour",maxValue,tickSpace,space=2.0 ,barWidth=2)
	pathtoSaveFile=os.path.join("totalBarChartsEdited" , "ml_frame"+"_"+str(frameNum)+".png")
	cv2.imwrite(pathtoSaveFile, imgtOTALBarChart) 
        ###############################################################
	progress=[0,1,2]
        drawProgressBar(progress)



       ############################################################

	gantChart=CreateGanttChart(frameNum,maxValue,tickSpace)







	###################################################
	#imgBarChart=drawBarChartNumOfWorkers(count)

	heigtOfInstBarChart=500
	imgBarChart = cv2.resize(imgBarChart, (1280, heigtOfInstBarChart)) 

	both = np.vstack((imgBarChart,img))
	cv2.imshow("indus.ai",both)
	pathtoSaveFile=os.path.join("ML_frames_WithBarGraph" , "ml_frame"+"_"+str(frameNum)+".png")
	cv2.imwrite(pathtoSaveFile, both) 
        #cv2.waitKey(0)
	print(rebarWorkeFullnum,ConcerterWorkerFullnum,formWorkerFullnum)
	#raw_input("Total count printed")
	count = [0,rebarWorkeFullnum,ConcerterWorkerFullnum]
        #imgtOTALBarChart=drawBarChartTotalNumOfWorkers(count)
      
        ########################################################################################
	imgtOTALBarChart = cv2.resize(imgtOTALBarChart, (1200, 720+heigtOfInstBarChart)) 
        both = np.hstack((both,imgtOTALBarChart))
	pathtoSaveFile=os.path.join("ML_frames_WithTWOBarGraph" , "ml_frame"+"_"+str(frameNum)+".png")
	cv2.imwrite(pathtoSaveFile, both) 
 
	####################################  Add Segmentation Frame##########################	
	segmentationImage=cv2.imread("Segmentations/segmentFrame" + str(frameNum)+".png")
	pathtoSaveFile=os.path.join("ML_frames_WithAllInfo" , "ml_frame"+"_"+str(frameNum)+".png")
	segmentationImage = cv2.resize(segmentationImage, (2480, 300)) 
        #total and Segnemt
	#np.vstack(imgtOTALBarChart,segmentationImage)
	
	###########################Add ProgressBar###################################################
	progressBarImage=cv2.imread("progressBars/progressBarFrame" + str(frameNum)+".png")
	pathtoSaveFile=os.path.join("ML_frames_WithTWOBarGraphProgressBar" , "ml_frame"+"_"+str(frameNum)+".png")
	progressBarImage = cv2.resize(progressBarImage, (2480, 300)) 
	gantChart = cv2.resize(gantChart, (2480, 300)) 
	#print(both.shape)
	#print(progressBarImage.shape)
	both2 = np.vstack((gantChart,both))
	cv2.imwrite(pathtoSaveFile, both2) 
        ########################################################################################################
	#exit()



############################################################
rebarWorkernumHistory=[]
ConcerterWorkernumHistory=[]
formWorkernumHistory=[]
rebarWorkeFullnumHistory=[]
ConcerterWorkerFullnumHistory=[]
formWorkerFullnumHistory=[]
rebarWorkeFullnumHistoryEdited=[]
ConcerterWorkerFullnumHistoryEdited=[]





#############################################################
rebarColor=(255,0,0)	   ##bgr	
concereteColor=(0,255,0)   #bgr
folderJSONName="Jsonfiles/"
folderMLFramesName="ML_frames/"
folderFramesName="frames/"
shutil.rmtree("ML_frames", ignore_errors=True, onerror=None)
shutil.rmtree("ML_frames_noInfo", ignore_errors=True, onerror=None)
shutil.rmtree("ML_frames_WithBarGraph", ignore_errors=True, onerror=None)
shutil.rmtree("ML_frames_WithTWOBarGraph", ignore_errors=True, onerror=None)
if not os.path.exists("ML_frames_noInfo"):
    os.makedirs("ML_frames_noInfo")
if not os.path.exists("ML_frames_WithBarGraph"):
    os.makedirs("ML_frames_WithBarGraph")
if not os.path.exists("ML_frames_WithTWOBarGraph"):
    os.makedirs("ML_frames_WithTWOBarGraph")   #

shutil.rmtree("ML_frames_WithTWOBarGraphProgressBar", ignore_errors=True, onerror=None)
if not os.path.exists("ML_frames_WithTWOBarGraphProgressBar"):
    os.makedirs("ML_frames_WithTWOBarGraphProgressBar")


shutil.rmtree("ML_frames_WithAllInfo", ignore_errors=True, onerror=None)
if not os.path.exists("ML_frames_WithAllInfo"):
    os.makedirs("ML_frames_WithAllInfo")

shutil.rmtree("TotalCurves", ignore_errors=True, onerror=None)
if not os.path.exists("TotalCurves"):
    os.makedirs("TotalCurves")


shutil.rmtree("instantiniousCurves", ignore_errors=True, onerror=None)
if not os.path.exists("instantiniousCurves"):
    os.makedirs("instantiniousCurves")  #instantiniousBarCharts

shutil.rmtree("instantiniousBarCharts", ignore_errors=True, onerror=None)
if not os.path.exists("instantiniousBarCharts"):
    os.makedirs("instantiniousBarCharts")         #totalBarCharts

shutil.rmtree("totalBarCharts", ignore_errors=True, onerror=None)
if not os.path.exists("totalBarCharts"):
    os.makedirs("totalBarCharts")     #totalBarChartsEdited


shutil.rmtree("totalBarChartsEdited", ignore_errors=True, onerror=None)
if not os.path.exists("totalBarChartsEdited"):
    os.makedirs("totalBarChartsEdited") 


shutil.rmtree("gantCharts", ignore_errors=True, onerror=None)
if not os.path.exists("gantCharts"):
    os.makedirs("gantCharts")

rebarWorkeFullnum,ConcerterWorkerFullnum,formWorkerFullnum=0,0,0
frameNum=1
while(True):
	ConcerterWorkernum,rebarWorkernum,formWorkernum=0,0,0	
	fileNamejSON="frame"+str(frameNum)+".txt"
	fileNamejSON=folderJSONName+fileNamejSON
	#if (frameNum<61):
			#continue
	if(os.path.exists(fileNamejSON)):
		print(fileNamejSON)
		
		#fileNameImg="ml_frame_"+str(frameNum)+".png"  
		fileNameImg="frame_"+str(frameNum)+".png"              
		#fileNameImg=folderMLFramesName+fileNameImg
		fileNameImg=folderFramesName+fileNameImg
		#print(fileNameImg)
		#raw_input("press any key")
		img=cv2.imread(fileNameImg)
		run(fileNamejSON,img,frameNum)	
		f.write("ml_frame"+"_"+str(frameNum)+".png" + ","+str(formWorkernum)+","+str(rebarWorkernum)+"," + str(ConcerterWorkernum)+"\n")
		#cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
		#cv2.imshow("ml_frame_"+str(frameNum)+".png",img)
		cv2.imshow("indus.ai",img)
		pathtoSaveFile=os.path.join("ML_frames_noInfo" , "ml_frame"+"_"+str(frameNum)+".png")
		cv2.imwrite(pathtoSaveFile, img) 
		if cv2.waitKey(1000) & 0xff==ord('q'):
			break
		print(frameNum)
		#raw_input("press any key to continue")
		frameNum=frameNum+1
		if (frameNum==240):
			break
	else:
		print( fileNamejSON +"does not exist")
		break


