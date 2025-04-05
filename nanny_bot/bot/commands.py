from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from data.database import add_user, get_all_nannies, get_nanny, get_owner_bookings, get_nanny_bookings

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id, user.username or user.first_name)
    
    text = (
        f"Привет, {user.first_name}! Я бот для поиска нянь для питомцев.\n\n"
        "Доступные команды:\n"
        " /view_nannies - Просмотреть список нянь\n"
        " /become_nanny - Зарегистрироваться как няня\n"
        " /login - Войти в систему как няня\n"
        " /myinfo - Просмотр информации о себе\n"
        " /my_bookings - Мои заказы\n"
        " /search - Поиск нянь по параметрам\n"
        " /help - Помощь по работе с ботом"
    )
    await update.message.reply_text(text)

async def view_nannies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nannies = get_all_nannies()
    if not nannies:
        await update.message.reply_text("К сожалению, пока нет доступных нянь.")
        return
    
    text = " Список доступных нянь для питомцев:\n\n"
    
    for i, nanny in enumerate(nannies, 1):
        rating_stars = "⭐" * int(nanny['rating']) if nanny['rating'] else "Нет отзывов"
        text += (
            f"{i}. {nanny['name']}, {nanny['city']}\n"
            f"Опыт: {nanny['experience']} лет | Рейтинг: {rating_stars}\n"
            f"Типы питомцев: {', '.join(nanny['pet_types']) if nanny['pet_types'] else 'Все'}\n"
            f"Цена: {nanny['hourly_rate']} ₸/час\n\n"
        )
        
   
        buttons = []
        for i, nanny in enumerate(nannies, 1):
            buttons.append([InlineKeyboardButton(
                f"{nanny['name']} ({nanny['city']})",
                callback_data=f"nanny_{nanny['user_id']}"
            )])
        
        reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.message.reply_text(text, reply_markup=reply_markup)

async def nanny_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    nanny_id = int(query.data.split('_')[1])
    nanny = get_nanny(nanny_id)
    if not nanny:
        await query.edit_message_text("Информация о няне не найдена.")
        return
    
    rating_stars = "⭐" * int(nanny['rating']) if nanny['rating'] else "Нет отзывов"
    text = (
        f"{nanny['name']} из {nanny['city']}\n\n"
        f"Опыт: {nanny['experience']} лет\n"
        f" Рейтинг: {rating_stars}\n"
        f"Типы питомцев: {', '.join(nanny['pet_types']) if nanny['pet_types'] else 'Все'}\n"
        f" Цена: {nanny['hourly_rate']} ₸/час\n\n"
        f" О себе: {nanny['description']}\n\n"
    )
    
    buttons = [
        [InlineKeyboardButton("Забронировать", callback_data=f"book_{nanny_id}")],
        [InlineKeyboardButton(" Назад к списку", callback_data="nannies_list")]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.edit_message_text(text, reply_markup=reply_markup)

async def myinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    user_id = update.effective_user.id
    nanny = get_nanny(user_id)
    
    if nanny:
        rating_stars = "⭐" * int(nanny['rating']) if nanny['rating'] else "Нет отзывов"
        text = (
            f" Информация о тебе:\n\n"
            f"Имя: {nanny['name']}\n"
            f"Город: {nanny['city']}\n"
            f"Опыт: {nanny['experience']} лет\n"
            f"Рейтинг: {rating_stars}\n"
            f"Типы питомцев: {', '.join(nanny['pet_types']) if nanny['pet_types'] else 'Все'}\n"
            f"Цена: {nanny['hourly_rate']} ₸/час\n"
            f"Статус: {'Доступен' if nanny['available'] else 'Недоступен'}\n\n"
            f"О себе: {nanny['description']}\n"
        )
        
        buttons = [
            [InlineKeyboardButton(" Редактировать профиль", callback_data="edit_profile")],
            [InlineKeyboardButton(" Изменить статус", callback_data="toggle_status")]
        ]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        await update.message.reply_text(text, reply_markup=reply_markup)
    else:
        text = "👤 Информация не найдена. Зарегистрируйтесь как няня через /become_nanny."
        await update.message.reply_text(text)

async def my_bookings(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    nanny = get_nanny(user_id)
    
    if nanny:
        bookings = get_nanny_bookings(user_id)
        if not bookings:
            await update.message.reply_text("У вас пока нет заказов.")
            return
        
        text = " Ваши заказы как няни:\n\n"
        
        for booking in bookings:
            start = booking['start_time'].strftime("%d.%m.%Y %H:%M")
            end = booking['end_time'].strftime("%d.%m.%Y %H:%M")
            
            text += (
                f" Заказ #{booking['id']}\n"
                f" Клиент: {booking['owner_name']}\n"
                f" Время: {start} - {end}\n"
                f" Адрес: {booking['address']}\n"
                f" Питомец: {booking['pet_details']}\n"
                f" Статус: {booking['status']}\n\n"
            )
        
        await update.message.reply_text(text)
    else:
        bookings = get_owner_bookings(user_id)
        if not bookings:
            await update.message.reply_text("У вас пока нет заказов. Используйте /view_nannies чтобы найти няню.")
            return
        
        text = "Ваши заказы как владельца питомца:\n\n"
        
        for booking in bookings:
            start = booking['start_time'].strftime("%d.%m.%Y %H:%M")
            end = booking['end_time'].strftime("%d.%m.%Y %H:%M")
            
            text += (
                f" Заказ #{booking['id']}\n"
                f" Няня: {booking['nanny_name']}\n"
                f" Время: {start} - {end}\n"
                f" Адрес: {booking['address']}\n"
                f" Питомец: {booking['pet_details']}\n"
                f" Статус: {booking['status']}\n\n"
            )
        
        await update.message.reply_text(text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help"""
    text = (
        "🐾 Помощь по использованию бота няни для питомцев 🐾\n\n"
        "Для владельцев питомцев:\n"
        "1. Используйте /view_nannies для просмотра доступных нянь\n"
        "2. Нажмите на кнопку с именем няни для просмотра деталей\n"
        "3. Нажмите 'Забронировать' чтобы создать заказ\n"
        "4. Используйте /my_bookings для просмотра ваших заказов\n"
        "5. Используйте /search для поиска нянь по параметрам\n\n"
        
        "Для нянь:\n"
        "1. Используйте /become_nanny для регистрации как няня\n"
        "2. Используйте /login для входа в систему\n"
        "3. Используйте /myinfo для просмотра и редактирования профиля\n"
        "4. Используйте /my_bookings для просмотра ваших заказов\n"
        "5. Нажмите 'Изменить статус' чтобы сделать себя доступным/недоступным\n\n"
        
        "Общие команды:\n"
        "- /start - Начать работу с ботом\n"
        "- /cancel - Отменить текущую операцию\n"
        "- /help - Показать это сообщение"
    )
    await update.message.reply_text(text)