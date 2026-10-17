import requests

# ضع رمز التفعيل الخاص بك هنا تماماً كما وصلك من BotFather
TOKEN = "8613606617:AAHm-Em3GMVyF_FUgKc6Bi5Pf8EnuMGXmE8[span_0](start_span)"[span_0](end_span)

# رقم معرف المستخدم الخاص بك (Chat ID) لتستقبل الرسالة عليه، أو يمكنك استبداله بمعرف الدردشة الخاص بك
CHAT_ID = "ضع_معرف_الدردشة_هنا"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.post(url, json=payload)
    return response.json()

# تجربة إرسال رسالة اختبارية
if __name__ == "__main__":
    result = send_message("مرحباً! هذا اختبار لربط بوت تيليجرام بلغة بايثون بنجاح.")
    print(result)
