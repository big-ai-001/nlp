import requests
import numpy as np
from scipy.io import wavfile

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def call_api(data):
    headers = {
        'Content-Type': 'application/json'
    }
    server = 'https://api.twman.org/AudioDenoise'
    response = requests.post(server, headers=headers, json=data, verify=False)
    return response.json()

sampling_rate, request_wav = wavfile.read('D:\TW_DEEP_MASTER\Denoise.wav')


data = {"token":"Deep Learning 101", "model_type":"Conv-denoiser","input_wav":request_wav.tolist()}

out = call_api(data)
b = out.get('output')
wavfile.write('api_denoise.wav', 16000, np.array(b).astype(np.int16))
pass
