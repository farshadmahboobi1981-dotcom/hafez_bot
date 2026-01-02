import os
import random
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQuery_handler, ContextTypes

# لود کردن دیتابیس حافظ
with open('hafez_db.json', 'r', encoding='utf-8') as f:
    hafez_data = json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📿 نیت کردم (دریافت فال)", callback_data='get_fal')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("به ربات فال حافظ خوش آمدید. نیت کنید و دکمه را بزنید:", reply_markup=reply_markup)

async def handle_fal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    # انتخاب تصادفی
    fal = random.choice(hafez_data)
    
    response = f"📜 **غزل شماره {fal['id']}**\n\n{fal['text']}\n\n✨ **تعبیر:**\n{fal['interpretation']}"
    
    await query.edit_message_text(text=response, parse_mode='Markdown')

if __name__ == '__main__':
    # توکن را از محیط سیستم (Environment Variable) می‌گیریم
    TOKEN = os.getenv("BOT_TOKEN")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQuery_handler(handle_fal, pattern='get_fal'))
    app.run_polling()
