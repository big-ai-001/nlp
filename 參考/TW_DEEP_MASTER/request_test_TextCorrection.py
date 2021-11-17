import requests

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def call_api(data):
    headers = {
        'Content-Type': 'application/json'
    }
    server = 'https://api.twman.org/TextCorrection'
    response = requests.post(server, headers=headers, json=data, verify=False)
    return response.json()

text = '金天天汽真好，在去一次行鄭院敢覺不錯'

data = {"token":"Deep Learning 101", "model_type":"bert", "input_text":text}

out = call_api(data)
print(out)
pass
