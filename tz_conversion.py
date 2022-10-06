import datetime
import pytz
# import everyting required for Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# if a user's message is in the format hh:mm TZ1 TZ2, then convert the time from TZ1 to TZ2
# TODO: fix this so that it works in bot.py
# maybe even add defitions to conversions.hctd instead of pytz's timezone list

def convert_time(bot, update):
    message = update.message.text
    if len(message.split()) == 3:
        try:
            time = datetime.datetime.strptime(message.split()[0], "%H:%M")
            time = pytz.timezone(message.split()[1]).localize(time)
            time = time.astimezone(pytz.timezone(message.split()[2]))
            bot.send_message(chat_id=update.message.chat_id,
                             text=time.strftime("%H:%M"))
        except ValueError:
            bot.send_message(chat_id=update.message.chat_id,
                             text="Invalid time format, please use hh:mm")
        except pytz.exceptions.UnknownTimeZoneError:
            bot.send_message(chat_id=update.message.chat_id,
                             text="Unknown timezone")
    else:
        bot.send_message(chat_id=update.message.chat_id,
                         text="Invalid format, please use hh:mm TZ1 TZ2")
