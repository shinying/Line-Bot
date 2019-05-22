from linebot.models import *


def get_basic_ques():
    message = TemplateSendMessage(
        alt_text='basic',
        template=ButtonsTemplate(
            # thumbnail_image_url='https://i.imgur.com/YBw7dzA.jpg',
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
    return message


def get_favor(kind):
    if kind == 'singer':
        message = TemplateSendMessage(
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
        message = TextSendMessage(text="水獺！0x10008D")
    elif kind == 'sport':
        message = TextSendMessage(text="應該是排球，不過最近也有在重訓～")
    return message