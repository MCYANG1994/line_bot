from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('gPMv3W5zgM3hw3bzk7aBUrk6SP6/MYioBiWgHAOmab6dSFjirv9IjkUFvnz7V9npXUI4+YlliGa8zIk99mcmmjnf42AbifegSdBUGDuHvON4/I8jhiUUR/SD32MdjqYLH3Y+jfxAl5BWRok2n3dxcgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f9f55994307fca13eb056bdf34bc68ce')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()