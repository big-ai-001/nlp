import requests

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def call_api(data):
    headers = {
        'Content-Type': 'application/json'
    }
    server = 'https://api.twman.org/TextSimilarity'
    response = requests.post(server, headers=headers, json=data, verify=False)
    return response.json()

text1 = '我想去洗手間'
text2 = '我想去廁所'

data = {"token":"Deep Learning 101", "model_type":"albert", "input_text_1":text1, "input_text_2":text2}

out = call_api(data)
print(out)
pass
