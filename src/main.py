#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

import os
import logging
from dotenv import load_dotenv

from utils.commands import COMMANDS, error_callback

from classes.telegramBot import TelegramBot
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
    
from logging.handlers import RotatingFileHandler
logging.basicConfig(
        handlers=[RotatingFileHandler('./py_goblin_bot.log', maxBytes=100000, backupCount=10)],
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')
LOGGER = logging.getLogger(__name__)

def main() -> None:
    GOBLIN_TELEGRAM_BOT_API_TOKEN = os.environ.get('GOBLIN_TELEGRAM_BOT_API_TOKEN', '')
    bot = TelegramBot(GOBLIN_TELEGRAM_BOT_API_TOKEN)
        
    for key, value in COMMANDS.items():
        bot.register_handler(key, value)
    bot.register_error_handler(error_callback)
    
    # Run the bot until the user presses Ctrl-C
    bot.start()

if __name__ == "__main__":
    load_dotenv() 
    main()