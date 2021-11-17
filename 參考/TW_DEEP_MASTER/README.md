# TW Deep Master API 

### **SpeechRecognition（語音識別）**
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"token":www.interactionx.co, "model_type":model_type(str), "input_wav":input_wav(list)}' \
 'https://API.TWMAN.ORG/SpeechRecognition'
```
* token（str）：www.interactionx.co
* model_type（str）："**asr_alpha**"、"**asr_beta**"、"**asr_omega**"
* input_wav（list）：測試音檔格式需為 16kHz、1 channel 的 wav，讀取方式參照 **request_test_SpeechRecognition.py**
* response 為 json 格式。
<br>

### **SpeakerRecognition（語者識別）**
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"token":www.interactionx.co, "model_type":model_type(str), \
 "enroll_list":enroll_list(dict), "test_wav":test_wav(list)}' \
 'https://API.TWMAN.ORG/SpeakerRecognition'
```
* token（str）：www.interactionx.co
* model_type（str）："**sincnet_plda**"
* enroll_list（dict）：格式為 {[說話人名稱]_[編號]: 音檔}，需至少包含兩個說話者並各自含五個音檔以上，音檔格式需為 16kHz、1 channel 的 wav **(讀取方法同 SpeechRecognition)**。
* test_wav（list）：測試音檔格式需為 16kHz、1 channel 的 wav **(讀取方法同 SpeechRecognition)**。
* response 為 json 格式。
* 參照 **request_test_SpeakerRecognition.py**。
<br>

### **AudioDenoise（語音去噪）**
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"token":www.interactionx.co, "model_type":model_type(str), "input_wav":input_wav(list)}' \
 'https://API.TWMAN.ORG/AudioDenoise'
```
* token（str）：www.interactionx.co
* model_type（str）："**Conv-denoiser**"、"**Fair-denoiser**"
* input_wav（str）：輸入音檔格式需為 16kHz、1 channel 的 wav **(讀取方法同 SpeechRecognition)**。
* response 為 json 格式，回傳的去噪後聲音需使用以下方法存出：
```
# In Python
from scipy.io import wavfile
import numpy as np

api_output = response.json().get('output')
wavfile.write(路徑＋檔名, 16000, np.array(api_output).astype(np.int16))
```
* 詳情可參照 **request_test_AudioDenoise.py**。
<br>

### **SpeechSeparation（語音分離）**
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"token":www.interactionx.co, "model_type":model_type(str), "input_wav":input_wav(list)}' \
 'https://API.TWMAN.ORG/SpeechSeparation'
```
* token（str）：www.interactionx.co
* model_type（str）："**dptnet**"、"**sudormrf**"
* input_wav（str）：輸入音檔格式需為 16kHz、1 channel 的 wav **(讀取方法同 SpeechRecognition)**。
* response 為 json 格式，回傳的去噪後聲音需使用以下方法存出：
```
# In Python
from scipy.io import wavfile
import numpy as np

sep1, sep2 = response.json().get('output')
wavfile.write(路徑＋檔名1, 16000, np.array(sep1).astype(np.int16))
wavfile.write(路徑＋檔名2, 16000, np.array(sep2).astype(np.int16))
```
* 詳情可參照 **request_test_SpeechSeparation.py**。
<br>

## **NLP**
<br>

### **QuestionAnswering（閱讀理解）**
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"token":www.interactionx.co, "model_type":model_type(str), "context":context(str), "question":question(str)}' \
 'https://API.TWMAN.ORG/QuestionAnswering'
```
* token（str）：www.interactionx.co
* model_type（str）："**bert_base_drcd**"
* context（str）：輸入的文章，需包含問題的答案才可正確作答。
* question（str）：輸入的問題，針對輸入文章內容的提問。
* 文章與問題的長度總和需小於 512。
* response 為 json 格式。
* 詳情可參照 **request_test_QuestionAnswering.py**。
<br>

### **QuestionAnsweringPlus（多文章閱讀理解）**
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"token":www.interactionx.co, "context_ls":[context1(str), context2(str), ...], "question":question(str)}' \
 'https://API.TWMAN.ORG/QuestionAnsweringPlus'
```
* token（str）：www.interactionx.co
* context_ls（str）：輸入的文章列表，其中一篇文章需包含問題的答案才可正確作答。
* question（str）：輸入的問題，針對輸入文章內容的提問。
* 任一文章與問題的長度總和需小於 512，若超過長度文章會被截斷。
* response 為 json 格式。
* 詳情可參照 **request_test_QuestionAnsweringPlus.py**。
<br>

### **NamedEntityRecognition（命名實體識別）**
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"token":www.interactionx.co, "model_type":model_type(str), "input_text":input_text(str)}' \
 'https://API.TWMAN.ORG/NamedEntityRecognition'
```
* token（str）：www.interactionx.co
* model_type（str）："**bert_base_msra**"
* input_text（str）：要預測是否包含實體的語句，長度須小於 512。
* response 為 json 格式。
* 詳情可參照 **request_test_NamedEntityRecognition.py**。
<br>

### **TextClassification（文本分類）**
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"token":www.interactionx.co, "model_type":model_type(str), "input_text":input_text(str)}' \
 'https://API.TWMAN.ORG/TextClassification'
```
* token（str）：www.interactionx.co
* model_type（str）："**bert_lstm_service**"
* input_text（str）：要預測類別的語句，長度須小於 64。
* 類別包含："商業洽談", "課程銷售", "債務告警", "房產銷售", "快遞通知", "金融推銷", "獵人頭", "保險推銷", "貸款銷售", "外賣通知", "聊天", "電信客服"
* response 為 json 格式。
* 詳情可參照 **request_test_TextClassification.py**。
<br>

### **TextSimilarity（文本相似度）**
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"token":www.interactionx.co, "model_type":model_type(str), "input_text_1":input_text_1(str), \
 "input_text_2":input_text_2(str)}' \
 'https://API.TWMAN.ORG/TextSimilarity'
```
* token（str）：www.interactionx.co
* model_type（str）："**albert**"
* input_text_1（str）：語句1，模型會計算此句與 input_text_2 的相似度。
* input_text_2（str）：語句2，模型會計算此句與 input_text_1 的相似度。
* 輸入 text1 與 text2 長度相加須小於 512。
* response 為 json 格式。
* 詳情可參照 **request_test_TextSimilarity.py**。
<br>

### **TextCorrection（文本糾錯）**
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{"token":www.interactionx.co, "model_type":model_type(str), "input_text":input_text(str)}' \
 'https://API.TWMAN.ORG/TextCorrection'
```
* token（str）：www.interactionx.co
* model_type（str）："**bert**"
* input_text（str）：要執行糾錯的語句，長度須小於 64。
* response 為 json 格式。
* 詳情可參照 **request_test_TextCorrection.py**。
<br>
