import requests

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def call_api(data):
    headers = {
        'Content-Type': 'application/json'
    }
    server = 'https://api.twman.org/NamedEntityRecognition'
    response = requests.post(server, headers=headers, json=data, verify=False)
    return response.json()

input_text = '臺灣知名女模特兒林志玲嫁給日本舞者黑澤良平'

data = {"token":"Deep Learning 101", "model_type":"bert_base_msra", "input_text":input_text}

out = call_api(data)
print(out)
pass
