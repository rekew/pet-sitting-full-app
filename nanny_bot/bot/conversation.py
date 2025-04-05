from telegram import Update,ReplyKeyboardRemove

from telegram.ext import CommandHandler,ConversationHandler,MessageHandler,filters,ContextTypes


BECOME_NANNY_NAME,BECOME_NANNY_CITY,BECOME_NANNY_EXP=range(3)

async def nanny_regestarion_start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Регистрация няни:\nВведите ваше имя:")

    return BECOME_NANNY_NAME

async def nanny_regestration_name(update:Update,context:ContextTypes.DEFAULT_TYPE):
    context.user_data['nanny_info']={}

    context.user_data['nanny_info']['name']=update.message.text

    await update.message.reply_text("Ввведите ваш город:")
    return BECOME_NANNY_CITY

async def nanny_regestration_city(update:Update,context:ContextTypes.DEFAULT_TYPE):
    context.user_data['nanny_info']['city']=update.message.text
    await update.message.reply_text("Введите ваш опыт работы (в годах):")
    return BECOME_NANNY_EXP

async def nanny_regestration_exp(update:Update,context:ContextTypes.DEFAULT_TYPE):
    context.user_data['nanny_info']['experience']=update.message.text
    await update.message.reply_text("Регистрация завершена! Вы зарегистрированы как няня.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

async def nanny_regestration_cancel(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Регистрация отменена.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

nanny_registration_conv = ConversationHandler(
    entry_points=[CommandHandler('become_nanny', nanny_regestarion_start)],
    states={
        BECOME_NANNY_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, nanny_regestration_name)],
        BECOME_NANNY_CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, nanny_regestration_city)],
        BECOME_NANNY_EXP: [MessageHandler(filters.TEXT & ~filters.COMMAND, nanny_regestration_exp)]
    },
    fallbacks=[CommandHandler('cancel', nanny_regestration_cancel)]
)