import os

import logging
import random

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

TELEGRAM_BOT_API_TOKEN='***REMOVED***'
HEROKU_APP_NAME='tel-goblin-roll-bot'

AVAILABLE_DICE = ["d2","d4","d6","d8","d10","d12","d20","d100"]

RADWOLF_FRASES = [
        "Este bot está auspiciado por Garbarino", 
        "Es solo un lobo con camisa! Nada más.", 
        "Licenciado* Radwolf.", 
        "Por favor, ya no más."
    ]

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
LOGGER = logging.getLogger(__name__)

def rollDice(max):
    return random.randrange(max) + 1

def error(bot, update, error):
    LOGGER.warning('Update "%s" caused error "%s"', update, error)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Soy un bot goblin, hablenme!")

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Stoi chikito, no entendí ese comando.")

def roll(update, context):
    dNum = context.args[0]
    text_roll = "Dado inválido, opciones: {0}".format(AVAILABLE_DICE)

    if dNum in AVAILABLE_DICE:
        num = int(dNum[1:])
        text_roll = '=> {0}'.format(rollDice(num))
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_roll)

def radwolf(update, context):
    rad_text = random.choice(RADWOLF_FRASES)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rad_text)

def main():    

    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(token=TELEGRAM_BOT_API_TOKEN, use_context=True)    
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    roll_handler = CommandHandler('roll', roll)
    rad_handler = CommandHandler('rad', radwolf)
    radwolf_handler = CommandHandler('radwolf', radwolf)

    unknown_handler = MessageHandler(Filters.command, unknown)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(roll_handler)
    dispatcher.add_handler(rad_handler)
    dispatcher.add_handler(radwolf_handler)


    dispatcher.add_handler(unknown_handler)
    dispatcher.add_error_handler(error)
    
    updater.start_webhook(listen="0.0.0.0",
                        port=PORT,
                        url_path=TELEGRAM_BOT_API_TOKEN)
    updater.bot.set_webhook("https://{0}.herokuapp.com/{1}".format(HEROKU_APP_NAME, TELEGRAM_BOT_API_TOKEN))
    updater.idle()


if __name__ == "__main__":
    main()