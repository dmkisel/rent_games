import telebot
from telebot import types
from backend.config import telebot_token

TOKEN = telebot_token

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Подтвердить регистрацию")
    btn2 = types.KeyboardButton("Проверить статус заказа")
    markup.add(btn1, btn2)
    bot.reply_to(message, "Добро пожаловать! Я ваш бот. Выберите действие")


# @bot.message_handler(content_types=['text'])
# def func(message):
#     if message.text == 'Подтвердить регистрацию':
#         data = str(message.from_user)
#         data_tg = json.loads(data)
#         result = verif.verif_user(data_tg)
#         if result:
#             bot.send_message(message, "Аккаунт подтверждён.")
#         else:
#             bot.send_message(message, "Аккаунт не найден.")


if __name__ == '__main__':
    bot.polling(none_stop=True)
