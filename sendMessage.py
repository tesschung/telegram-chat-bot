import requests # 요청하기 위한 모듈
import pprint   # 분석을 용이하게 함
import decouple
from decouple import config # decouple.config # decouple에 담긴 config 함수만 호출
import pprint

base_url = 'https://api.telegram.org'
token = config('API_TOKEN')
chat_id = config('CHAT_ID')
text = '안녕하세요'

api_url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

response = requests.get(api_url).json()
# print(response)

pprint.pprint(response)

# 요청이 이렇게 보내지므로
# 사용자의 인풋에 따라-> text
# 요청을 보낼 수 있도록
# 개발