import requests

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def call_api(data):
    headers = {
        'Content-Type': 'application/json'
    }
    server = 'https://api.twman.org/QuestionAnswering'
    response = requests.post(server, headers=headers, json=data, verify=False)
    return response.json()

context = '超人氣動畫《鬼滅之刃》首部劇場版《無限列車篇》上週正式在台上映，立刻掀起全台觀影熱潮，3天票房勇破1.1億，迅速登上年度動畫票房冠軍，同時也是今年開片日票房冠軍，更是今年最快破億電影，後勢持續看漲。代理發行該片的木棉花昨也正式宣布，本週五（6日）將加映中文配音版本，以及影迷不停敲碗的「IMAX」版。'
question = '鬼滅之刃劇場版無限列車篇上映三天票房多少？'

data = {"token":"Deep Learning 101", "model_type":"bert_base_drcd", "context":context, "question":question}

out = call_api(data)
print(out)
pass
