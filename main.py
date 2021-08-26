import telebot

token = '1939481803:AAGEqWIkEa0UXsibp-sMuB04GNB0wsY07Jg'
bot = telebot.TeleBot(token)


@bot.message_handler()
def handle_message(message):
    print(message.text)
    bot.send_message(message.chat.id, text=message.text)

if __name__ == '__main__':
    bot.polling()
