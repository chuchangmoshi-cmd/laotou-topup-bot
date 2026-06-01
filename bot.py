from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import os

TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["🎮 MLBB Topup"],
        ["🔫 PUBG UC"],
        ["📦 Check Order"],
        ["👨‍💻 Support"]
    ]

    await update.message.reply_text(
        "🎮 Welcome to LaoTou Topup\n\nChoose a service:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "🎮 MLBB Topup":
        await update.message.reply_text(
            "Please send your MLBB ID"
        )

    elif text == "🔫 PUBG UC":
        await update.message.reply_text(
            "Please send your PUBG UID"
        )

    elif text == "📦 Check Order":
        await update.message.reply_text(
            "Please send your Order ID"
        )

    elif text == "👨‍💻 Support":
        await update.message.reply_text(
            "@shoplaotou"
        )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, menu))

    app.run_polling()


if __name__ == "__main__":
    main()
