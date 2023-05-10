import telebot
from translate import Translator
import random

bot = telebot.TeleBot('1855541290:AAFO0qIZzOsBRL6Rj1-grFkbO6cFIpgkLLg')
translator = Translator(to_lang="ar")

# قائمة من الإشعارات
quotes = [
    "Life is like riding a bicycle. To keep your balance, you must keep moving. - Albert Einstein",
    "Be the change that you wish to see in the world. - Mahatma Gandhi",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Don't cry because it's over, smile because it happened. - Dr. Seuss",
    " am attacked by a sadness that should not be mine."
]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً وسهلاً! أرسل لي /quote للحصول على اقتباس قصير باللغة الإنجليزية وترجمته إلى العربية.")

@bot.message_handler(commands=['quote'])
def send_quote(message):
    # اختيار اقتباس قصير عشوائية من القائمة
    quote = random.choice(quotes)
    
    # ترجمة الاقتباس إلى العربية
    translated_quote = translator.translate(quote)
    
    # إرسال الاقتباس وترجمته
    bot.reply_to(message, quote + "\n\n" + translated_quote)

bot.polling()