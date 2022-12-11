#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

import os
import logging
import random

from dotenv import load_dotenv

from classes.diceRoller import DiceRoller
from classes.radwolf import RadAdvice
from classes.rant import Rant
import constants

from telegram import __version__ as TG_VER
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram.ext import Application, CommandHandler, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

GOBLIN_ROLLER = DiceRoller(random)

async def roll(update, context):
    global GOBLIN_ROLLER
    terms = ''.join(context.args).replace(" ", "").split("+")

    withBless = True if GOBLIN_ROLLER.get_goblin_bless() > 0 else False

    text_roll = GOBLIN_ROLLER.process_roll(withBless, terms)
    await update.message.reply_text(text_roll)


async def roll_fours(update, context):
    global GOBLIN_ROLLER
    qty = ''.join(context.args).replace(" ", "")

    text_roll = GOBLIN_ROLLER.process_fours(qty)
    await update.message.reply_text(text_roll)


async def goblin_bless(update, context):
    global GOBLIN_ROLLER
    GOBLIN_ROLLER.add_goblin_bless()
    goblin_bless_text = random.choice(constants.GOBLIN_BLESS_FRASES)
    
    await update.message.reply_text(goblin_bless_text)


async def radwolf(update, context):
    rad = RadAdvice()
    rad_text = rad.advise()
    await update.message.reply_text(rad_text)


async def ty_radwolf(update, context):
    rad_text = random.choice(constants.TY_RADWOLF_SPONSOR_FRASES)
    await update.message.reply_text(rad_text)


async def error_callback(update, context):
    LOGGER.error(msg="Exception while handling an update:", exc_info=context.error)

async def catra(update, context):
    await update.message.reply_text(constants.CATRA_TEXT)


async def bubblegum(update, context):
    await update.message.reply_text(constants.BUBBLEGUM_TEXT)


async def orc_gang(update, context):
    orc_num = random.randrange(100) + 1

    orc_text = ""

    if orc_num == 69:
        orc_text = constants.DADDY_ORC_GANG_TEXT
    else:
        orc_text = constants.ORC_GANG_TEXT.format(orc_num)

    await update.message.reply_text(orc_text)

async def rant(update, context):
    ranter = Rant() 
    rant_text = ranter.rant()
    await update.message.reply_text(rant_text)

async def start(update, context):
    await update.message.reply_text("Soy un bot goblin, hablenme!")

async def help(update, context):
    await update.message.reply_text(constants.HELP_TEXT)


def main() -> None:
    GOBLIN_TELEGRAM_BOT_API_TOKEN =  os.environ.get('GOBLIN_TELEGRAM_BOT_API_TOKEN', '')

    application = Application.builder().token(GOBLIN_TELEGRAM_BOT_API_TOKEN).build()

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

    application.add_handler(start_handler)
    application.add_handler(roll_handler)
    application.add_handler(rollfours_handler)
    application.add_handler(bless_handler)
    application.add_handler(rad_handler)
    application.add_handler(radwolf_handler)
    application.add_handler(tyrad_handler)
    application.add_handler(tyradwolf_handler)
    application.add_handler(catra_handler)
    application.add_handler(bubblegum_handler)
    application.add_handler(orcgang_handler)
    application.add_handler(rant_handler)
    application.add_handler(help_handler)
    
    application.add_error_handler(error_callback)
    
    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    load_dotenv() 
    main()