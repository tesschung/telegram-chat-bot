[TOC]



## 챗봇/telegram API활용

https://telegram.org/



BotFather을 통해 메신저를 만들 수 있음



/newbot

![1562895140333](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562895140333.png)



801216085:AAH8Uj0wEeNh-wXZZIYu40NOJoPuXSrgF-M

https://core.telegram.org/bots/api

![1562895364190](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562895364190.png)



https://api.telegram.org/bot<token>/METHOD_NAME





base_url:

https://api.telegram.org/bot801216085:AAH8Uj0wEeNh-wXZZIYu40NOJoPuXSrgF-M/

getMe

#### getMe: 기본 정보확인 METHOD

A simple method for testing your bot's auth token. Requires no parameters. Returns basic information about the bot in form of a [User](https://core.telegram.org/bots/api#user) object.

![1562895563135](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562895563135.png)

viainstancttess_bot

![1562895680216](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562895680216.png)





https://api.telegram.org/bot801216085:AAH8Uj0wEeNh-wXZZIYu40NOJoPuXSrgF-M/getUpdates

#### getUpdates: 받은 모든 메세지를 확인 할 수 있는 METHOD

Use this method to receive incoming updates using long polling ([wiki](http://en.wikipedia.org/wiki/Push_technology#Long_polling)). An Array of [Update](https://core.telegram.org/bots/api#update) objects is returned.

| Parameter       | Type            | Required | Description                                                  |
| :-------------- | :-------------- | :------- | :----------------------------------------------------------- |
| offset          | Integer         | Optional | Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as [getUpdates](https://core.telegram.org/bots/api#getupdates) is called with an *offset* higher than its *update_id*. The negative offset can be specified to retrieve updates starting from *-offset* update from the end of the updates queue. All previous updates will forgotten. |
| limit           | Integer         | Optional | Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100. |
| timeout         | Integer         | Optional | Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only. |
| allowed_updates | Array of String | Optional | List the types of updates you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See [Update](https://core.telegram.org/bots/api#update) for a complete list of available update types. Specify an empty list to receive all updates regardless of type (default). If not specified, the previous setting will be used.  Please note that this parameter doesn't affect updates created before the call to the getUpdates, so unwanted updates may be received for a short period of time. |

![1562896142510](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562896142510.png)

id: **823252179**

누군가 봇에 말을 걸면 그 사람의 메세지인 '**text**'와 유저 고유 식별자인 '**id**' 값 확인 가능





#### sendMessage

Use this method to send text messages. On success, the sent [Message](https://core.telegram.org/bots/api#message) is returned.

**Requird**의 **Yes**는 반드시 포함이 되어야 한다.

| Parameter                | Type                                                         | Required | Description                                                  |
| :----------------------- | :----------------------------------------------------------- | :------- | :----------------------------------------------------------- |
| **chat_id**              | Integer or String                                            | **Yes**  | Unique identifier for the target chat or username of the target channel (in the format `@channelusername`) |
| **text**                 | String                                                       | **Yes**  | Text of the message to be sent                               |
| parse_mode               | String                                                       | Optional | Send [*Markdown*](https://core.telegram.org/bots/api#markdown-style) or [*HTML*](https://core.telegram.org/bots/api#html-style), if you want Telegram apps to show [bold, italic, fixed-width text or inline URLs](https://core.telegram.org/bots/api#formatting-options) in your bot's message. |
| disable_web_page_preview | Boolean                                                      | Optional | Disables link previews for links in this message             |
| disable_notification     | Boolean                                                      | Optional | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |
| reply_to_message_id      | Integer                                                      | Optional | If the message is a reply, ID of the original message        |
| reply_markup             | [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) or [ReplyKeyboardMarkup](https://core.telegram.org/bots/api#replykeyboardmarkup) or [ReplyKeyboardRemove](https://core.telegram.org/bots/api#replykeyboardremove) or [ForceReply](https://core.telegram.org/bots/api#forcereply) | Optional | Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating), [custom reply keyboard](https://core.telegram.org/bots#keyboards), instructions to remove reply keyboard or to force a reply from the user. |

url로 명령 보내기 가능



https://api.telegram.org/bot801216085:AAH8Uj0wEeNh-wXZZIYu40NOJoPuXSrgF-M/sendMessage?chat_id=823252179&text=그래안녕하다



/sendMessage? *API*

chat_id=823252179 *보낼 사용자 id*

&text=그래안녕하다 *원하는 text*

![1562897245572](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562897245572.png)

requests.get 하여 json parsing하고 메세지 가져오는 것 가능

```python
import requests # 요청하기 위한 모듈

base_url = 'https://api.telegram.org'
token = '801216085:AAH8Uj0wEeNh-wXZZIYu40NOJoPuXSrgF-M'
chat_id = '823252179'
text = '안녕하세요'

# params = dict(chat_id = chat_id,

api_url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

response = requests.get(api_url).json()
print(response)
```

![1562898126249](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562898126249.png)

json으로 parsing한 정보 분석 가능

![1562898174367](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562898174367.png)

```python
pprint.pprint(response)
```

![1562898430267](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562898430267.png)



.env 파일 생성

.env=environment
환경변수에 저장해서 .py로 참조하여 사용함으로써 개인정보를 보호할 것

설치방법:

$ pip install python-decouple

**중요**

메세지를 받을때마다 우리가 만든 서버에 알림

hi라는 메세지를 받았습니다 라는 식으로 지정한 서버에서 알림 받음



flask 서버를 만들고, chatbot한테 이야기

CHAT_ID를 분석하여 사용자에게 전달한다.

![1562904498550](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562904498550.png)

봇에게 메세지를 보낸 것을 전송해야할 서버를 지정

앞으로 봇이 받는 메세지를 특정 url/서버에 보내라는 **setWebhook method** 사용

#### setWebhook

Use this method to specify a url and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, **we will send an HTTPS POST request to the specified url, containing a JSON-serialized [Update](https://core.telegram.org/bots/api#update).** In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns *True* on success.

If you'd like to make sure that the Webhook request comes from Telegram, we recommend using a secret path in the URL, e.g. **`https://www.example.com/<token>**`. Since nobody else knows your bot‘s token, you can be pretty sure it’s us.

| Parameter       | Type                                                      | Required | Description                                                  |
| :-------------- | :-------------------------------------------------------- | :------- | :----------------------------------------------------------- |
| **url**         | String                                                    | **Yes**  | HTTPS url to send updates to. Use an empty string to remove webhook integration |
| certificate     | [InputFile](https://core.telegram.org/bots/api#inputfile) | Optional | Upload your public key certificate so that the root certificate in use can be checked. See our [self-signed guide](https://core.telegram.org/bots/self-signed) for details. |
| max_connections | Integer                                                   | Optional | Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to *40*. Use lower values to limit the load on your bot‘s server, and higher values to increase your bot’s throughput. |
| allowed_updates | Array of String                                           | Optional | List the types of updates you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See [Update](https://core.telegram.org/bots/api#update) for a complete list of available update types. Specify an empty list to receive all updates regardless of type (default). If not specified, the previous setting will be used.  Please note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time. |

`https://www.example.com/<token>` 을 사용하여 설정



로컬호스트를 외부화함 -> **로컬이 열렸을때만 , 이제 로컬호스트가 아니라 어디에서나 접속가능**

*해당 engrok.exe를 프로젝트 파일에 복사하여 옮긴다.*

https://ngrok.com/

1. ngrok에 회원정보 등록

```bash
./ngrok authtoken 6fvskqMGvc4mVtcRNzmoW_7xAFunFeLuppQKN7guKXa
```



2. terminal

   ```bash
   ./ngrok.exe http 5000
   ```

   ![1562905640764](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562905640764.png)

https://api.telegram.org/bot<token>?url=<myngrokurl>/<token>

**실수 method 두번 작성했음**

https://api.telegram.org/bot801216085:AAH8Uj0wEeNh-wXZZIYu40NOJoPuXSrgF-M/setWebhook?url=https://7611d355.ngrok.io/801216085:AAH8Uj0wEeNh-wXZZIYu40NOJoPuXSrgF-M



![1562906928943](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562906928943.png)









모든메세지가 text인 것은 아니다 

왜냐하면 사진일 수도 있고, 수정 할 수도 있기 때문

그래서 메세지가 있을때만 등록하도록 작성



1. 여러 사용자의 id를 받아 해당하는 그 id의 사람에게 메세지를 보내도록함
2. chat_id의 변수를 가져온다



https://developers.naver.com/products/nmt)

### Neural Machine Translation 사용

http://developers.naver.com/

https://developers.naver.com/products/nmt/

NMT는 Neural Machine Translation(인공신경망 기반 기계번역)의 약어입니다. 파파고의 NMT 기술은 입력 문장을 문장벡터로 변환하는 신경망(encoder)과 문장벡터에서 번역하는 언어의 문장을 생성하는 신경망(decoder)를 대규모의 병렬 코퍼스부터 자동으로 학습합니다. 입력문장의 일부가 아니라 문장 전체 정보를 바탕으로 번역을 수행하기때문에 기존 SMT방식의 번역보다 더욱 정확하고 문장 맥락에 맞는 번역을 하는것이 특징입니다.

오픈 API신청

![1562912487992](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562912487992.png)

**Client ID**: b3yvBN42vjmV69bXznrU

**Client Secret**: G6IHqQZoxo



파파고 NMT API 가이드

[가이드](https://developers.naver.com/docs/nmt/reference/)에 따라, cURL을 이용해 동작을 확인해 보세요.

```
curl "https://openapi.naver.com/v1/papago/n2mt" \
-H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
-H "X-Naver-Client-Id: b3yvBN42vjmV69bXznrU" \
-H "X-Naver-Client-Secret: G6IHqQZoxo" \
-d "source=ko&target=en&text=만나서 반갑습니다." -v
```



### chat-bot 배포: 한 계정에 하나밖에 등록 못합니다!

[pythonanywhere](https://www.pythonanywhere.com/): 배포를 쉽게 해주는 사이트

![1562915849357](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562915849357.png)



Add a new web app 클릭하여 원하는 설정으로 Next

![1562916012441](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562916012441.png)

하여 코드 전체 복사

다른 모듈은 추가로 설치 해주어야 한다.

console로 들어가서 설치해야 한다.

![1562916628325](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562916628325.png)

.env 옮기고

![1562916858576](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562916858576.png)

original url 변경:

801216085:AAH8Uj0wEeNh-wXZZIYu40NOJoPuXSrgF-M/setWebhook?url=https://7611d355.ngrok.io/801216085:AAH8Uj0wEeNh-wXZZIYu40NOJoPuXSrgF-M

http://tesschung.pythonanywhere.com/

주소 얻어서 **https**여야한다.

https://api.telegram.org/bot801216085:AAH8Uj0wEeNh-wXZZIYu40NOJoPuXSrgF-M/setWebhook?url=https://tesschung.pythonanywhere.com/801216085:AAH8Uj0wEeNh-wXZZIYu40NOJoPuXSrgF-M



### http 메소드 요약

Reference: [https://medium.com/@mystar09070907/flask%EB%A1%9C-get-post-%EC%9A%94%EC%B2%AD-%EB%B3%B4%EB%82%B4%EA%B8%B0-1-57d8f4559793](https://medium.com/@mystar09070907/flask로-get-post-요청-보내기-1-57d8f4559793)

| **Sr.No** | **Methods & Description**                                    |
| --------- | ------------------------------------------------------------ |
| 1         | **GET**: 암호화되지 않은 form의 데이터를 서버로 전송합니다.가장 흔하게 사용되는 메소드입니다. |
| 2         | **HEAD**: response body를 제외하고 GET과 동일합니다.         |
| 3         | **POST**: HTML form 데이터를 서버로 전송합니다. POST 메소드로 전달받은 데이터는 서버에 cache되지 않습니다. |
| 4         | **PUT**: 현재 표현되고 있는 대상 resource를 업로드된 컨텐츠로 교체합니다. |
| 5         | **DELETE**: URL가 준 현재 표현되고 있는 대상 resource를 제거합니다. |

**post** request: 중요한 요청들은 post에 보내지게 된다.

request.post('변수')



**get** request

request.args.get('변수')