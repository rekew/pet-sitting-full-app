from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes
from data.database import add_nanny, add_user
import re
(
    BECOME_NANNY_NAME,
    BECOME_NANNY_CITY,
    BECOME_NANNY_EXP,
    BECOME_NANNY_PETS,
    BECOME_NANNY_RATE,
    BECOME_NANNY_DESC,
    BECOME_NANNY_PASSWORD
) = range(7)

async def nanny_registration_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id, user.username or user.first_name)
    
    await update.message.reply_text(
        " Регистрация няни для питомцев \n\n"
        "Введите ваше имя и фамилию:"
    )
    return BECOME_NANNY_NAME

async def nanny_registration_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['nanny_info'] = {}
    context.user_data['nanny_info']['name'] = update.message.text
    
    await update.message.reply_text("Введите ваш город:")
    return BECOME_NANNY_CITY

async def nanny_registration_city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['nanny_info']['city'] = update.message.text
    
    await update.message.reply_text(
        "Введите ваш опыт работы с питомцами (в годах):"
    )
    return BECOME_NANNY_EXP

async def nanny_registration_exp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    experience = update.message.text
    if not experience.isdigit():
        await update.message.reply_text(
            "Пожалуйста, введите число. Например: 2"
        )
        return BECOME_NANNY_EXP
    
    context.user_data['nanny_info']['experience'] = int(experience)
    
    keyboard = [
        ['🐶 Собаки', '🐱 Кошки'],
        ['🐦 Птицы', '🐹 Грызуны'],
        ['🐠 Рыбки', '🦎 Рептилии'],
        ['Все типы питомцев']
    ]
    
    await update.message.reply_text(
        "Выберите типы питомцев, с которыми вы работаете:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )
    return BECOME_NANNY_PETS

async def nanny_registration_pets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pet_choice = update.message.text
    if pet_choice == 'Все типы питомцев':
        pet_types = ['Собаки', 'Кошки', 'Птицы', 'Грызуны', 'Рыбки', 'Рептилии']
    else:
        
        pet_types = [re.sub(r'[^\w\s]', '', pet_choice).strip()]
    
    context.user_data['nanny_info']['pet_types'] = pet_types
    
    await update.message.reply_text(
        "Введите вашу почасовую ставку в тенге (только число):",
        reply_markup=ReplyKeyboardRemove()
    )
    return BECOME_NANNY_RATE

async def nanny_registration_rate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rate = update.message.text
    if not rate.isdigit():
        await update.message.reply_text(
            "Пожалуйста, введите число без символов. Например: 2000"
        )
        return BECOME_NANNY_RATE
    
    context.user_data['nanny_info']['hourly_rate'] = int(rate)
    
    await update.message.reply_text(
        "Опишите ваш опыт и услуги (до 200 символов):"
    )
    return BECOME_NANNY_DESC

async def nanny_registration_desc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    description = update.message.text
    if len(description) > 200:
        await update.message.reply_text(
            "Описание слишком длинное. Пожалуйста, сократите его до 200 символов."
        )
        return BECOME_NANNY_DESC
    
    context.user_data['nanny_info']['description'] = description
    
    await update.message.reply_text(
        "Придумайте пароль для входа в систему:"
    )
    return BECOME_NANNY_PASSWORD

async def nanny_registration_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    password = update.message.text
    if len(password) < 4:
        await update.message.reply_text(
            "Пароль должен содержать минимум 4 символа. Попробуйте еще раз:"
        )
        return BECOME_NANNY_PASSWORD
    
    context.user_data['nanny_info']['password'] = password
    
    add_nanny(update.effective_user.id, context.user_data['nanny_info'])
    
    await update.message.reply_text(
        "🎉 Регистрация успешно завершена! 🎉\n\n"
        "Вы зарегистрированы как няня для питомцев.\n"
        "Используйте /myinfo для просмотра вашего профиля.\n"
        "Используйте /login для входа в систему."
    )
    return ConversationHandler.END

async def nanny_registration_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Регистрация отменена.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


nanny_registration_conv = ConversationHandler(
    entry_points=[CommandHandler('become_nanny', nanny_registration_start)],
    states={
        BECOME_NANNY_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, nanny_registration_name)],
        BECOME_NANNY_CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, nanny_registration_city)],
        BECOME_NANNY_EXP: [MessageHandler(filters.TEXT & ~filters.COMMAND, nanny_registration_exp)],
        BECOME_NANNY_PETS: [MessageHandler(filters.TEXT & ~filters.COMMAND, nanny_registration_pets)],
        BECOME_NANNY_RATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, nanny_registration_rate)],
        BECOME_NANNY_DESC: [MessageHandler(filters.TEXT & ~filters.COMMAND, nanny_registration_desc)],
        BECOME_NANNY_PASSWORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, nanny_registration_password)]
    },
    fallbacks=[CommandHandler('cancel', nanny_registration_cancel)]
)
