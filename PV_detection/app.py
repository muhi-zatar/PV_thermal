import os
import numpy as np
from flask import Flask, request, Response
from detector import Detector
from config import config

#detect = None

app = Flask(__name__)

@app.route('/detector', methods=['GET','POST'])
    #       params=[Param(name='image', required=True, type=bytes, source=['body-data'])])

def detector():
    global detect
    image = request.args.get('path', None)
    #import pdb;pdb.set_trace()
    #nparr = np.fromstring(r.data, np.uint8)
    ans = detect.infer(image)
    print('here')
    return ans
    #return 'why hello there'


if __name__ == '__main__':
    global detect
    detect = Detector(config['model_path'])
    print('Model Loaded')
    app.run(debug=True)
