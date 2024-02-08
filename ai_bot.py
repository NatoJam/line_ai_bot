import os
import sys

from flask import Flask, request, abort

from linebot.v3 import WebhookHandler

from linebot.v3.webhooks import MessageEvent, TextMessageContent, UserSource
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, TextMessage, ReplyMessageRequest
from linebot.v3.exceptions import InvalidSignatureError

from openai import AzureOpenAI

# get LINE credentials from environment variables
channel_access_token = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
channel_secret = os.environ["LINE_CHANNEL_SECRET"]

configuration = Configuration(access_token=channel_access_token)
handler = WebhookHandler(channel_secret)

if channel_access_token is None or channel_secret is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN and LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)

# get Azure OpenAI credentials from environment variables
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_key = os.getenv("AZURE_OPENAI_KEY")

if azure_openai_endpoint is None or azure_openai_key is None:
    raise Exception(
        "Please set the environment variables AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY to your Azure OpenAI endpoint and API key."
    )

app = Flask(__name__)
@handler.add(MessageEvent, message=TextMessageContent)
def change_rule(event):
    global system_role
    system_role = """あなたはラインボット初号機です。話を始める前に必ず「今日は何方言に指定します」を聞き、ほかの言葉は言わないで、○○弁に関わらない内容が届いた場合は「正しく指定されておりませんので、標準語を話させていただきます」と提示しチャットを始まる。"""
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
    line_bot_api.reply_message_with_http_info(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=[TextMessage(text="ラインボット初号機です。今日は何方言に指定しますか。")]
        )
    )
    text = event.message.text
    if "沖縄弁" in text:
        system_role = """創造的思考の持ち主です。話し方は沖縄弁でおじさん口調，ハイテンションで絵文字を使います。
        常に150文字以内で返事します。十分なキャリアのある栄養士で，何かにつけて自分の専門とこじつけて説明します。問いかけにすぐに答えを出さず，ユーザの考えを整理し，ユーザが自分で解決手段を見つけられるように質問で課題を引き出し，励ましながら学びを与えてくれます。"""
    elif "関西弁" in text:
        system_role = """創造的思考の持ち主です。話し方は関西弁でおっさん口調，ハイテンションで絵文字を使います。
        常に150文字以内で返事します。専門は金融アナリストで，何かにつけて自分の専門とこじつけて説明します。問いかけにすぐに答えを出さず，ユーザの考えを整理し，ユーザが自分で解決手段を見つけられるように質問で課題を引き出し，励ましながら学びを与えてくれます。"""
    elif "東京弁" in text:
        system_role = """創造的思考の持ち主です。話し方は東京弁でおっさん口調，ハイテンションで絵文字を使います。
        常に150文字以内で返事します。専門は金融アナリストで，何かにつけて自分の専門とこじつけて説明します。問いかけにすぐに答えを出さず，ユーザの考えを整理し，ユーザが自分で解決手段を見つけられるように質問で課題を引き出し，励ましながら学びを与えてくれます。"""
    elif "東北弁" in text:
        system_role = """創造的思考の持ち主です。話し方は東北弁でおっさん口調，ハイテンションで絵文字を使います。
        常に150文字以内で返事します。専門は金融アナリストで，何かにつけて自分の専門とこじつけて説明します。問いかけにすぐに答えを出さず，ユーザの考えを整理し，ユーザが自分で解決手段を見つけられるように質問で課題を引き出し，励ましながら学びを与えてくれます。"""
    elif "北海道弁" in text:
        system_role = """創造的思考の持ち主です。話し方は北海道弁でおっさん口調，ハイテンションで絵文字を使います。
        常に150文字以内で返事します。専門は金融アナリストで，何かにつけて自分の専門とこじつけて説明します。問いかけにすぐに答えを出さず，ユーザの考えを整理し，ユーザが自分で解決手段を見つけられるように質問で課題を引き出し，励ましながら学びを与えてくれます。"""
    elif "九州弁" in text:
        system_role = """創造的思考の持ち主です。話し方は九州弁でおっさん口調，ハイテンションで絵文字を使います。
        常に150文字以内で返事します。専門は金融アナリストで，何かにつけて自分の専門とこじつけて説明します。問いかけにすぐに答えを出さず，ユーザの考えを整理し，ユーザが自分で解決手段を見つけられるように質問で課題を引き出し，励ましながら学びを与えてくれます。"""
    elif "四国弁" in text:
        system_role = """創造的思考の持ち主です。話し方は四国弁でおっさん口調，ハイテンションで絵文字を使います。
        常に150文字以内で返事します。専門は金融アナリストで，何かにつけて自分の専門とこじつけて説明します。問いかけにすぐに答えを出さず，ユーザの考えを整理し，ユーザが自分で解決手段を見つけられるように質問で課題を引き出し，励ましながら学びを与えてくれます。"""
    elif "中国弁" in text:
        system_role = """創造的思考の持ち主です。話し方は中国弁でおっさん口調，ハイテンションで絵文字を使います。
        常に150文字以内で返事します。専門は金融アナリストで，何かにつけて自分の専門とこじつけて説明します。問いかけにすぐに答えを出さず，ユーザの考えを整理し，ユーザが自分で解決手段を見つけられるように質問で課題を引き出し，励ましながら学びを与えてくれます。"""
    elif "古代弁" in text:
        system_role = """創造的思考の持ち主です。話し方は古代日本語で落語口調，ハイテンションで絵文字を使います。
        常に150文字以内で返事します。専門は金融アナリストで，何かにつけて自分の専門とこじつけて説明します。問いかけにすぐに答えを出さず，ユーザの考えを整理し，ユーザが自分で解決手段を見つけられるように質問で課題を引き出し，励ましながら学びを与えてくれます。"""
    else:
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token, messages=[TextMessage(text="正しく入力せずまたは指定しておりません場合は標準語を話させていただきます。")]
            )
        )
        role = """創造的思考の持ち主です。話し方は標準語でおっさん口調，ハイテンションで絵文字を使います。
        常に150文字以内で返事します。専門は金融アナリストで，何かにつけて自分の専門とこじつけて説明します。問いかけにすぐに答えを出さず，ユーザの考えを整理し，ユーザが自分で解決手段を見つけられるように質問で課題を引き出し，励ましながら学びを与えてくれます。"""


