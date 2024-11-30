import requests
from dotenv import load_dotenv
import os

# .envファイルを読み込む
load_dotenv(override=True)

# Dify APIのAPIキー
API_KEY = os.getenv("API_KEY")
# Dify APIのベースURL
BASE_URL = os.getenv("DIFY_URL") + "/chat-messages"


def get_dify_response(message: str, user_id: str):
    # リクエストヘッダー
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    # リクエストボディ
    data = {
        "inputs": {},
        "query": message,
        "response_mode": "blocking",
        "user": user_id,
    }

    # POSTリクエストを送信
    response = requests.post(BASE_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["answer"]


if __name__ == "__main__":
    message = "オーストラリアの首都はどこ"
    user_id = "test_user"
    response = get_dify_response(message, user_id)
    print(response)
