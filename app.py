from flask import Flask, request, abort, url_for

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASS_DIR = os.path.join(BASE_DIR, 'assets')

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
    if '男' in text and '歌手' in text:
        message = TemplateSendMessage(
            alt_text='男歌手',
            template=ButtonsTemplate(
                thumbnail_image_url=url_for('assets', filename='m_singer.jpg'),
                title='小宇',
                text='台灣少見的奇幻風格與前衛曲風，是全方位的音樂人',
                actions=[
                    PostbackTemplateAction(
                        label='postback',
                        text='postback text',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message',
                        text='message text'
                    ),
                    URITemplateAction(
                        label='Youtube Channel',
                        uri='https://www.youtube.com/channel/UC8C3GSHSFQltb9RjbCGgmPA'
                    )
                ]
            )
        )
    else:
        message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
