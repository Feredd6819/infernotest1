
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

def send_new_channels():
    # هنا نفترض أن هذا هو المكان الذي يستخرج القنوات الجديدة
    # بدلًا من التكرار الفارغ، نتحقق هل فعلا هناك بيانات
    found_channels = get_fresh_channels()

    if found_channels:
        message = "📡 <b>قنوات جديدة 🔥:</b>\n\n"
        for channel in found_channels:
            message += f"🔗 {channel}\n"
        tg_send(message.strip(), BOT_TOKEN, USER_ID)
    else:
        print("[NO CHANNELS FOUND] لا يوجد جديد هذه المرة.")

def get_fresh_channels():
    # هنا تضع الذكاء الخاص بك لجلب القنوات
    # مثال تجريبي
    from random import randint
    test = randint(0, 2)
    if test == 0:
        return []  # لا يوجد قنوات
    else:
        return [f"https://t.me/sample_channel_{randint(1000,9999)}"]

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
                    continue

                print(f"[Command] {text}")
                if text.startswith("/start"):
                    tg_send("🤖 InfernoLogHunter جاهز! استخدم /today /elite /status /pdfreport", BOT_TOKEN, USER_ID)
                elif text.startswith("/today"):
                    send_new_channels()
                elif text.startswith("/elite"):
                    tg_send("💎 القنوات الـ VIP المميزة جاهزة!", BOT_TOKEN, USER_ID)
                elif text.startswith("/status"):
                    tg_send("✅ النظام يعمل بنجاح. يتم البحث كل 20 دقيقة.", BOT_TOKEN, USER_ID)
                elif text.startswith("/pdfreport"):
                    tg_send("📄 التقرير قيد الإعداد...", BOT_TOKEN, USER_ID)
                else:
                    tg_send("❓ أمر غير معروف. جرب /start", BOT_TOKEN, USER_ID)

        except Exception as err:
            print("[Polling error]", err)
        time.sleep(5)

if __name__ == "__main__":
    tg_send("🔁 بدء التشغيل الذكي... انتظر النتائج في حال وجود قنوات.", BOT_TOKEN, USER_ID)
    send_new_channels()  # تشغيل مبدئي
    poll_telegram()
