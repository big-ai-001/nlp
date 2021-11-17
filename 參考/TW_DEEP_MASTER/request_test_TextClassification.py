import requests

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def call_api(data):
    headers = {
        'Content-Type': 'application/json'
    }
    server = 'https://api.twman.org/TextClassification'
    response = requests.post(server, headers=headers, json=data, verify=False)
    return response.json()

input_text = '辛苦老師啦，很喜歡你的上課風格會再向學弟妹推薦您'

data = {"token":"Deep Learning 101", "model_type":"bert_lstm_service", "input_text":input_text}

out = call_api(data)
print(out)
pass
