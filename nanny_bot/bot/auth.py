from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes
from data.database import verify_login, get_nanny

LOGIN_USERNAME, LOGIN_PASSWORD = range(2)

async def login_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введите ваше имя (как указано при регистрации):")
    return LOGIN_USERNAME

async def login_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['login_username'] = update.message.text
    await update.message.reply_text("Введите ваш пароль:")
    return LOGIN_PASSWORD

async def login_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = context.user_data.get('login_username')
    password = update.message.text
    
  
    user_id = verify_login(username, password)
    
    if user_id:
        nanny = get_nanny(user_id)
        
        if nanny:
            context.user_data['logged_in'] = True
            context.user_data['nanny_id'] = user_id
            
            await update.message.reply_text(
                f"🎉 Вы успешно вошли в систему как {nanny['name']}!\n"
                "Используйте /myinfo для просмотра своего профиля\n"
                "Используйте /my_bookings для просмотра ваших заказов"
            )
        else:
            await update.message.reply_text(
                "Произошла ошибка при получении данных профиля."
            )
    else:
        await update.message.reply_text(
            "Неверное имя пользователя или пароль. Попробуйте снова!"
        )
        return LOGIN_USERNAME 
    
    return ConversationHandler.END

async def login_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Вход отменён.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


login_conv = ConversationHandler(
    entry_points=[CommandHandler('login', login_start)],
    states={
        LOGIN_USERNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, login_username)],
        LOGIN_PASSWORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, login_password)]
    },
    fallbacks=[CommandHandler('cancel', login_cancel)]
)



