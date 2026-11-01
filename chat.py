import os
from openai import OpenAI

# قراءة المفتاح من متغيرات البيئة
api_key = os.environ.get("XAI_API_KEY")

if not api_key:
    print("خطأ: لم يتم العثور على مفتاح API.")
    exit(1)

# تهيئة العميل بالاتصال بخوادم xAI
client = OpenAI(
    api_key=api_key,
    base_url="https://api.x.ai/v1"  # عنوان Grok API
)

try:
    # إرسال الطلب إلى Grok
    response = client.chat.completions.create(
        model="grok-4.7",  # يمكنك تغيير الموديل حسب رصيدك (مثل grok-2-latest)
        messages=[
            {"role": "user", "content": "مرحباً! ما هو دوري أبطال أوروبا؟"}
        ],
        max_tokens=1024
    )
    
    # طباعة رد Grok
    print("Grok:", response.choices[0].message.content)

except Exception as e:
    print(f"حدث خطأ: {e}")
