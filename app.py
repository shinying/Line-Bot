from flask import Flask, request, abort, url_for

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from cv import *
from utils import *
from detector import Detector

import os
import random
import re

app = Flask(__name__)

line_bot_api = LineBotApi('pDq55Cpri+YlG3ADO7C++ufKY0ouqcXNOATku0+0RwIMYvrnOfZPaMfjznfHyGGzbfn53zny2NEOQLWdxDnsaX3yHSDjkFv9gPmX1hD6a+5tVTjOMdwlBk5rScGo1zl5vsN24KgPscitpHF4X4rXywdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('13a1e740fbc927e2955de31fc7552fbd')

detector = Detector(128, 'word2vec.wv', 'model.h5')
detect_mode = False

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
    global detect_mode
    text = event.message.text
    if not detect_mode:
        if re.match('[.*你好.*]', text) or re.match('[嗨]', text) or re.match('哈囉', text):
            msg = get_greet()
        elif re.match('[哈呵嘿嘻]', text) or re.match('.*XD+', text):
            msg = TextSendMessage(text="傻眼\U00100079")
        elif re.match('[^不]回答', text) or re.match('[^不]做', text) or re.match('.*能力*', text):
            msg = get_ques('我會很多事喔！')
        elif re.match('.*常見問題', text):
            msg = get_basic_ques()
        elif re.match('.*自我介紹', text):
            msg = TextSendMessage(text="我深耕資訊技術，也漫遊於心理、設計與管理之間，致⼒於將以⼈為本的設計原則注入科技領域，並應⽤科技解決問題。\U0010008F")
        elif re.match('.*為什麼.*錄取', text):
            msg = TextSendMessage(text="好的工程師除了要有紮實的技術硬底子，也需要有良好的團隊合作能力。在資：管 = 7:3系上課程和課堂外project的訓練下必備的能力我不會少，而我還有很多社團和校外組織的跨領域合作經驗，在溝通和表達上更具優勢。\U00100033")
        elif re.match('.*為什麼.*申請', text):
            msg = TextSendMessage(text="Line不但是台灣市佔率最高的通訊軟體，也是積極開拓新服務和跨國網路和軟體公司，我很想試試和國際級的人才並肩工作的感覺！\U001000A5")
        elif re.match('.*興趣', text):
            msg = TextSendMessage(text="唱歌吧，你還可以問問我喜歡的歌手、運動、動物，或參加過的社團")
        elif re.match('[^不無]*[最喜歡愛]', text):
            if re.match('.*歌手', text):
                msg = get_favor('singer')
            elif re.match('.*動物', text):
                msg = get_favor('animal')
            elif re.match('.*運動', text):
                msg = get_favor('sport')
            else:
                msg = TextSendMessage(text="其他喜歡的東西還沒有加入喔～\U00100065")
        elif re.match('.*社團', text):
            msg = get_clubs()
        elif re.match('.*技能', text):
            msg = get_skills()
        elif re.match('.*專題', text):
            msg = get_projects()
        elif re.match('.*比賽', text):
            msg = get_contests()
        elif re.match('.*修.*課', text):
            msg = TextSendMessage(text="系上的課程規劃是資:管 7:3，除了資工基本的線代、資結、演算法等，也有管理相關的統計、會計。另外我也選修了其他如區塊鏈、語音處理、機器學習等課程。")
        elif re.match('呼叫阿水伯', text):
            msg = TextSendMessage(text="呵呵呵～阿水伯來了！我上知天文下知地理喔～不想問的時候只要說一句「問完了」，我就會叫阿信回來和你聊天啦")
            detect_mode = True
        elif re.match('.*開.*話題', text):
            topics = pick(1)
            msg = TemplateSendMessage(
                alt_text='pick',
                template=ButtonsTemplate(
                    title='開個話題',
                    text='也許我們可以來聊聊',
                    actions=[
                        MessageTemplateAction(
                            label=topics[0],
                            text=topics[0]
                        ),
                        MessageTemplateAction(
                            label='聊過了？再來一個',
                            text='開個話題'
                        )
                    ]
                )
            )
        else:
            msg = get_ques('抱歉我沒有聽懂...')
    else:
        if not re.match('問完了', text):
            msg = TextSendMessage(text=detector.predict(text))
        else:
            msg = TextSendMessage(text="阿信回來了！我們繼續聊天吧")
            detect_mode = False

    line_bot_api.reply_message(event.reply_token, msg)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
