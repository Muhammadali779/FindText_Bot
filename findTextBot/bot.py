import telebot
from config import TOKEN

API_TOKEN = TOKEN
bot = telebot.TeleBot(API_TOKEN)

# ----------------- FOYDALANUVCHI MA'LUMOTI -----------------
USER_DATA = {}  # chat_id: {"text": "", "awaiting_word": True/False}

# ----------------- SEARCH ENGINE -----------------
def search_word(text, word, window=60):
    word_lower = word.lower()
    text_lower = text.lower()
    positions = []
    contexts = []

    index = 0
    while index < len(text_lower):
        index = text_lower.find(word_lower, index)
        if index == -1:
            break
        positions.append(index)

        start = max(0, index - window)
        end = min(len(text), index + len(word) + window)
        ctx = text[start:end].replace("\n", " ")
        contexts.append(ctx)
        index += len(word)
    return positions, contexts

def format_result(word, positions, contexts):
    if not positions:
        return f"'{word}' so'zi topilmadi."
    
    result = f"Topilgan so'z: '{word}'\n"
    result += f"Uchrashlar soni: {len(positions)}\n\n"
    result += "Kontekstlar:\n"
    for i, ctx in enumerate(contexts, 1):
        highlighted = ctx.replace(word, f"⭐{word}⭐")
        result += f"{i}. {highlighted}\n"
    return result

# ----------------- HANDLERS -----------------
@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    USER_DATA[chat_id] = {"text": "", "awaiting_word": False}
    bot.send_message(
        chat_id,
        "Salom! Matn qidirish uchun avval matn yuboring.\n"
        "So‘zlarni qidirish uchun vergul bilan ajrating (masalan: so‘z1, so‘z2).\n"
        "Yangi matn yubormoqchi bo‘lsangiz, /newtext yozing."
    )

@bot.message_handler(commands=['newtext'])
def new_text(message):
    chat_id = message.chat.id
    USER_DATA[chat_id]["awaiting_word"] = False
    bot.send_message(chat_id, "Iltimos, yangi matn yuboring:")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text.strip()

    # Telegram xabar uzunligi ~4096 belgi, shuning uchun foydalanuvchi xabarlarini biriktirib saqlash mumkin
    if chat_id not in USER_DATA:
        USER_DATA[chat_id] = {"text": text, "awaiting_word": True}
        bot.send_message(chat_id, "Matn qabul qilindi! Endi qaysi so'zni yoki so'zlarni qidiraylik?")
        return

    # Agar /newtext ishlatilsa yoki yangi matn kiritilsa
    if not USER_DATA[chat_id]["awaiting_word"]:
        USER_DATA[chat_id]["text"] = text
        USER_DATA[chat_id]["awaiting_word"] = True
        bot.send_message(chat_id, "Yangi matn qabul qilindi! Endi qaysi so'zni yoki so'zlarni qidiraylik?")
        return

    # So‘z(lar)ni qidirish
    main_text = USER_DATA[chat_id]["text"]
    words = [w.strip() for w in text.split(",") if w.strip()]
    if not words:
        bot.send_message(chat_id, "Iltimos, qidiriladigan so'zni kiriting.")
        return

    results = ""
    for word in words:
        positions, contexts = search_word(main_text, word, window=60)
        results += format_result(word, positions, contexts) + "\n\n"

    # Agar javob juda uzun bo‘lsa, uni bo‘lib yuborish
    for chunk in [results[i:i+4000] for i in range(0, len(results), 4000)]:
        bot.send_message(chat_id, chunk)

    bot.send_message(chat_id, "Yana boshqa so'zni qidirish uchun so'zni yozing yoki yangi matn yuboring (/newtext).")

# ----------------- BOT START -----------------
print("Bot ishga tushdi...")
bot.infinity_polling()
