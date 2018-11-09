import tensorflow as tf
from tensorflow.python.platform import gfile

#filename = '/Users/chen/simple-object-tracking/jan4_7_label_rfcn.pb'



def graphdef_to_pbtxt(filename):
  with gfile.FastGFile(filename,'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')
    tf.train.write_graph(graph_def, '/Users/chen/simple-object-tracking/', 'protobuf.pbtxt', as_text=True)
  return


graphdef_to_pbtxt('/Users/chen/simple-object-tracking/jan4_7_label_rfcn.pb')

