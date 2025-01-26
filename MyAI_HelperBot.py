from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from transformers import pipeline

# Initializing the LLM pipeline
pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

# Command Handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your AI Assistant. Ask me anything!")

# Handler for user messages
async def chat_with_llm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text  # Capture user input
    # Generate response using TinyLlama
    response = pipe(user_message, max_length=150, min_length=150, do_sample=True, temperature=0.5, top_k=50, top_p=0.9)[0]["generated_text"]
    await update.message.reply_text(response)

# Main function
def main():
    TOKEN = "7097598270:AAG-HAUv_hEPZbm2xtAOBCxKHH0nRGD57lY" 

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))  # Handles /start command
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_llm))  # Handles text messages

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
