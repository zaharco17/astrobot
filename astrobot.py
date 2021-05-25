
import datetime
import logging
from telegram import update # для записи отчета о работе бота, импортитруем logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem



# записывать будет все сообщения уровня INFO и выше в файл bot.log
logging.basicConfig(filename='bot.log', level=logging.INFO)

def planet(pl, date):
    mars = ephem.pl(date)# pl (введенная планета) '2000/01/01'(дата)
    constellation = ephem.constellation(mars)
    return(constellation)    



def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text('введите дату цифрами "год/месяц/число" :')

def dt(update, context):
    text = update.message.text
    print(text)
    pl = talk_to_me.user_text
    answer = planet(pl,text)
    update.message.answer

def greet_user(update, context):
    print('Вызван /start') # пишет в консоли
    update.message.reply_text("привет. выбери и введи планету:\n Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune ") # пишет в чат
    
def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True) # ключ скрыт в файле settings
    dp = mybot.dispatcher # бот диспетчер
    # при нажатии "старт" вызовет функцию greet_user
    dp.add_handler(CommandHandler("start", greet_user))
    
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, dt))

    logging.info("Бот стартовал") # залогируем начало работы бота

    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

if __name__ == "__main__":
    main()