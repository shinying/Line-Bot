from linebot.models import *


def get_skills():
    message = TextSendMessage(text="最熟悉的語言是 Python 和 C++，其他如資料分析、機器學習、區塊鏈等等熱門關鍵字都了解一點。")
    return message

def get_projects():
    message = TemplateSendMessage(
        alt_text='projects',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='Dance Light',
                    text='幫助聽障舞者感受音樂的燈光裝置',
                    actions=[
                        URITemplateAction(
                            label='watch video',
                            uri='https://www.youtube.com/watch?v=Yx0Welpq9NY'
                        ),
                        URITemplateAction(
                            label='read document',
                            uri='https://drive.google.com/open?id=110YDLC42UPF5E4cwvmgw3WnwZKq_24PJ'
                        )
                    ]
                ),
                CarouselColumn(
                    title='高雄港智慧拖船調度演算法',
                    text='應用最佳化方法和訓練拖船工作時間預測模型來自動化高雄港的拖船調度，並開發模擬系統，以港區會發生的真實事件評估效能（保密協定限制無法提供原始碼）',
                    actions=[
                        URITemplateAction(
                            label='read README.md',
                            uri='https://hackmd.io/ptgih1aEQAWAAWQtoMrrug?view'
                        )
                    ]
                ),
                CarouselColumn(
                    title='NodEverywhere',
                    text='以 Unity 建構場景實驗，測試使⽤者以視線停留、頭的指向停留和點頭三種方式選擇物件之速度和準確率。',
                    actions=[
                        URITemplateAction(
                            label='read paper',
                            uri='https://drive.google.com/open?id=1lqL_Yfh9MgvPunjNDeRqS8M25sZeHcF2'
                        )
                    ]
                )
            ]
        )
    )
    return message


def get_contests():
    message = TemplateSendMessage(
        alt_text='contests',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/FOGaRWQ.png',
                    title='Addon',
                    text='2018臺大、師大、臺科大三校 App 創意競賽冠軍。以手機端和網頁打造無紙化的 brainstorming 體驗',
                    actions=[
                        URITemplateAction(
                            label='watch video',
                            uri='https://www.youtube.com/watch?v=IdpYBQ3P_fU&t=14s'
                        ),
                        URITemplateAction(
                            label='visit Github',
                            uri='https://github.com/shinying/Addon'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/S0vtWir.png',
                    title='ChainSurance',
                    text='第二屆上海銀行滬港台金融科技創新校園競賽第四名。為小型商家、個人勞動者創造全新商業模式。',
                    actions=[
                        URITemplateAction(
                            label='read slides',
                            uri='https://drive.google.com/file/d/1CG7wkHzd3X6hhQoxYbBwdnXbccAOee_z/view'
                        ),
                    ]
                )
            ]
        )
    )
    return message

def get_clubs():
    message = TemplateSendMessage(
        alt_text='club',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/YBw7dzA.jpg',
            title='不一樣思考社',
            text='我大一二在不一樣思考社擔任課程長，致力於推廣和應用設計思考。另外也參加過阿卡貝拉社、NTU Maker等社團',
            actions=[
                URITemplateAction(
                    label='Facebook',
                    uri='https://www.facebook.com/NTUd.thinking/'
                ),
            ]
        )
    )
    return message