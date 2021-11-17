import requests
import numpy as np
from scipy.io import wavfile

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def call_api(data):
    headers = {
        'Content-Type': 'application/json'
    }
    server = 'https://api.twman.org/SpeechSeparation'
    response = requests.post(server, headers=headers, json=data, verify=False)
    return response.json()

sampling_rate, request_wav = wavfile.read('D:\TW_DEEP_MASTER\Separation.wav')

data = {"token":"Deep Learning 101", "model_type":"sudormrf","input_wav":request_wav.tolist()}

out = call_api(data)
b, c = out.get('output')
wavfile.write('api_sep1.wav', 16000, np.array(b).astype(np.int16))
wavfile.write('api_sep2.wav', 16000, np.array(c).astype(np.int16))
pass
