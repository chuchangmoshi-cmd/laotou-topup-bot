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
        ["🎮 Top Up"],
        ["💰 Balance"],
        ["📦 My Orders"],
        ["💳 Deposit"],
        ["☎️ Support"]
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

    if text == "🎮 Top Up":

        keyboard = [
            ["🎯 Mobile Legends"],
            ["🎯 PUBG Mobile"],
            ["🎯 Free Fire"],
            ["🔙 Back"]
        ]

        await update.message.reply_text(
            "Select Game:",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    elif text == "🎯 Mobile Legends":

        keyboard = [
            ["💎 56 Diamonds"],
            ["💎 172 Diamonds"],
            ["💎 257 Diamonds"],
            ["🔙 Back"]
        ]

        await update.message.reply_text(
            "Select MLBB Package:",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    elif text == "🎯 PUBG Mobile":

        keyboard = [
            ["🔫 60 UC"],
            ["🔫 325 UC"],
            ["🔫 660 UC"],
            ["🔙 Back"]
        ]

        await update.message.reply_text(
            "Select PUBG Package:",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    elif text == "🎯 Free Fire":

        keyboard = [
            ["💎 100 Diamonds"],
            ["💎 310 Diamonds"],
            ["💎 1060 Diamonds"],
            ["🔙 Back"]
        ]

        await update.message.reply_text(
            "Select Free Fire Package:",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    elif text == "💰 Balance":

        await update.message.reply_text(
            "💰 Your Balance\n\n$0.00"
        )

    elif text == "📦 My Orders":

        await update.message.reply_text(
            "📦 No orders yet."
        )

    elif text == "💳 Deposit":

        await update.message.reply_text(
            "💳 Deposit\n\nPlease contact admin:\n@shoplaotou"
        )

    elif text == "☎️ Support":

        await update.message.reply_text(
            "☎️ Support\n\n@shoplaotou"
        )

    elif text == "💎 56 Diamonds":

        await update.message.reply_text(
            "Please send your MLBB ID"
        )

    elif text == "💎 172 Diamonds":

        await update.message.reply_text(
            "Please send your MLBB ID"
        )

    elif text == "💎 257 Diamonds":

        await update.message.reply_text(
            "Please send your MLBB ID"
        )

    elif text == "🔫 60 UC":

        await update.message.reply_text(
            "Please send your PUBG UID"
        )

    elif text == "🔫 325 UC":

        await update.message.reply_text(
            "Please send your PUBG UID"
        )

    elif text == "🔫 660 UC":

        await update.message.reply_text(
            "Please send your PUBG UID"
        )

    elif text == "💎 100 Diamonds":

        await update.message.reply_text(
            "Please send your Free Fire ID"
        )

    elif text == "💎 310 Diamonds":

        await update.message.reply_text(
            "Please send your Free Fire ID"
        )

    elif text == "💎 1060 Diamonds":

        await update.message.reply_text(
            "Please send your Free Fire ID"
        )

    elif text == "🔙 Back":

        await start(update, context)


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, menu))

    app.run_polling()


if __name__ == "__main__":
    main()
