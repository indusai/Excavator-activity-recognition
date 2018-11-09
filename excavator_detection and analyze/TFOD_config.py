import os




everyNFrame=1

# List of the strings that is used to add correct label for each box.


PATH_TO_LABELS ="/Users/chen/PycharmProjects/indus.ai-applyingDetector-master/labels/object-detection_6_labels.pbtxt"


thershold=0.3






#multiTruckClassifierFilePath="models/multiTruckModel_8_net11_32px_87.68%_20180529-153539.keras2"




# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = 'jan4_7_label_rfcn.pb'
#PATH_TO_CKPT = 'frozen_inference_graph3classes3april.pb'
#




PATH_TO_CKPT = "/Users/chen/PycharmProjects/indus.ai-applyingDetector-master/jan4_7_label_rfcn.pb"
#videoFile="test5.mp4"


#videoFile="videos/Skanska_UCSF_Site1_NE_V3_2018-09-04-19-40-46_2018-09-04-20-10-47 .mp4"
videoFile="/Users/chen/Desktop/detector.mp4"


NUM_CLASSES = 7
startingFrame=0
