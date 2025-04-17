# bot.py
import os
import httpx
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)


BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "PASTE_YOUR_TOKEN_HERE")
API_URL   = os.getenv("BACKEND_API_URL",   "http://localhost:8000")
# --------------------------------------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Команда /start – приветствие."""
    await update.message.reply_text(
        "Привет! Я помогу найти няню для вашего питомца 🐾\n"
        "Список доступных нянь – командой /sitters.\n"
        "Можно указать город: /sitters Astana"
    )

async def sitters(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Команда /sitters [город] – выводит нянь из бэкенда."""
    city = " ".join(context.args) if context.args else None
    url  = f"{API_URL}/sitters"
    if city:
        url += f"?city={city}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
    if resp.status_code != 200:
        await update.message.reply_text("Сервис временно недоступен 😕")
        return

    sitters = resp.json()
    if not sitters:
        await update.message.reply_text("Нянь не найдено.")
        return

    lines = [
        f"• {s['user']['name']} — {s['city']}, {s['daily_rate']} KZT/день"
        for s in sitters
    ]
    await update.message.reply_text("\n".join(lines))

def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start",   start))
    app.add_handler(CommandHandler("sitters", sitters))
    app.run_polling()

if __name__ == "__main__":
    main()