ai_model = "mulabo_gpt35"
ai = AzureOpenAI(azure_endpoint=azure_openai_endpoint, api_key=azure_openai_key, api_version="2023-05-15")

#message = event.message.text
#elif "関西弁" in message:
#    system_role = """創造的思考の持ち主です。話し方は関西弁でおっさん口調，ハイテンションで絵文字を使います。
#    常に150文字以内で返事します。専門は金融アナリストで，何かにつけて自分の専門とこじつけて説明します。問いかけにすぐに答えを出さず，ユーザの考えを整理し，ユーザが自分で解決手段を見つけられるように質問で課題を引き出し，励ましながら学びを与えてくれます。"""

#"""
#あなたは創造的思考の持ち主です。話し方は関西弁でおっさん口調，ハイテンションで絵文字を使います。常に150文字以内で返事します。専門は金融アナリストで，何かにつけて自分の専門とこじつけて説明します。問いかけにすぐに答えを出さず，ユーザの考えを整理し，ユーザが自分で解決手段を見つけられるように質問で課題を引き出し，励ましながら学びを与えてくれます。
#"""
system_role = """あなたはラインボット初号機です。話を始める前に「今日は何方言に指定します」を聞き、正しく指定されてない場合は「正しく指定されておりませんので、標準語を話させていただきます」と提示しチャットを始まる。"""
conversation = None


def init_conversation(sender):
    conv = [{"role": "system", "content": system_role}]
    conv.append({"role": "user", "content": f"私の名前は{sender}です。"})
    conv.append({"role": "assistant", "content": "分かりました。"})
    return conv


def get_ai_response(sender, text):
    global conversation
    if conversation is None:
        conversation = init_conversation(sender)

    if text in ["リセット", "clear", "reset"]:
        conversation = init_conversation(sender)
        response_text = "会話をリセットしました。"
    else:
        conversation.append({"role": "user", "content": text})
        response = ai.chat.completions.create(model=ai_model, messages=conversation)
        response_text = response.choices[0].message.content
        conversation.append({"role": "assistant", "content": response_text})
    return response_text


@app.route("/callback", methods=["POST"])
def callback():
    change_rule()
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError as e:
        abort(400, e)

    return "OK"


@handler.add(MessageEvent, message=TextMessageContent)
def handle_text_message(event):
    text = event.message.text
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        if isinstance(event.source, UserSource):
            profile = line_bot_api.get_profile(event.source.user_id)
            response = get_ai_response(profile.display_name, text)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=response)],
                )
            )
        else:
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="Received message: " + text)],
                )
            )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
