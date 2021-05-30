
import logging # для записи отчета о работе бота, импортитруем logging
from telegram import update 
from telegram.ext import Updater, CommandHandler
import settings
import ephem
import datetime

# записывать будет все сообщения уровня INFO и выше в файл bot.log
logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /planet')
    ans = update.message.text.split()
    pl = ans[1]
    
    update.message.reply_text(f'созвездие, {planet(pl)}') # пишет в чат

def planet(pl):
    A = getattr(ephem,pl)(datetime.date.today()) 
    constellation = ephem.constellation(A)
    return constellation    

def main():
    mybot = Updater(settings.API_KEY, use_context=True) 
    dp = mybot.dispatcher 
    dp.add_handler(CommandHandler("planet", greet_user))
    logging.info("Бот стартовал") 
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()

