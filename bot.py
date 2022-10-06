from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import conversion_parser as cplib
try:
    with open("env.txt", "r") as ENVFile:
        token = ENVFile.read()
        ENVFile.close()
except FileNotFoundError:
    print("File not found file I/O Err.")
    exit(1)
except FileExistsError:
    print("File does not exist file I/O Err.")
    exit(1)

updater = Updater(token,
                  use_context=True)
  
print(f"Logged in as {updater.bot.id}")

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Ok!")

def define_unit(update: Update, context: CallbackContext):
    pass
def help(update: Update, context: CallbackContext):
    update.message.reply_text("/help - Display this message\n/start - Check if the bot is ready\n/define_unit OR /du - Define a new unit that USC will add to its database of units")
        
def unknown(update: Update, context: CallbackContext):
    if update.message.text[0] == '/':
        update.message.reply_text(
        "Sorry '%s' is not a command" % update.message.text)
    else:
        update.message.reply_text(
        "Sorry I can't convert that")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('du', define_unit))
updater.dispatcher.add_handler(CommandHandler('define_unit', define_unit))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))

updater.start_polling()