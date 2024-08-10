from telegram.ext import Application, CommandHandler

class TelegramBot():
    def __init__(self, token):
        self.token = token
        self.bot = Application.builder().token(self.token).build()
    
    def register_handler(self, name, handler):
        self.bot.add_handler(CommandHandler(name, handler))
    
    def register_error_handler(self, handler):
        self.bot.add_error_handler(handler)
        
    # @staticmethod
    # async def create_reply_handler(update, context, ):
    #     await update.message.reply_text(text)
        
    def start(self):
        self.bot.run_polling()
    
    
    