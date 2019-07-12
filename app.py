from flask import Flask, request
from decouple import config
import pprint
import requests
app = Flask(__name__)
API_TOKEN = config('API_TOKEN') # 상수는 대문자
# CHAT_ID = config('CHAT_ID') 삭제


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/greeting/<name>') # https://7611d355.ngrok.io/greeting/승원
def greeting(name):
    return f'Hello, {name}'


@app.route(f'/{API_TOKEN}', methods=['POST'])
def telegram():
    from_telegram = request.get_json() # 실수: jason으로 문법 error
    pprint.pprint(from_telegram)
    if from_telegram.get('message') is not None: # is not None
        # 알고리즘
        chat_id = from_telegram.get('message').get('chat').get('id')
        text = from_telegram.get('message').get('text') # 사용자가 보낸 텍스트

        if text == '점심메뉴':
            text = '짜장면 먹어'
                    # text -> '원하는거' -> url에 넣고 -> response

        # send massage API URL
        base_url = 'https://api.telegram.org'
        api_url = f'{base_url}/bot{API_TOKEN}/sendMessage?chat_id={chat_id}&text={text}'
        response = requests.get(api_url)
        
        '''
        print(response)
        print('chat_id:', chat_id)
        print('text', text)
        '''

    return '', 200 # 아무것도 하지 않을 거라도 입력해줘야 한다. status code = 200


if __name__ == '__main__':
    app.run(debug=True)


