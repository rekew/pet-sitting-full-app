import logging
import sys
import asyncio
import signal
import platform
from telegram.ext import ApplicationBuilder
from telegram.request import HTTPXRequest
from config import TELEGRAM_TOKEN
from data.database import init_db, pg_pool
from bot.commands import get_command_handlers
from bot.conversation import nanny_registration_conv
from bot.auth import login_conv, quick_nav_cb
from bot.booking import booking_conv
from bot.search import search_conv
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
async def _shutdown(app):
    logging.info("Shutting down application …")
    await app.shutdown()
    pg_pool.closeall()
    await app.stop()
    logging.info("Bye! 👋")
def main() -> None:
    init_db()
    request = HTTPXRequest(connect_timeout=30, read_timeout=30)
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).request(request).build()
    for h in get_command_handlers():
        app.add_handler(h)

    app.add_handler(nanny_registration_conv)
    app.add_handler(login_conv)
    app.add_handler(quick_nav_cb)
    app.add_handler(booking_conv)
    app.add_handler(search_conv)
    if platform.system() != "Windows":
        loop = asyncio.get_event_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, lambda s=sig: asyncio.create_task(_shutdown(app)))
    else:
        pass

    print("Бот запущен! Нажмите Ctrl+C для остановки.")
    try:
        app.run_polling()
    except (KeyboardInterrupt, SystemExit):
       
        asyncio.run(_shutdown(app))
        sys.exit(0)


if __name__ == "__main__":
    main()
