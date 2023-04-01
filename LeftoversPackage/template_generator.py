from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
# Import the message type of the line bot
from linebot.models import (
    ImagemapSendMessage, TextSendMessage,
    ImageSendMessage, LocationSendMessage,
    FlexSendMessage, VideoSendMessage,
    StickerSendMessage, AudioSendMessage,
    ImageMessage, VideoMessage,
    AudioMessage, TextMessage,
    TemplateSendMessage, QuickReply
)

# Import the action type of the line bot
from linebot.models import (
    MessageTemplateAction, PostbackAction,
    MessageAction, URIAction, QuickReplyButton
)
from linebot.models.template import (
    ButtonsTemplate, CarouselTemplate,
    ConfirmTemplate, ImageCarouselTemplate
)
from linebot.models.template import *
from linebot.models.events import (
    FollowEvent, MessageEvent
)
import os
import pandas as pd
from numpy import NaN
import math
from flask import Flask, request, abort, jsonify
import datetime
import json

def TestFunc() -> None:

    print('Hello template generator')


def text_message_generator(reply_text) :

    text_message = '{\"type\": \"text\", \"text\": \"' + reply_text + '\"}'

    return text_message

def buttons_template_generator_two(
    alt_text, title, title_info, 
    label1, label1_reply, 
    label2, label2_reply
    ) -> 'TemplateSendMessage':
    
    buttons_template_message = TemplateSendMessage(
        alt_text=alt_text,
        template=ButtonsTemplate(
            title=title,
            text=title_info,
            actions=[
                MessageTemplateAction(
                    label=label1,
                    text=label1_reply,
                ),
                MessageTemplateAction(
                    label=label2,
                    text=label2_reply,
                )
            ]
        )
    )

    return buttons_template_message


def quick_reply_generator(
        text, label, reply_content) -> 'TextSendMessage':

    quick_reply = TextSendMessage(
        text=text,
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label=label, 
                        text=reply_content,
                    )
                )
            ]
        )
    )

    return quick_reply

known_us_quick_reply = quick_reply_generator(
    text='請選擇要顯示的買賣超資訊',
    label='來認識我們吧', 
    reply_content='來認識「一食二鳥」吧！',
)

def buttons_template_generator_one(alt_text, 
    title, title_info, label1, label1_reply,
    ) -> 'TemplateSendMessage':
    
    buttons_template_message = TemplateSendMessage(
        alt_text=alt_text,
        template=ButtonsTemplate(
            title=title,
            text=title_info,
            actions=[
                MessageTemplateAction(
                    label=label1,
                    text=label1_reply,
                ),
            ]
        )
    )

    return buttons_template_message

def carousel_template_generator_one(
        alt_text, image_url, title, description, 
        label1, label1_info, label2, label2_info,
        label3, label3_info,
    ) -> 'TemplateSendMessage':
    
    carousel_template_message = TemplateSendMessage(
        alt_text=alt_text,
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=image_url,
                    image_aspect_ratio='square',
                    image_size='cover',
                    title=title,
                    text=description,
                    actions=[
                        MessageAction(
                            label=label1,
                            text=label1_info,
                        ),
                        MessageAction(
                            label=label2,
                            text=label2_info,
                        ),
                        MessageAction(
                            label=label3,
                            text=label3_info,
                        ),
                    ]
                ),
            ]
        )
    )
    return carousel_template_message


products_info1 = carousel_template_generator_one(
    alt_text='Carousel template',
    image_url='https://i.imgur.com/vG4FgDX.png',
    title='商品名稱、店家地址、商品數量種類',
    description='請輸入店家詳細資訊',
    label1='店家名稱',
    label1_info='我想要輸入店家名稱',
    label2='店家地址',
    label2_info='我想要輸入店家地址',
    label3='商品種類數量',
    label3_info='我想要輸入今天欲上架商品種類數量',
)


policy_buttons_template_message = buttons_template_generator_two(
    alt_text='policy button',
    title='我願意遵守使用者條款',
    title_info='願意遵守使用者條款',
    label1='願意',
    label1_reply='我已詳閱使用者條款並且願意遵守',
    label2='再看看',
    label2_reply='我還不太清楚使用者條款，可以給我看看使用者條款嗎？',
)

carousel_template_message = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://example.com/item1.jpg',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackAction(
                        label='postback1',
                        display_text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label='message1',
                        text='message text1'
                    ),
                    URIAction(
                        label='uri1',
                        uri='http://example.com/1'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://example.com/item2.jpg',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackAction(
                        label='postback2',
                        display_text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageAction(
                        label='message2',
                        text='message text2'
                    ),
                    URIAction(
                        label='uri2',
                        uri='http://example.com/2'
                    )
                ]
            )
        ]
    )
)

flex_message = TextSendMessage(
    text="請選擇要顯示的買賣超資訊",
    quick_reply=QuickReply(
        items=[
            QuickReplyButton(
                action=MessageAction(
                    label="最新法人", 
                    text="最新法人買賣超 "
                )
            ),
            QuickReplyButton(
                action=MessageAction(
                    label="歷年法人", 
                    text="歷年法人買賣超 "
                )
            ),
            QuickReplyButton(
                action=MessageAction(
                    label="外資", 
                    text="外資買賣超 "
                )
            ),
            QuickReplyButton(
                action=MessageAction(
                    label="投信", 
                    text="投信買賣超 "
                )
            ),
            QuickReplyButton(
                action=MessageAction(
                    label="自營商", 
                    text="自營商買賣超 "
                )
            ),
            QuickReplyButton(
                action=MessageAction(
                    label="三大法人", 
                    text="三大法人買賣超 "
                )
            )
        ]
    )
)