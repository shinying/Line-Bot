from flask import Flask, request, abort, url_for

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from cv import *
from myself import *

import os

app = Flask(__name__)

line_bot_api = LineBotApi('pDq55Cpri+YlG3ADO7C++ufKY0ouqcXNOATku0+0RwIMYvrnOfZPaMfjznfHyGGzbfn53zny2NEOQLWdxDnsaX3yHSDjkFv9gPmX1hD6a+5tVTjOMdwlBk5rScGo1zl5vsN24KgPscitpHF4X4rXywdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('13a1e740fbc927e2955de31fc7552fbd')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if '常見問題' in text:
        message = get_basic_ques()
    elif '自我介紹' in text:
        message = TextSendMessage(text="我從資訊技術出發，遊走於心理、設計與管理之間，致⼒於將以⼈為本的設計原則注入科技領域，並應⽤科技解決問題。")
    elif '錄取' in text:
        message = TextSendMessage(text="好的工程師除了要有紮實的技術硬底子，也需要有良好的團隊合作能力。在資：管 = 7:3系上課程和課堂外project的訓練下必備的能力我不會少，而我還有很多社團和校外組織的跨領域合作經驗，在溝通和表達上更具優勢。")
    elif '申請' in text:
        message = TextSendMessage(text="Line不但是台灣市佔率最高的通訊軟體，也是積極開拓新服務和跨國網路和軟體公司，我很想試試和國際級的人才並肩工作的感覺！")
    elif '生活' in text:
        message = TextSendMessage(text="你可以問問我喜歡的歌手、運動、動物，或參加過的社團")
    elif ('喜歡' in text or '喜愛' in text):
        if '歌手' in text:
            message = get_favor('singer')
        elif '動物' in text:
            message = get_favor('animal')
        elif '運動' in text:
            message = get_favor('sport')
        else:
            message = TextSendMessage(text="其他喜歡的東西還沒有加入喔～")
    elif '社團':
        message = get_clubs()
    elif '技能' in text:
        message = get_skills()
    elif '專題' in text:
        message = get_projects()
    elif '比賽' in text:
        message = get_contests()
    else:
        message = TemplateSendMessage(
            alt_text='unknown',
            template=ButtonsTemplate(
                # thumbnail_image_url='',
                title='抱歉我沒有聽懂',
                text='不過也許我們可以聊聊',
                actions=[
                    MessageTemplateAction(
                        label='常見問題',
                        text='常見問題'
                    ),
                    MessageTemplateAction(
                        label='專題',
                        text='專題'
                    ),
                    MessageTemplateAction(
                        label='比賽',
                        text='比賽'
                    ),
                    MessageTemplateAction(
                        label='技能',
                        text='技能'
                    ),
                    MessageTemplateAction(
                        label='生活小事',
                        text='生活小事'
                    ),
                ]
            )
        )

    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
