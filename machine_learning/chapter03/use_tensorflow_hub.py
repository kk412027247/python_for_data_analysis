import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import os

proxy = 'http://127.0.0.1:8123'
os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy



config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

num_classes = 10
img_rows, img_cols = 28, 28
num_channels = 1
input_channels = 1
input_shape = (img_rows, img_cols, num_channels)

url = 'https://tfhub.dev/google/tf2-preview/inception_v3/feature_vector/2'

hub_feature_extractor = hub.KerasLayer(
    url,
    trainable=False,
    input_shape=(299, 299, 3),
    output_shape=(2048,),
    dtype=tf.float32)

inception_model = Sequential(
    [hub_feature_extractor, Dense(num_classes, activation='softmax')],
    name='inception_tf_hub'
)
