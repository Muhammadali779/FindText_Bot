Quyida sening boting uchun **professional darajadagi README.md** tayyorlab berdim.
Dasturchilar uchun tushunarli, tartibli va to‘liq.

---

# 📘 **FindText Bot — Matn Ichidan So‘z Qidiruvchi Telegram Bot**

FindText Bot — bu foydalanuvchi yuborgan matndan so‘z yoki so‘zlar qidirib beradigan Telegram bot.
Bot **kontekst** (atrofidagi so‘zlar) bilan birga qidiruv natijalarini qaytaradi va uzun matnlarni ham boshqaradi.

---

# 🚀 **Botning Maqsadi**

* Foydalanuvchi yuborgan matndan bir yoki bir nechta so‘zlarni qidirish
* Topilgan so‘zning atrofidagi kontekstni chiqarish
* Matnlar juda uzun bo‘lsa ham ulardan so‘zlarni izlab berish
* Foydalanuvchiga bir nechta so‘zni vergul bilan ajratib qidirish imkonini berish
* Xohlagan paytda yangi matn kiritish imkonini berish

Bu bot ayniqsa:

* talabalar
* ilmiy ish qiluvchilar
* matn ustida ishlovchilar
* PDF/Word dan matn ko‘chirib analiz qiluvchilar
  uchun juda qulay.

---

# 📂 **Loyiha Tuzilmasi**

```
FindText_Bot/
│
├── bot.py                # Asosiy bot logikasi
├── config.py             # TOKEN saqlanadigan fayl (GitHubga chiqmaydi)
├── config_example.py     # Token o'rni bo'sh misol fayl
├── requirements.txt      # Kutubxonalar ro‘yxati
└── README.md             # Loyihaning tavsifi
```

---

# 🔐 **Tokenni himoya qilish**

`config.py` fayli GitHubga chiqmasligi kerak.
U `.gitignore` ichiga qo‘shilgan:

```
config.py
```

TOKEN faqat `config_example.py` ichida ko‘rsatiladi (bo‘sh holda).

---

# ⚙️ **O‘rnatish (Installation)**

1. Loyihani yuklab oling:

```sh
git clone https://github.com/username/FindText_Bot.git
cd FindText_Bot
```

2. Virtual environment yarating:

```sh
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

3. Kerakli kutubxonalarni o‘rnating:

```sh
pip install -r requirements.txt
```

4. Tokenni kiriting:

`config.py` fayl yarating:

```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

5. Botni ishga tushiring:

```sh
python bot.py
```

---

# 🤖 **Botning Qanday Ishlashi**

### ▶️ **1. /start**

Foydalanuvchi start bosganda bot quyidagilarni qiladi:

* USER_DATA ichida chat uchun bo‘sh maydon yaratadi
* Foydalanuvchidan matn yuborishni so‘raydi

### ▶️ **2. Foydalanuvchi matn yuboradi**

Bot matnni qabul qiladi va:

> “Matn qabul qilindi! Endi qaysi so‘zni qidiraylik?”
> — deb javob beradi.

### ▶️ **3. Foydalanuvchi so‘z yoki so‘zlarni yuboradi**

Misollar:

```
kitob
ona
dunyo, vaqt, odam
```

Bot qiladigan ishlar:

* so‘zni matndan qidiradi
* topilgan joylar sonini hisoblaydi
* har bir topilgan so‘zning ±60 ta belgisi kontekstini chiqaradi
* so‘zlarni ⭐ belgisi bilan belgilaydi

### ▶️ **4. Javob juda uzun bo‘lsa → bo‘lib yuboradi**

Telegramning **4096 belgidan oshmasligi** uchun bot natijani avtomatik bo‘ladi.

### ▶️ **5. /newtext**

Foydalanuvchi yangi matn kiritmoqchi bo‘lsa:

* eski matn o‘chiriladi
* bot “Yangi matn yuboring” deb so‘raydi

---

# 🧠 **Funksiyalar izohi**

### 🔎 `search_word(text, word, window=60)`

* Matndan so‘zni qidiradi
* Topilgan joyning indeksini qaytaradi
* Har bir so‘zning 60 belgi oldi va orqasidan kontekst oladi
* `lower()` orqali katta-kichik harfni bir xil qiladi

### 📝 `format_result(word, positions, contexts)`

* So‘z topilmasa → xabar qaytaradi
* Topilgan bo‘lsa → tartiblangan natija chiqaradi
* So‘zni ⭐ bilan ajratadi

---

# 📦 **requirements.txt**

```
pyTelegramBotAPI==4.21.0
```

---

# 🧑‍💻 **Dasturchilar uchun tavsiyalar**

* `USER_DATA` hozir RAM ichida saqlanadi → katta loyihalarda bazaga o‘tish tavsiya etiladi

* Kelajakda PDF/Word fayllarni ham qabul qilish uchun:

  * `PyPDF2`
  * `python-docx`
    qo‘shilishi mumkin

* Tokenni hech qachon GitHubga qo‘ymang

* Botni serverda ishga tushirish uchun:

  * Uvicorn
  * Supervisor
  * Docker
    ishlatish tavsiya qilinadi

---
