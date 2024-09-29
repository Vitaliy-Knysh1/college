import telebot

token = "7778416994:AAE0dWY2jUI6_X2XsqUeRF7I6EQ0b-fTmcE"

bot = telebot.TeleBot(token=token)

@bot.message_handler(content_types=["text"])
def message_recived(message):
    print (message)
    bot.send_message(chat_id=message.from_user.id, text=message.text)

bot.polling(True)
