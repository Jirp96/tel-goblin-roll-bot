import os

import logging
import random

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)

from diceRoller import DiceRoller
import constants

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

GOBLIN_ROLLER = DiceRoller(random)


def roll(update, context):
    global GOBLIN_ROLLER
    terms = ''.join(context.args).replace(" ", "").split("+")

    withBless = True if GOBLIN_ROLLER.get_goblin_bless() > 0 else False

    text_roll = GOBLIN_ROLLER.process_roll(withBless, terms)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_roll)


def roll_fours(update, context):
    global GOBLIN_ROLLER
    qty = ''.join(context.args).replace(" ", "")

    text_roll = GOBLIN_ROLLER.process_fours(qty)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_roll)


def goblin_bless(update, context):
    global GOBLIN_ROLLER
    GOBLIN_ROLLER.add_goblin_bless()
    goblin_bless_text = random.choice(constants.GOBLIN_BLESS_FRASES)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=goblin_bless_text)


def radwolf(update, context):
    rad_text = random.choice(constants.RADWOLF_FRASES)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rad_text)


def ty_radwolf(update, context):
    rad_text = random.choice(constants.TY_RADWOLF_SPONSOR_FRASES)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rad_text)


def error_callback(bot, update, context):
    try:
        raise context.error
    except BadRequest:
        LOGGER.warning('Update "%s" caused error "%s"', update, context.error)
    except TelegramError:
        LOGGER.warning('Update "%s" caused error "%s"', update, context.error)


def catra(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=constants.CATRA_TEXT)


def bubblegum(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=constants.BUBBLEGUM_TEXT)


def orc_gang(update, context):
    orc_num = random.randrange(100) + 1

    orc_text = ""

    if orc_num == 69:
        orc_text = constants.DADDY_ORC_GANG_TEXT
    else:
        orc_text = constants.ORC_GANG_TEXT.format(orc_num)

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=orc_text)

def rant(update, context):
    rad_text = random.choice(constants.RANTS)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rad_text)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Soy un bot goblin, hablenme!")


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Stoi chikito, no entendí ese comando.")


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=constants.HELP_TEXT)


def main():

    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(token=constants.TELEGRAM_BOT_API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    roll_handler = CommandHandler('roll', roll)
    bless_handler = CommandHandler('bless', goblin_bless)
    rad_handler = CommandHandler('rad', radwolf)
    radwolf_handler = CommandHandler('radwolf', radwolf)
    catra_handler = CommandHandler('catra', catra)
    bubblegum_handler = CommandHandler('bubblegum', bubblegum)
    orcgang_handler = CommandHandler('orcgang', orc_gang)
    tyrad_handler = CommandHandler('tyrad', ty_radwolf)
    tyradwolf_handler = CommandHandler('tyradwolf', ty_radwolf)
    help_handler = CommandHandler('help', help)
    rollfours_handler = CommandHandler('fours', roll_fours)
    rant_handler = CommandHandler('rant', rant)

    unknown_handler = MessageHandler(Filters.command, unknown)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(roll_handler)
    dispatcher.add_handler(rollfours_handler)
    dispatcher.add_handler(bless_handler)
    dispatcher.add_handler(rad_handler)
    dispatcher.add_handler(radwolf_handler)
    dispatcher.add_handler(tyrad_handler)
    dispatcher.add_handler(tyradwolf_handler)
    dispatcher.add_handler(catra_handler)
    dispatcher.add_handler(bubblegum_handler)
    dispatcher.add_handler(orcgang_handler)
    dispatcher.add_handler(rant_handler)
    dispatcher.add_handler(help_handler)
    

    dispatcher.add_handler(unknown_handler)
    dispatcher.add_error_handler(error_callback)

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=constants.TELEGRAM_BOT_API_TOKEN)
    updater.bot.set_webhook("https://{0}.herokuapp.com/{1}".format(
        constants.HEROKU_APP_NAME, constants.TELEGRAM_BOT_API_TOKEN))
    updater.idle()


if __name__ == "__main__":
    main()
