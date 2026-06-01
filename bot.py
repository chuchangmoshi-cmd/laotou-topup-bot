from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import os

from handlers.deposit import notify_admin, ADMIN_ID
from handlers.balance import get_balance

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

    # Deposit Mode
    if context.user_data.get("deposit_mode"):

        amount = text

        context.user_data["deposit_amount"] = amount

        msg = await notify_admin(
            update,
            amount
        )

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=msg
        )

        await update.message.reply_text(
            "✅ Deposit Request Sent"
        )

        context.user_data["deposit_mode"] = False

        return

    # Main Menu
    if text == "🎮 Top Up":

        keyboard = [
            ["🎯 Mobile Legends"],
            ["🎯 PUBG Mobile"],
            ["🔙 Back"]
        ]

        await update.message.reply_text(
            "Select Game:",
            reply_markup=ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True
            )
        )

    elif text == "💰 Balance":

        balance = get_balance(
            update.effective_user.id
        )

        await update.message.reply_text(
            f"💰 Your Balance\n\n{balance} KS"
        )

    elif text == "📦 My Orders":

        await update.message.reply_text(
            "📦 No orders yet."
        )

    elif text == "💳 Deposit":

        context.user_data["deposit_mode"] = True

        await update.message.reply_text(
            "Enter Deposit Amount (KS)"
        )

    elif text == "☎️ Support":

        await update.message.reply_text(
            "@shoplaotou"
        )

    # MLBB
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

    elif text == "💎 56 Diamonds":

        context.user_data["game"] = "MLBB"
        context.user_data["package"] = "56 Diamonds"
        context.user_data["price"] = "3900 KS"

        await update.message.reply_text(
            "Please send your MLBB ID"
        )

    elif text == "💎 172 Diamonds":

        context.user_data["game"] = "MLBB"
        context.user_data["package"] = "172 Diamonds"
        context.user_data["price"] = "10800 KS"

        await update.message.reply_text(
            "Please send your MLBB ID"
        )

    elif text == "💎 257 Diamonds":

        context.user_data["game"] = "MLBB"
        context.user_data["package"] = "257 Diamonds"
        context.user_data["price"] = "15600 KS"

        await update.message.reply_text(
            "Please send your MLBB ID"
        )

    # PUBG
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

    elif text == "🔫 60 UC":

        context.user_data["game"] = "PUBG Mobile"
        context.user_data["package"] = "60 UC"
        context.user_data["price"] = "4000 KS"

        await update.message.reply_text(
            "Please send your PUBG UID"
        )

    elif text == "🔫 325 UC":

        context.user_data["game"] = "PUBG Mobile"
        context.user_data["package"] = "325 UC"
        context.user_data["price"] = "19000 KS"

        await update.message.reply_text(
            "Please send your PUBG UID"
        )

    elif text == "🔫 660 UC":

        context.user_data["game"] = "PUBG Mobile"
        context.user_data["package"] = "660 UC"
        context.user_data["price"] = "38000 KS"

        await update.message.reply_text(
            "Please send your PUBG UID"
        )

    # UID Input
    elif text.isdigit():

        game = context.user_data.get("game")
        package = context.user_data.get("package")
        price = context.user_data.get("price")

        if game and package:

            await update.message.reply_text(
                f"📦 Order Confirmation\n\n"
                f"Game: {game}\n"
                f"Package: {package}\n"
                f"Price: {price}\n"
                f"Player ID: {text}\n\n"
                f"Reply YES to confirm."
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
