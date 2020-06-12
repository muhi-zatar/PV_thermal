import os
import keras
import tensorflow as tf
import numpy as np
from keras.models import load_model
from utils import load_cell_image, normalize
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config

class Detector(object):
    def __init__(self, model_path):
        self.session = tf.Session()
        keras.backend.set_session(self.session)
        self.model = load_model(model_path)
        self.model._make_predict_function()

    def infer(self, input_image):
        with self.session.as_default():
            with self.session.graph.as_default():
                test = load_cell_image(input_image)
                image = normalize(test)
                hey = np.expand_dims(image, axis=-1)
                vecs = np.expand_dims(hey, axis=0)
                pred = self.model.predict(vecs)
                if pred >= 0.5:
                    return 'PV module is Defetected'
                else:
                    return 'PV module is not Defected'
