from flask import Flask, request
from decouple import config
import pprint
import requests
app = Flask(__name__)
API_TOKEN = config('API_TOKEN') # 상수는 대문자
# CHAT_ID = config('CHAT_ID') 삭제

NAVER_CLIENT_ID = config('NAVER_CLIENT_ID')
NAVER_CLIENT_PASSWORD = config('NAVER_CLIENT_PASSWORD')

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
        '''
        if text == '점심메뉴':
            text = '짜장면 먹어'
                    # text -> '원하는거' -> url에 넣고 -> response
        '''

        #첫 네글자가 '/번역 '일 때
        if text[0:4] == '/한영 ':
            headers = {
                'X-Naver-Client-Id': NAVER_CLIENT_ID,
                'X-Naver-Client-Secret': NAVER_CLIENT_PASSWORD
            }
            data = {
                'source': 'ko',
                'target': 'en',
                'text': text[4:] # '/번역 ' 이후의 문자열만 대상으로 번역
            }
            papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
            papago_response = requests.post(papago_url, headers=headers, data=data).json()
            print(papago_response)
            # pprint.pprint(papago_response.json())
            translatedText = papago_response.get('message').get('result').get('translatedText')


        if text[0:4] == '/영한 ':
            headers = {
                'X-Naver-Client-Id': NAVER_CLIENT_ID,
                'X-Naver-Client-Secret': NAVER_CLIENT_PASSWORD
            }
            data = {
                'source': 'en',
                'target': 'ko',
                'text': text[4:] # '/번역 ' 이후의 문자열만 대상으로 번역
            }
            papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
            papago_response = requests.post(papago_url, headers=headers, data=data).json()
            print(papago_response)
            # pprint.pprint(papago_response.json())
            translatedText = papago_response.get('message').get('result').get('translatedText')

        # send massage API URL
        base_url = 'https://api.telegram.org'
        api_url = f'{base_url}/bot{API_TOKEN}/sendMessage?chat_id={chat_id}&text={translatedText}'
        response = requests.get(api_url)
        '''
        print(response)
        print('chat_id:', chat_id)
        print('text', text)
        '''

    return '', 200 # 아무것도 하지 않을 거라도 입력해줘야 한다. status code = 200


if __name__ == '__main__':
    app.run(debug=True)


