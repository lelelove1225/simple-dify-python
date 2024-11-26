from dotenv import load_dotenv
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from hello import get_dify_response

# 環境変数を読み込む
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

# Boltアプリを初期化
app = App(token=SLACK_BOT_TOKEN)


# メンションイベントに応答
@app.event("app_mention")
def respond_to_mention(event, say):
    user = event["user"]
    text = event["text"]
    response = get_dify_response(text, user)
    say(f"<@{user}> {response}")


# メッセージイベントを処理
@app.event("message")
def handle_message_events(body, logger):
    event = body.get("event", {})
    if "subtype" in event and event["subtype"] == "bot_message":
        # ボット自身のメッセージを無視
        return
    logger.info(event)


# アプリを起動
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
