import logging
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from telegram.request import HTTPXRequest
from data.config import TELEGRAM_TOKEN
from data.database import init_db
from bot.commands import start, view_nannies, myinfo, nanny_details, my_bookings, help_command,delete_my_nanny_profile
from bot.conversation import nanny_registration_conv
from bot.auth import login_conv
from bot.booking import booking_conv
from bot.search import search_conv

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
 
    init_db()
    
    request = HTTPXRequest(connect_timeout=30, read_timeout=30)
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).request(request).build()
    
  
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("view_nannies", view_nannies))
    app.add_handler(CommandHandler("myinfo", myinfo))
    app.add_handler(CommandHandler("my_bookings", my_bookings))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("delete_me", delete_my_nanny_profile))
    app.add_handler(nanny_registration_conv)
    app.add_handler(login_conv)
    app.add_handler(booking_conv)
    app.add_handler(search_conv)
    app.add_handler(CallbackQueryHandler(nanny_details, pattern=r'^nanny_\d+$'))
    
    print("Бот запущен!")
    app.run_polling()

if __name__ == '__main__':
    main()