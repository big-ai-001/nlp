import requests
import numpy as np
from scipy.io import wavfile

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def call_api(data):
    headers = {
        'Content-Type': 'application/json'
    }
    server = 'https://api.twman.org/SpeechRecognition'
    response = requests.post(server, headers=headers, json=data, verify=False)
    return response.json()

sampling_rate, request_wav = wavfile.read('D:\TW_DEEP_MASTER\TonSpeech.wav')


data = {"token":"Deep Learning 101", "model_type":"asr_omega","input_wav":request_wav.tolist()}

out = call_api(data)
print(out)
pass
