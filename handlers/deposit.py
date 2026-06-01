from telegram import Update

ADMIN_ID = 7321399891


async def notify_admin(
    update: Update,
    amount: str
):

    user = update.effective_user

    username = user.username or "No Username"

    text = (
        f"💳 New Deposit Request\n\n"
        f"User: @{username}\n"
        f"User ID: {user.id}\n"
        f"Amount: {amount} KS"
    )

    return text
