from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "ТВОЙ_ТОКЕН_ЗДЕСЬ"
AUDIO_PATH = "orc_alarm.mp3"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🔥 Разбуди меня!", callback_data='wake_up')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("ХРРРР! Орк на страже твоего сна. Жми кнопку — и звук сотрясёт твои уши! 🪓", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'wake_up':
        await query.message.reply_audio(audio=open(AUDIO_PATH, 'rb'), caption="🔔 Орочий будильник тебя зовёт!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот запущен. СЛАВА ВОЖДЮ!")
    app.run_polling()