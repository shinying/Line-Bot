from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

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


@handler.add(MessageEvent, message=TextMessage(text='你好'))
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
