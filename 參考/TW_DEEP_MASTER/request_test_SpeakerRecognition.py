import requests
import numpy as np
from scipy.io import wavfile

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def call_api(data):
    headers = {
        'Content-Type': 'application/json'
    }
    server = 'https://api.twman.org/SpeakerRecognition'
    response = requests.post(server, headers=headers, json=data, verify=False)
    return response.json()

sampling_rate, test_wav = wavfile.read('D:\TW_DEEP_MASTER/Speaker.wav')
enroll_wav_lst = {
    '劉德華_0':wavfile.read('D:\TW_DEEP_MASTER\enrolls/劉德華_enroll_1.wav')[1].tolist(), 
    '劉德華_1':wavfile.read('D:\TW_DEEP_MASTER\enrolls/劉德華_enroll_2.wav')[1].tolist(), 
    '劉德華_2':wavfile.read('D:\TW_DEEP_MASTER\enrolls/劉德華_enroll_3.wav')[1].tolist(), 
    '劉德華_3':wavfile.read('D:\TW_DEEP_MASTER\enrolls/劉德華_enroll_4.wav')[1].tolist(), 
    '劉德華_4':wavfile.read('D:\TW_DEEP_MASTER\enrolls/劉德華_enroll_5.wav')[1].tolist(), 
    '蔡康永_0':wavfile.read('D:\TW_DEEP_MASTER\enrolls/蔡康永_enroll_1.wav')[1].tolist(), 
    '蔡康永_1':wavfile.read('D:\TW_DEEP_MASTER\enrolls/蔡康永_enroll_2.wav')[1].tolist(), 
    '蔡康永_2':wavfile.read('D:\TW_DEEP_MASTER\enrolls/蔡康永_enroll_3.wav')[1].tolist(), 
    '蔡康永_3':wavfile.read('D:\TW_DEEP_MASTER\enrolls/蔡康永_enroll_4.wav')[1].tolist(), 
    '蔡康永_4':wavfile.read('D:\TW_DEEP_MASTER\enrolls/蔡康永_enroll_5.wav')[1].tolist()
}
data = {"token":"www.interactionx.co", "model_type":"sincnet_plda", "enroll_list":enroll_wav_lst, "test_wav":test_wav.tolist()}

out = call_api(data)
print(out)
pass
