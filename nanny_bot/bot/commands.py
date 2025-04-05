from telegram import Update 
from telegram.ext import ContextTypes 

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
     text = (
        "Привет! Я бот для поиска нянь.\n\n"
        "Доступные команды:\n"
        "/view_nannies - Просмотреть список нянь\n"
        "/become_nanny - Зарегистрироваться как няня\n"
        "/login - Войти в систему\n"
        "/myinfo - Просмотр информации о себе\n"
    )
     await update.message.reply_text(text)


async def view_nannies(update:Update,context:ContextTypes.DEFAULT_TYPE):
     text=(
           "Список доступных нянь:\n"
        "1. Анара, Алматы\n"
        "2. Назерке, Астана\n"
        "3. Рустем, Алматы"
     )
     await update.message.reply_text(text)


async def myinfo(update:Update,context:ContextTypes.DEFAULT_TYPE):
    user_data = context.user_data
    if "nanny_info" in user_data:
        info = user_data["nanny_info"]
        text = (
            f"Информация о тебе:\n"
            f"Имя: {info.get('name', 'Не указано')}\n"
            f"Город: {info.get('city', 'Не указан')}\n"
            f"Опыт: {info.get('experience', 'Не указан')} лет"
        )
    else:
        text = "Информация не найдена. Зарегистрируйся через /become_nanny."
    await update.message.reply_text(text)
