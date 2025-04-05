import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram.request import HTTPXRequest  
from config import TELEGRAM_TOKEN
from bot.commands import start, view_nannies, myinfo
from bot.conversation import nanny_registration_conv
from bot.auth import login_conv

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
   
    request = HTTPXRequest( connect_timeout=30, read_timeout=30)
    
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).request(request).build()

   
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("view_nannies", view_nannies))
    app.add_handler(CommandHandler("myinfo", myinfo))

    
    app.add_handler(nanny_registration_conv)
    app.add_handler(login_conv)

    print("Бот запущен!")
    app.run_polling()

if __name__ == '__main__':
    main()