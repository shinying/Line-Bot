from flask import Flask, request, abort, url_for

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from cv import *
from myself import *

import os
import random
import re

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


def pick(n):
    topics = ['常見問題', '興趣', '參加過的社團', '技能', '專題', '參加過的比賽', '修過什麼課']
    return random.choices(topics, k=n)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if re.match('[哈呵嘿嘻]', text) or re.match('XD+', text):
        message = TextSendMessage(text="\U00100079")
    if re.match('.*常見問題', text):
        message = get_basic_ques()
    elif re.match('.*自我介紹', text):
        message = TextSendMessage(text="我從資訊技術出發，遊走於心理、設計與管理之間，致⼒於將以⼈為本的設計原則注入科技領域，並應⽤科技解決問題。\U0010008F")
    elif re.match('.*為什麼.*錄取', text):
        message = TextSendMessage(text="好的工程師除了要有紮實的技術硬底子，也需要有良好的團隊合作能力。在資：管 = 7:3系上課程和課堂外project的訓練下必備的能力我不會少，而我還有很多社團和校外組織的跨領域合作經驗，在溝通和表達上更具優勢。\U00100033")
    elif re.match('.*為什麼.*申請', text):
        message = TextSendMessage(text="Line不但是台灣市佔率最高的通訊軟體，也是積極開拓新服務和跨國網路和軟體公司，我很想試試和國際級的人才並肩工作的感覺！\U001000A5")
    elif re.match('.*興趣', text):
        message = TextSendMessage(text="唱歌吧，你還可以問問我喜歡的歌手、運動、動物，或參加過的社團")
    elif re.match('[^不無]*[最喜歡愛]', text):
        if re.match('.*歌手', text):
            message = get_favor('singer')
        elif re.match('.*動物', text):
            message = get_favor('animal')
        elif re.match('.*運動', text):
            message = get_favor('sport')
        else:
            message = TextSendMessage(text="其他喜歡的東西還沒有加入喔～\U00100065")
    elif re.match('.*社團', text):
        message = get_clubs()
    elif re.match('.*技能', text):
        message = get_skills()
    elif re.match('.*專題', text):
        message = get_projects()
    elif re.match('.*比賽', text):
        message = get_contests()
    elif re.match('.*修.*課', text):
        message = TextSendMessage(text="系上的課程規劃是資:管 7:3，除了資工基本的線代、資結、演算法等，也有管理相關的統計、會計。另外我也選修了其他如區塊鏈、語音處理、機器學習等課程。")
    elif re.match('.*開.*話題', text):
        topics = pick(1)
        message = TemplateSendMessage(
            alt_text='unknown',
            template=ButtonsTemplate(
                title='開個話題',
                text='也許我們可以來聊聊',
                actions=[
                    MessageTemplateAction(
                        label=topics[0],
                        text=topics[0]
                    )
                ]
            )
        )
    else:
        topics = pick(3)
        message = TemplateSendMessage(
            alt_text='unknown',
            template=ButtonsTemplate(
                title='抱歉我沒有聽懂\U00100010',
                text='不過也許我們可以聊聊',
                actions=[
                    MessageTemplateAction(
                        label=topics[0],
                        text=topics[0]
                    ),
                    MessageTemplateAction(
                        label=topics[1],
                        text=topics[1]
                    ),
                    MessageTemplateAction(
                        label=topics[2],
                        text=topics[2]
                    ),
                ]
            )
        )

    line_bot_api.reply_message(event.reply_token, message)


@handler.add(FollowEvent)
def handle_follow(event):
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text='不知道聊什麼的時候，試試「開個話題」吧\U0010008A'))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
