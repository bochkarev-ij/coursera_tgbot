import telebot


token = '1939481803:AAGEqWIkEa0UXsibp-sMuB04GNB0wsY07Jg'
START, ADD, LIST, RESET = range(4)
bot = telebot.TeleBot(token)
USER_STATE = {'current_state': 5}


def set_state(state):
    USER_STATE['current_state'] = state


def get_state():
    return USER_STATE['current_state']


@bot.message_handler(commands=['add'])
def handle_message(message):
    set_state(ADD)
    bot.send_message(message.chat.id, text='Please enter address')


@bot.message_handler(func=lambda a: get_state() == ADD)
def handle_add(message):
    with open('list.txt', 'a') as f:
        f.write(message.text+'\n')
        bot.send_message(message.chat.id, text='Address added')
    set_state(START)


@bot.message_handler(commands=['list'])
def handle_list(message):
    with open('list.txt') as f:
        content = f.readlines()
    if len(content):
        message_text = "".join(content[-10:])
        bot.send_message(message.chat.id, text=message_text)
    else:
        bot.send_message(message.chat.id, text='address list is empty')
    #     bot.send_message(message.chat.id, text=f.readlines())

    set_state(START)


@bot.message_handler(commands=['reset'])
def handle_list(message):
    with open('list.txt', 'w+') as f:
        f.writelines([])
        bot.send_message(message.chat.id, text='Address list reset')
    set_state(START)


if __name__ == '__main__':
    bot.polling()
