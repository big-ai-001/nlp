import requests

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def call_api(data):
    headers = {
        'Content-Type': 'application/json'
    }
    server = 'https://api.twman.org/QuestionAnsweringPlus'
    response = requests.post(server, headers=headers, json=data, verify=False)
    return response.json()

context_ls = [
    '超人氣動畫《鬼滅之刃》首部劇場版《無限列車篇》上週正式在台上映，立刻掀起全台觀影熱潮，3天票房勇破1.1億，迅速登上年度動畫票房冠軍，同時也是今年開片日票房冠軍，更是今年最快破億電影，後勢持續看漲。代理發行該片的木棉花昨也正式宣布，本週五（6日）將加映中文配音版本，以及影迷不停敲碗的「IMAX」版。', 
    '台北市長柯文哲拋出結婚補助政策，引發熱議。民進黨北市議員王閔生今質疑，結婚補助真能解決少子化？補助結婚政策恐倒果為因？是否成效不佳，還要推「進洞房補助」？柯文哲回應，之所以提出結婚補助政策，是因台北市有高達35%的人不結婚，所以解決少子化，結婚是先決條件。',    
    '科比布萊恩共取得5座NBA總冠軍、2次總決賽最有價值球員、1次年度最有價值球員、15次入選NBA最佳陣容、18次入選全明星賽，科比位居聯盟生涯例行賽得分第四名以及生涯季后賽得分第四名。他共入選18次全明星賽是有史以來第二多，同時也創下連續先發場數的記錄。2000年代中期，科比為自己的綽號取為「黑曼巴」（BLACK MAMBA）。2008年和2012年夏季奧運會，科比以美國國家隊成員身份獲得兩枚金牌。2018年，科比編劇及旁白配音的動畫短片《親愛的籃球》獲得奧斯卡最佳動畫短片獎。',
    '最新一集的《玩命關頭》（Fast & Furious）目前演到第8集，《玩命關頭9》原訂今年5月上映，受到新冠肺炎以及《007：生死交戰》大片檔期強碰的影響，確定延至2021年4月2日與觀眾們見面，其中最大的看點就是原本領便當的「韓哥」姜成鎬回歸，讓粉絲感到興奮，而《玩命關頭10》規劃保密到家，據傳回著墨在主角群本身，為《玩命關頭11》大結局作為暖身。'
]
question = '奧斯卡最佳動畫短片獎的作者的綽號是什麼'

data = {"token":"Deep Learning 101", "context_ls":context_ls, "question":question}

out = call_api(data)
print(out)
pass
