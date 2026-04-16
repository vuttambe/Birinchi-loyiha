import telebot

bot = telebot.TeleBot("8709262637:AAFLgpQPqkJIDf8JVD6BhUbvJvuVQ_XHbmU")

@bot.message_handler(func=lambda m: True)
def javob(message):
    bot.reply_to(message, "Salom! Xabaringizni oldim: " + message.text)

bot.polling()
