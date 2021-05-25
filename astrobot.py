from Astro_Bot.settings import API_KEY
import logging
from telegram import update # для записи отчета о работе бота, импортитруем logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# записывать будет все сообщения уровня INFO и выше в файл bot.log
logging.basicConfig(filename='bot.log', level=logging.INFO)

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def greet_user(update, context):
    print('Вызван /start') # пишет в консоли
    update.message.reply_text("привет. начнем?") # пишет в чат

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(API_KEY, use_context=True)
    dp = mybot.dispatcher # бот диспетчер
    # при нажатии "старт" вызовет функцию greet_user
    dp.add_handler(CommandHandler("start", greet_user))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал") # залогируем начало работы бота

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

if __name__ == "__main__":
    main()