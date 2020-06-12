import os
import json
import numpy as np
from flask import Flask, request, Response
from detector import Detector
import sys
#sys.path.append('/home/mawdoo3/Muhystuff/research/PV_images/PV_thermal')
from config import config

app = Flask(__name__)

@app.route('/detector', methods=['GET','POST'])

def detector():
    global detect
    image = request.args.get('path', None)
    ans = detect.infer(image)
    result = json.dumps({'status': 'SUCCESS',
                         'result': ans})
    return (result, 200)


if __name__ == '__main__':
    global detect
    detect = Detector(config['model_path'])
    print('Model Loaded')
    app.run(debug=True)
