import telebot
import random

token = open('token.txt', 'r').read()
bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Что мне можно сказать')
keyboard.row('Вывести рандомное число', 'Вывести рандомный цвет')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard)
    print("Bot started")


@bot.message_handler(content_types=['text'])
def start_message(message):
    input = message.text.lower()
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard2)

    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока', reply_markup=keyboard_remove)


    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, 'Хорошо')

    elif message.text.lower() == 'вывести рандомное число':
        bot.send_message(message.chat.id, random.random())

    elif message.text.lower() == 'в какую игру играешь?' or message.text.lower() == 'в какую игру играешь':
        randnum = random.randint(0, 3)
        if randnum == 0:
            bot.send_message(message.chat.id, 'World of Tanks')

        elif randnum == 1:
            bot.send_message(message.chat.id, 'Minecraft')

        elif randnum == 2:
            bot.send_message(message.chat.id, 'PUBG')

    elif message.text.lower() == 'что делаешь?' or message.text.lower() == 'что делаешь':
        randnum = random.randint(0, 3)
        if randnum == 0:
            bot.send_message(message.chat.id, 'Отдыхаю')

        elif randnum == 1:
            bot.send_message(message.chat.id, 'Играю в пк (можно спросить в какую игру я игрю)')

        elif randnum == 2:
            bot.send_message(message.chat.id, 'Общаюсь с другим ботом')


    elif message.text.lower() == 'вывести рандомный цвет':
        randnum = random.randint(0, 4)
        if randnum == 0:
            bot.send_message(message.chat.id, 'Красный')

        elif randnum == 1:
            bot.send_message(message.chat.id, 'Синий')

        elif randnum == 2:
            bot.send_message(message.chat.id, 'Зелёный')

        elif randnum == 3:
            bot.send_message(message.chat.id, 'Жёлтый')

    elif message.text.lower() == 'что мне можно сказать':
        bot.send_message(message.chat.id, 'Привет, пока, как дела?, что делаешь?')

    elif message.text.lower() == 'как дела?' or message.text.lower() == 'как дела':
        randnum = random.randint(0, 2)
        if randnum == 0:
            bot.send_message(message.chat.id, 'Хорошо')

        elif randnum == 1:
            bot.send_message(message.chat.id, 'Всё ок')


    else:
        inputa = list(input)
        if inputa[-1] == '?':
            bot.send_message(message.chat.id, 'Я не могу ответить на этот вопрос')

        else:
            randnum = random.randint(0, 2)
            if randnum == 0:
                bot.send_message(message.chat.id, 'Ага')

            elif randnum == 1:
                bot.send_message(message.chat.id, 'Понятно')

bot.polling()