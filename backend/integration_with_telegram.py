
import requests

def tg_send(text, bot_token, user_id):
    requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage",
                  data={"chat_id": user_id, "text": text, "parse_mode": "HTML"})

BOT_TOKEN = "7339050095:AAGylwmPEwalWlpN2goNYhYMnKvzNlhoQh0"
USER_ID = "5711733208"

tg_send("🔥 InfernoLogHunter VIP Dashboard Activated!", BOT_TOKEN, USER_ID)
