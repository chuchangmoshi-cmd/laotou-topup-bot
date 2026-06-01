from database import init_db

from handlers.orders import (
    add_order,
    get_orders
)

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

import os

from handlers.deposit import notify_admin, ADMIN_ID
from handlers.balance import (
    get_balance,
    add_balance,
    deduct_balance
)

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

        context.user_data["waiting_screenshot"] = True

        context.user_data["deposit_mode"] = False

        await update.message.reply_text(
            "📸 Please upload payment screenshot."
        )

        return

    # Waiting Screenshot
    if context.user_data.get("waiting_screenshot"):

        if update.message.photo:

            amount = context.user_data.get("deposit_amount")

            user = update.effective_user

            caption = (
                f"💳 New Deposit Request\n\n"
                f"User: @{user.username}\n"
                f"User ID: {user.id}\n"
                f"Amount: {amount} KS"
            )

            photo = update.message.photo[-1].file_id

            keyboard = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "✅ Confirm",
                        callback_data=f"approve:{user.id}:{amount}"
                    ),
                    InlineKeyboardButton(
                        "❌ Reject",
                        callback_data=f"reject:{user.id}:{amount}"
                    )
                ]
            ])

            await context.bot.send_photo(
                chat_id=ADMIN_ID,
                photo=photo,
                caption=caption,
                reply_markup=keyboard
            )

            await update.message.reply_text(
                "✅ Deposit Request Submitted"
            )

            context.user_data["waiting_screenshot"] = False

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

        orders = get_orders(
            update.effective_user.id
        )

        if not orders:

            await update.message.reply_text(
                "📦 No orders yet."
            )

            return

        msg = "📦 Order History\n\n"

        for i, order in enumerate(
            orders,
            start=1
        ):

            msg += (
                f"#{i}\n"
                f"{order['game']}\n"
                f"{order['package']}\n"
                f"{order['price']} 🇲🇲\n"
                f"Status: {order['status']}\n\n"
            )

        await update.message.reply_text(msg)

    elif text == "💳 Deposit":

        await update.message.reply_photo(
            photo="https://raw.githubusercontent.com/chuchangmoshi-cmd/laotou-topup-bot/main/laotouskm.jpg",
            caption=(
                "💳 KBZPay Deposit\n\n"
                "Name: DAW CHWAY SI MEE\n"
                "Number: 09760772941\n\n"
                "Please complete payment first.\n"
                "Then enter deposit amount (KS)."
            )
        )

        context.user_data["deposit_mode"] = True

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

            price_num = int(
                price.replace(" KS", "")
            )

            balance = get_balance(
                update.effective_user.id
            )

            if balance < price_num:

                await update.message.reply_text(
                    f"❌ Insufficient Balance\n\n"
                    f"Current Balance:\n"
                    f"{balance} KS 🇲🇲\n\n"
                    f"Required:\n"
                    f"{price_num} KS 🇲🇲"
                )

                return

                await update.message.reply_text(
                    f"📦 Order Submitted\n\n"
                    f"Game: {game}\n"
                    f"Package: {package}\n"
                    f"Price: {price} 🇲🇲\n"
                    f"Player ID: {text}\n\n"
                    f"Status: Pending"
                )

            add_order(
    update.effective_user.id,
    {
        "game": game,
        "package": package,
        "price": price,
        "uid": text,
        "status": "Pending",
        "user_id": update.effective_user.id
    }
)
            keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "✅ Complete",
            callback_data=f"complete:{update.effective_user.id}:{price}"
        ),
        InlineKeyboardButton(
            "❌ Cancel",
            callback_data=f"cancel:{update.effective_user.id}"
        )
    ]
])

        await context.bot.send_message(
    chat_id=ADMIN_ID,
    text=(
        f"📦 New Order\n\n"
        f"User: @{update.effective_user.username}\n"
        f"User ID: {update.effective_user.id}\n\n"
        f"Game: {game}\n"
        f"Package: {package}\n"
        f"Price: {price}\n"
        f"Player ID: {text}"
    ),
    reply_markup=keyboard
)
        await start(update, context)


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.from_user.id != ADMIN_ID:
        return

    data = query.data

    if data.startswith("approve:"):

        _, user_id, amount = data.split(":")

        user_id = int(user_id)
        amount = int(amount)

        new_balance = add_balance(
            user_id,
            amount
        )

        await context.bot.send_message(
            chat_id=user_id,
            text=(
                f"✅ Deposit Approved\n\n"
                f"Amount: {amount} KS\n\n"
                f"Current Balance: {new_balance} KS"
            )
        )

        await query.edit_message_caption(
            caption=query.message.caption + "\n\n✅ APPROVED"
        )

    elif data.startswith("reject:"):

        _, user_id, amount = data.split(":")

        user_id = int(user_id)

        await context.bot.send_message(
            chat_id=user_id,
            text="❌ Deposit Rejected"
        )

        await query.edit_message_caption(
            caption=query.message.caption + "\n\n❌ REJECTED"
        )

    elif data.startswith("complete:"):

        _, user_id, price = data.split(":")

        user_id = int(user_id)

        amount = int(
            price.replace(" KS", "")
        )

        success = deduct_balance(
            user_id,
            amount
        )

        if not success:

            await context.bot.send_message(
                chat_id=user_id,
                text="❌ Order Failed\n\nInsufficient Balance."
            )

            return

        balance = get_balance(
            user_id
        )

        await context.bot.send_message(
            chat_id=user_id,
            text=(
                f"✅ Order Completed\n\n"
                f"Amount: {amount} KS 🇲🇲\n\n"
                f"Current Balance: {balance} KS 🇲🇲"
            )
        )

        await query.edit_message_text(
            query.message.text + "\n\n✅ COMPLETED"
        )

    elif data.startswith("cancel:"):

        _, user_id = data.split(":")

        user_id = int(user_id)

        await context.bot.send_message(
            chat_id=user_id,
            text="❌ Order Cancelled"
        )

        await query.edit_message_text(
            query.message.text + "\n\n❌ CANCELLED"
        )
        
def main():

    init_db()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT | filters.PHOTO,
            menu
        )
    )

    app.add_handler(
        CallbackQueryHandler(button_callback)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
