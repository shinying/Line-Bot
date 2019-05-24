from linebot.models import *
import random


def pick(n):
    topics = ['常見問題', '興趣', '參加過的社團', '技能', '專題', '參加過的比賽', '修過什麼課']
    return random.sample(topics, k=n)


def get_greet():
    msg = TemplateSendMessage(
        alt_text='greet',
        template=ButtonsTemplate(
            title='嗨嗨你好啊',
            text='我是阿信，就讀於資管系三年級，很高興認識你\U00100079。你可以試著...',
            actions=[
                MessageTemplateAction(
                    label='查看所有問題',
                    text='你可以回答什麼？'
                ),
                MessageTemplateAction(
                    label='開個話題',
                    text='開個話題'
                ),
            ]
        )
    )
    return msg


def get_basic_ques():
    msg = TemplateSendMessage(
        alt_text='basic',
        template=ButtonsTemplate(
            title='常見問題',
            text='以下是一些面試常見的問題',
            actions=[
                MessageTemplateAction(
                    label='簡單自我介紹',
                    text='簡單自我介紹'
                ),
                MessageTemplateAction(
                    label='為什麼要錄取你',
                    text='為什麼要錄取你？'
                ),
                MessageTemplateAction(
                    label='為什麼想申請',
                    text='為什麼想申請 LINE TECH FRESH？'
                ),
            ]
        )
    )
    return msg


def get_favor(kind):
    if kind == 'singer':
        msg = TemplateSendMessage(
            alt_text='男歌手',
            template=ButtonsTemplate(
                thumbnail_image_url="https://i.imgur.com/RwJ9oIW.jpg",
                title='小宇',
                text='總是端出台灣少見的奇幻風格與前衛曲風，是全方位的音樂人',
                actions=[
                    URITemplateAction(
                        label='Youtube Channel',
                        uri='https://www.youtube.com/channel/UC8C3GSHSFQltb9RjbCGgmPA'
                    )
                ]
            )
        )
    elif kind == 'animal':
        msg = TextSendMessage(text="水獺！\U0010008D")
    elif kind == 'sport':
        msg = TextSendMessage(text="應該是排球，不過最近也有在重訓～")
    return msg


def get_ques(title):
    topics = pick(3)
    msg = TemplateSendMessage(
        alt_text='topics',
        template=ButtonsTemplate(
            title=title,
            text='也許我們可以聊聊',
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
    return msg