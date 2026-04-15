from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in users:
        users[user_id] = {"credits": 2}

    await update.message.reply_text("🔥 Bot actif\n\n/search pour tester")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = users[update.effective_user.id]

    if user["credits"] <= 0:
        await update.message.reply_text("🔒 Plus de crédits")
        return

    user["credits"] -= 1
    await update.message.reply_text(f"Résultat test\nCrédits: {user['credits']}")

app = ApplicationBuilder().token("TON_TOKEN").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("search", search))

app.run_polling()
