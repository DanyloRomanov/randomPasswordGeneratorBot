from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from password_generator import generate_secure_password


# function to handle the /start command
def start(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f'''Hi {first_name}, nice to meet you!\n
I will help you to generate secure password!
Type /g and hit enter to generate password''')


# functions that returns generated password
def generate(update, context):
    update.message.reply_text(f'You new secure password is {generate_secure_password()}')


# function to handle normal text
def text(update, context):
    text_received = update.message.text
    update.message.reply_text(f'did you said "{text_received}" ?')


def main():
    TOKEN = "5438627941:AAF2qdXdkhzZTrn0yb-pSOvKgTiJRiOHsos"

    # create the updater, that will automatically create also a dispatcher and a queue to
    # make them dialogue
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("g", generate))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
