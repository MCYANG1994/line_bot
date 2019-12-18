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

line_bot_api = LineBotApi('1Sr/Amy8ViALBfPx3pHg2u/uIFq1PLCzpqzGL8ruQDhKCtUs5g3zHK8uo5h0LLJcGkMJCvy427hQ4zDxA8H5PpFhzRXkM2zOHVok1OKOdlK6f9HXXFJDEsv+2O39FPa49ywztwDsh2CvgK0vRdLoQwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1821d1916e2690f4a90be9b1811e8fd3')


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
    msg = event.message.text
    r = "我看不懂你說什麼"

    if msg in ["hi", "Hi"]:
        r = "hi"
    if msg == "你吃飯了嗎":
        r = "還沒"
    elif msg == "你是誰"
        r = "機器人"
    

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()