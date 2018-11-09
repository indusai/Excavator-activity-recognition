import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf

import zipfile
import cv2
import shutil
from  TFOD_config import *
import collections
from collections import defaultdict
import pandas as pd


# In[3]:

'''
# This is needed to display the images.
get_ipython().magic(u'matplotlib inline')
# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")
'''

# ## Object detection imports
# Here are the imports from the object detection module.



from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

#from utils import label_map_util

#from utils import visualization_utils as vis_util


label_path = '/Users/chen/PycharmProjects/indus.ai-applyingDetector-master/labels/object-detection_7_labels.pbtxt'
videoFile = 'Users/chen/Desktop/detection.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# fourcc = cv2.VideoWriter_fourcc(*'FMP4')
#video_creator = cv2.VideoWriter( "Users/chen/Desktop/output1.mp4", fourcc, 20.0, (960, 720))




# Delete files from previous runs

shutil.rmtree("ML_frames", ignore_errors=True, onerror=None)
if not os.path.exists("ML_frames"):
    os.makedirs("ML_frames")


detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile('/Users/chen/PycharmProjects/indus.ai-applyingDetector-master/jan4_7_label_rfcn.pb', 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

print("Loaded a (frozen) Tensorflow model into memory")

# multiTruckClassifier=loadModel(detection_graph)


# ## Loading label map
# Label maps map indices to category names, so that when our convolution network predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility functions, but anything that returns a dictionary mapping integers to appropriate string labels would be fine

# In[8]:


label_map = label_map_util.load_labelmap(label_path)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)
#category_index = label_map_util.create_category_index_from_labelmap(label_path, use_display_name=True)

#print(label_map)
print(" Loaded label map")


# raw_input("press any key to continue")
# ## Helper code

# In[9]:


def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)


frameNum = 0
cap = cv2.VideoCapture("/Users/chen/Desktop/detection2.mp4")
with detection_graph.as_default():
    with tf.Session(graph=detection_graph) as sess:
        ret = True
        boxes_ =0
        classes_ =0
        scores_ =0
        while (ret):
            ret, image_np = cap.read()
            frameNum = frameNum + 1
            cv2.imwrite(os.path.join("frames", "frame" + "_" + str(frameNum) + ".png"), image_np)
            image_path = os.path.join("frames", "frame" + "_" + str(frameNum) + ".png")
            if (frameNum % everyNFrame != 0) or (frameNum < startingFrame):
                print("skipping " + str(frameNum))
                continue
            if frameNum % 16 == 1:
                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(image_np, axis=0)
                # Definite input and output Tensors for detection_graph
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
                # Each box represents a part of the image where a particular object was detected.
                boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                # Each score represent how level of confidence for each of the objects.
                # Score is shown on the result image, together with the class label.
                scores = detection_graph.get_tensor_by_name('detection_scores:0')
                classes = detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = detection_graph.get_tensor_by_name('num_detections:0')
                if (image_np_expanded is None):
                    break
                # Actual detection.
                (boxes_, scores_, classes_, num_detections) = sess.run(
                    [boxes, scores, classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})
                # Visualization of the results of a detection.

            vis_util.visualize_boxes_and_labels_on_image_array(image_np,
                                                               image_path,
                                                               np.squeeze(boxes_),
                                                               np.squeeze(classes_).astype(np.int32),
                                                               np.squeeze(scores_),
                                                               category_index,
                                                               instance_masks = None,
                                                               max_boxes_to_draw = 4,
                                                               use_normalized_coordinates=True,
                                                               min_score_thresh=0.5,
                                                               line_thickness=4)


#                boxes_16.append(boxes[0,(0,1,2,3)])



#


            #      plt.figure(figsize=IMAGE_SIZE)
            #      plt.imshow(image_np)
            # cv2.imshow('image',cv2.resize(image_np,(960,720)))
            imgToShow = cv2.resize(image_np, (960, 720))
#            video_creator.write(imgToShow)
#            cv2.imshow('image', imgToShow)
            cv2.imwrite(os.path.join("ML_frames", "ml_frame" + "_" + str(frameNum) + ".png"), imgToShow)

            if cv2.waitKey(25) & 0xFF == ord('q'):
               cv2.destroyAllWindows()
               cap.release()
               break

'''        print([category_index.get(i) for i in classes[0]])
            print(boxes.shape)
            print(num_detections)'''


