from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

updater = Updater('5097017995:AAEK4WHhBwoRspkuXBkQWsZVwNoESxR-EHs')

updater.dispatcher.add_handler(CommandHandler('start', hello))

updater.start_polling()
updater.idle()