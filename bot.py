from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import conversion_parser as cplib

MK = 0
UNIT = ""
UNIT_TO = ""

try:
    with open("env.txt", "r", encoding="utf8"
              ) as ENVFile:  # make sure you specify the encoding (utf8, ty)
        token = ENVFile.read()
        ENVFile.close()
except FileNotFoundError:
    print("File not found file I/O Err.")
    exit(1)
except FileExistsError:
    print("File does not exist file I/O Err.")
    exit(1)

updater = Updater(token, use_context=True)

print(f"Logged in as {updater.bot.id}")


def start(update: Update,
          context: CallbackContext):  # FIXME: Unused argument 'context' - why?
    update.message.reply_text("Ok!")


def define_unit(update: Update, context: CallbackContext
                ):  # FIXME: See above. Unused 'update' and 'context'
    """Dummy for now!"""


def helpcmd(update: Update, context: CallbackContext):
    update.message.reply_text(
        "/help - Display this message\n/start - Check if the bot is ready\n/define_unit OR /du [unit] [convert] [how_many_in] - Define a new unit that USC will add to its database of units where unit is the unit you are defining, convert is the unit you're converting to, and how_many_in is how many units are in the unit you're converting to."
    )


def unknown(update: Update, context: CallbackContext):
    #global hctd # why tf is this here? hctd is never defined...
    if update.message.text[0] == '/':
        update.message.reply_text("Sorry '%s' is not a command" %
                                  update.message.text)
    else:
        update.message.reply_text(str(cplib.parse(update.message.text, hctd)))


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', helpcmd))
updater.dispatcher.add_handler(CommandHandler('du', define_unit))
updater.dispatcher.add_handler(CommandHandler('define_unit', define_unit))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))

with open("conversions.hctd", "r", encoding="utf8") as conversions:
    hctd = conversions.read()
    conversions.close()
hctd = cplib.parse_hctd(hctd)
updater.start_polling()
