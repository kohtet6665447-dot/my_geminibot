import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import google.generativeai as genai

# API Keys (Render ရဲ့ Environment Variables ကနေ ဖတ်မှာဖြစ်ပါတယ်)
TOKEN = os.environ.get("8539257008:AAHpTyacFj5lULqSKHdFIEh4lczXKkQsnNs")
GEMINI_KEY = os.environ.get("AIzaSyDe8GiUaB6xCg0kdyKtBtpcudxQ4dSyUMc")

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        response = model.generate_content(user_text)
        await update.message.reply_text(response.text)
    except Exception as e:
        print(f"Error: {e}")
        await update.message.reply_text("Error ဖြစ်သွားပါတယ်ခင်ဗျာ။")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    application.run_polling()
  
