import os
import keras
import tensorflow as tf
import numpy as np
from keras.models import load_model
from utils import load_cell_image, normalize
import sys
sys.path.append('/home/mawdoo3/Muhystuff/research/PV_images/PV_thermal')
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
                    return 'Defetected'
                else:
                    return 'Not Defected'

#if __name__ == '__main__':
#    detector = Detector(config['model_path'])
#    path = '/home/mawdoo3/Muhystuff/research/PV_images/elpv-dataset/images/'
#    ans = detector.infer(os.path.join(path, 'cell0023.png'))
#    print(ans)
#    #for i in os.listdir(path):
#    #    ans = detector.infer(os.path.join(path,i))
#    #    print(ans)
