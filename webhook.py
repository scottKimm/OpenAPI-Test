from flask import Flask
from flask import request

import requests

app = Flask(__name__)

# slack webhook test
@app.route("/webhook", methods=['POST'])
def webhook():
    # 앞에 필요없는 부분 슬라이스 (슬랙쪽 설정에 맞춰서 한 것이기 때문에 실제 구현때는 적절히 바꿀필요있음)
    text = request.form.get("text")[7:]

    # swit webhook endpoint
    endpoint = "https://xxx.xxx/xxx"

    # plain text 만 가능
    json_data = {
        "text": text
    }

    headers_data = {
        'Content-type' : 'application/json'
    }
    res = requests.post(url=endpoint, json=json_data, headers=headers_data, timeout=180)

    if res.ok:
        # slack webhook 이용시 응답
        response_text = "success"

    response_text = "fail"

    return {
        "text": response_text
    }
