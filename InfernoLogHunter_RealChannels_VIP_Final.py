
import time
import requests
import random
import string

BOT_TOKEN = "7339050095:AAGylwmPEwalWlpN2goNYhYMnKvzNlhoQh0"
OWNER_ID = "5711733208"

# مكان حفظ التراخيص
user_licenses = {}
generated_keys = set()

# قائمة روابط حقيقية قابلة للتوسع
real_links = [
    "https://t.me/linux_softwares",
    "https://t.me/hackpathway",
    "https://t.me/ITSecTeam",
    "https://t.me/digital_osint",
    "https://t.me/freelancerspro",
    "https://t.me/ZeroDayCommunity",
    "https://t.me/darktoolsbackup",
    "https://t.me/anonfilesmirror",
    "https://t.me/worldofmalware",
    "https://t.me/vpn_cracked"
]

# إرسال رسالة عبر البوت
def tg_send(text, user_id):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": user_id, "text": text, "parse_mode": "HTML"}
    )

# توليد ترخيص VIP
def generate_license():
    part1 = ''.join(random.choices(string.ascii_uppercase, k=4))
    part2 = ''.join(random.choices(string.digits, k=4))
    part3 = ''.join(random.choices("VIPKING2025", k=4))
    license_key = f"{part1}-{part2}-{part3}"
    generated_keys.add(license_key)
    return license_key

# ترحيب جهنمي
def handle_start(chat_id):
    tg_send("""
🔥 <b>InfernoLogHunter Online</b>

مرحبًا بك في ساحة النخبة التقنية!  
⚙️ هذا النظام يستخرج لك أفضل قنوات التليجرام من كل زاوية.

💥 أوامر المستخدم:
🧠 /license [key] — تفعيل الرخصة
🔑 /vipstatus — التحقق من رخصتك
📡 /today — جلب قناة من صنف ناري
🎫 /generate — توليد ترخيص (للمطور فقط)
📊 /status — معرفة حالة البوت

    """, chat_id)

# تفعيل ترخيص
def handle_license(chat_id, message):
    try:
        key = message.split(" ", 1)[1].strip()
        if key in generated_keys:
            user_licenses[chat_id] = key
           Run python InfernoLogHunter_RealChannels_VIP_Final.py
  File "/home/runner/work/infernotest1/infernotest1/InfernoLogHunter_RealChannels_VIP_Final.py", line 67
    tg_send(f"✅ تم تفعيل رخصة VIP الخاصة بك:
            ^
SyntaxError: unterminated f-string literal (detected at line 67)
Error: Process completed with exit code 1.
<code>{key}</code>", chat_id)
        else:
            tg_send("❌ المفتاح غير صالح أو غير معروف!", chat_id)
    except:
        tg_send("⚠️ استخدم: /license مفتاحك", chat_id)

# حالة الرخصة
def handle_vipstatus(chat_id):
    key = user_licenses.get(chat_id)
    if key:
        tg_send(f"🔐 رخصتك فعالة:
<code>{key}</code>", chat_id)
    else:
        tg_send("🚫 لا تملك رخصة VIP", chat_id)

# توليد ترخيص (للمطور فقط)
def handle_generate(chat_id):
    if chat_id != OWNER_ID:
        tg_send("🚫 الأمر محظور - فقط للمطور", chat_id)
        return
    new_key = generate_license()
    tg_send(f"🎫 تم إنشاء ترخيص VIP:
<code>{new_key}</code>", chat_id)

# جلب قناة فعالة
def send_today(chat_id):
    if chat_id not in user_licenses:
        tg_send("🚫 هذه الميزة تحتاج ترخيص VIP. استخدم: /license مفتاحك", chat_id)
        return
    channel = random.choice(real_links)
    tg_send(f"📡 قناة 🔥 لك:
👉 <a href='{channel}'>{channel}</a>", chat_id)

# حلقة التحقق من الرسائل
def polling():
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
                if not msg: continue

                chat_id = str(msg["chat"]["id"])
                text = msg.get("text", "").strip().lower()

                if text in ["/start", "start/", "start"]:
                    handle_start(chat_id)
                elif text.startswith("/license"):
                    handle_license(chat_id, text)
                elif text.startswith("/vipstatus"):
                    handle_vipstatus(chat_id)
                elif text.startswith("/generate"):
                    handle_generate(chat_id)
                elif text.startswith("/status"):
                    tg_send("✅ InfernoLogHunter يعمل بكفاءة. 🔥", chat_id)
                elif text.startswith("/today"):
                    send_today(chat_id)
                else:
                    tg_send("❓ أمر غير معروف. ابدأ بـ /start", chat_id)

        except Exception as err:
            print("[Polling Error]", err)
        time.sleep(4)

if __name__ == "__main__":
    tg_send("🌀 البوت الآن يعمل تلقائيًا. أرسل /start لتبدأ.", OWNER_ID)
    polling()
