
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes
from data.database import get_all_nannies
SEARCH_CITY, SEARCH_PET_TYPE, SEARCH_MIN_RATING = range(3)

async def search_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'search_params' in context.user_data:
        del context.user_data['search_params']
    
    context.user_data['search_params'] = {}

    keyboard = [
        ['Алматы', 'Астана'],
        ['Шымкент', 'Караганда','Oскемен'],
        ['Везде (любой город)']
    ]
    
    await update.message.reply_text(
        "🔍 Поиск нянь для питомцев\n\n"
        "Выберите город или введите свой:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )
    return SEARCH_CITY

async def search_city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text
    
    if city != 'Везде (любой город)':
        context.user_data['search_params']['city'] = city
    
    keyboard = [
        ['🐶 Собаки', '🐱 Кошки'],
        ['🐦 Птицы', '🐹 Грызуны'],
        ['🐠 Рыбки', '🦎 Рептилии'],
        ['Любой питомец']
    ]
    
    await update.message.reply_text(
        "Выберите тип питомца:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )
    return SEARCH_PET_TYPE

async def search_pet_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pet_choice = update.message.text
    
    if pet_choice != 'Любой питомец':
        pet_type = pet_choice.split()[-1]
        context.user_data['search_params']['pet_type'] = pet_type
    
   
    keyboard = [
        ['⭐⭐⭐⭐⭐ (5)', '⭐⭐⭐⭐ (4+)'],
        ['⭐⭐⭐ (3+)', '⭐⭐ (2+)'],
        ['Любой рейтинг']
    ]
    
    await update.message.reply_text(
        "Выберите минимальный рейтинг няни:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )
    return SEARCH_MIN_RATING

async def search_min_rating(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rating_choice = update.message.text
    if 'Любой рейтинг' not in rating_choice:
        if '(5)' in rating_choice:
            min_rating = 5.0
        elif '(4+)' in rating_choice:
            min_rating = 4.0
        elif '(3+)' in rating_choice:
            min_rating = 3.0
        elif '(2+)' in rating_choice:
            min_rating = 2.0
        else:
            min_rating = 0.0
        
        context.user_data['search_params']['min_rating'] = min_rating
    search_params = context.user_data['search_params']
    city = search_params.get('city')
    pet_type = search_params.get('pet_type')
    min_rating = search_params.get('min_rating')
    
    nannies = get_all_nannies(city, pet_type, min_rating)
    
    if not nannies:
        await update.message.reply_text(
            "🔍 По вашему запросу нянь не найдено.\n"
            "Попробуйте изменить параметры поиска командой /search.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END
    

    text = "🔍 Результаты поиска нянь:\n\n"
    
    for i, nanny in enumerate(nannies, 1):
        rating_stars = "⭐" * int(nanny['rating']) if nanny['rating'] else "Нет отзывов"
        text += (
            f"{i}. {nanny['name']}, {nanny['city']}\n"
            f"   Опыт: {nanny['experience']} лет | Рейтинг: {rating_stars}\n"
            f"   🐾 Типы питомцев: {', '.join(nanny['pet_types']) if nanny['pet_types'] else 'Все'}\n"
            f"   💰 Цена: {nanny['hourly_rate']} ₸/час\n\n"
        )
    
    buttons = []
    for i, nanny in enumerate(nannies, 1):
        buttons.append([InlineKeyboardButton(
            f"{nanny['name']} ({nanny['city']})",
            callback_data=f"nanny_{nanny['user_id']}"
        )])
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.message.reply_text(
        text,
        reply_markup=reply_markup,
        reply_to_message=ReplyKeyboardRemove()
    )
    
    return ConversationHandler.END

async def search_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Поиск отменен.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


search_conv = ConversationHandler(
    entry_points=[CommandHandler('search', search_start)],
    states={
        SEARCH_CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, search_city)],
        SEARCH_PET_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, search_pet_type)],
        SEARCH_MIN_RATING: [MessageHandler(filters.TEXT & ~filters.COMMAND, search_min_rating)]
    },
    fallbacks=[CommandHandler('cancel', search_cancel)]
)