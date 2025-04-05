from telegram import Update,ReplyKeyboardRemove

from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes

LOGIN_USERNAME,LOGIN_PASSWORD=range(2)

async def login_start(update:Update,context:ContextTypes.DEFAULT_TYPE):
     if "nanny_info" in context.user_data:
        await update.message.reply_text("Введите ваш логин (например, ваше имя):")
        return LOGIN_USERNAME
     else:
        await update.message.reply_text("Вы не зарегистрированы как няня. Зарегистрируйтесь через /become_nanny.")
        return ConversationHandler.END


async def login_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['login_username'] = update.message.text
    await update.message.reply_text("Введите пароль (в демо-версии используйте '1234'):")
    return LOGIN_PASSWORD

async def login_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    password = update.message.text
    if password == "1234":
        await update.message.reply_text("Вы успешно вошли в систему!")
    else:
        await update.message.reply_text("Неверный пароль. Попробуйте снова или отмените командой /cancel.")
    return ConversationHandler.END


async def login_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Вход отменён.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

login_conv = ConversationHandler(
    entry_points=[CommandHandler('login', login_start)],
    states={
        LOGIN_USERNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, login_username)],
        LOGIN_PASSWORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, login_password)]
    },
    fallbacks=[CommandHandler('cancel', login_cancel)]
)
