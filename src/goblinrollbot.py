import os

import logging
import random
from src.diceRoller import DiceRoller

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

from src import constants

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
LOGGER = logging.getLogger(__name__)

GOBLIN_ROLLER = DiceRoller(random)

def roll(update, context):
    global GOBLIN_ROLLER
    terms = ''.join(context.args).replace(" ","").split("+")
    
    withBless = True if GOBLIN_ROLLER.getGoblinBless() > 0 else False

    text_roll = GOBLIN_ROLLER.processRoll(terms, withBless)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_roll)

def goblinBless(update, context):
    global GOBLIN_ROLLER
    GOBLIN_ROLLER.addGoblinBless()
    goblin_bless_text = random.choice(constants.GOBLIN_BLESS_FRASES)
    context.bot.send_message(chat_id=update.effective_chat.id, text=goblin_bless_text)

def radwolf(update, context):
    rad_text = random.choice(constants.RADWOLF_FRASES)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rad_text)

def tyradwolf(update, context):
    rad_text = random.choice(constants.TY_RADWOLF_SPONSOR_FRASES)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rad_text)

def error(bot, update, error):
    LOGGER.warning('Update "%s" caused error "%s"', update, error)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Soy un bot goblin, hablenme!")

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Stoi chikito, no entendí ese comando.")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=constants.HELP_TEXT)

def main():    

    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(token=constants.TELEGRAM_BOT_API_TOKEN, use_context=True)    
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    roll_handler = CommandHandler('roll', roll)
    bless_handler = CommandHandler('bless', goblinBless)
    rad_handler = CommandHandler('rad', radwolf)
    radwolf_handler = CommandHandler('radwolf', radwolf)
    tyrad_handler = CommandHandler('tyrad', tyradwolf)
    tyradwolf_handler = CommandHandler('tyradwolf', tyradwolf)
    help_handler = CommandHandler('help', help)

    unknown_handler = MessageHandler(Filters.command, unknown)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(roll_handler)
    dispatcher.add_handler(bless_handler)
    dispatcher.add_handler(rad_handler)
    dispatcher.add_handler(radwolf_handler)
    dispatcher.add_handler(tyrad_handler)
    dispatcher.add_handler(tyradwolf_handler)
    dispatcher.add_handler(help_handler)

    dispatcher.add_handler(unknown_handler)
    dispatcher.add_error_handler(error)
    
    updater.start_webhook(listen="0.0.0.0",
                        port=PORT,
                        url_path=constants.TELEGRAM_BOT_API_TOKEN)
    updater.bot.set_webhook("https://{0}.herokuapp.com/{1}".format(constants.HEROKU_APP_NAME, constants.TELEGRAM_BOT_API_TOKEN))
    updater.idle()


if __name__ == "__main__":
    main()