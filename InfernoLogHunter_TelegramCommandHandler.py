
import time
import requests

BOT_TOKEN = "7339050095:AAGylwmPEwalWlpN2goNYhYMnKvzNlhoQh0"
USER_ID = "5711733208"

def tg_send(text, token, user_id):
    try:
        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={"chat_id": user_id, "text": text, "parse_mode": "HTML"}
        )
    except Exception as e:
        print("Send error:", e)

def send_today():
    tg_send("📆 قائمة القنوات اليوم (تجريبية)...", BOT_TOKEN, USER_ID)

def send_elite():
    tg_send("💎 القنوات الـ VIP المميزة جاهزة!", BOT_TOKEN, USER_ID)

def generate_summary():
    return "✅ النظام شغال بكفاءة عالية 🔥"

def export_pdf_report():
    tg_send("📄 تم تجهيز تقرير PDF (قريباً)!", BOT_TOKEN, USER_ID)

def poll_telegram():
    offset = None
    while True:
        try:
            res = requests.get(
                f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates",
                params={"offset": offset, "timeout": 10}
            ).json()

            for update in res.get("result", []):
                offset = update["update_id"] + 1
                msg = update.get("message")
                if not msg:
                    continue

                chat_id = str(msg["chat"]["id"])
                text = msg.get("text", "").strip()

                if chat_id != USER_ID:
                    tg_send("🚫 وصول مرفوض. هذا النظام مخصص فقط للمطور.", BOT_TOKEN, chat_id)
                    continue

                print(f"[Command] {text}")
                if text.startswith("/start"):
                    tg_send("🤖 InfernoLogHunter جاهز! استخدم /today /elite /status /pdfreport", BOT_TOKEN, USER_ID)
                elif text.startswith("/today"):
                    send_today()
                elif text.startswith("/elite"):
                    send_elite()
                elif text.startswith("/status"):
                    tg_send(generate_summary(), BOT_TOKEN, USER_ID)
                elif text.startswith("/pdfreport"):
                    export_pdf_report()
                else:
                    tg_send("❓ أمر غير معروف. جرب /start", BOT_TOKEN, USER_ID)

        except Exception as err:
            print("[Polling error]", err)
        time.sleep(5)

if __name__ == "__main__":
    tg_send("🔁 بدء التحقق من الأوامر...", BOT_TOKEN, USER_ID)
    poll_telegram()
