from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

BASE_DIR = os.path.dirname(__file__)

# Reply Keyboard
reply_keyboard = ReplyKeyboardMarkup(
    [
        ["📈 What is the Multiplier"],
        ["⚡ Game Mechanics"],
        ["🧠 Tips & Strategy"]
    ],
    resize_keyboard=True
)

# CTA Buttons
def get_cta():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Join our Channel", url="https://t.me/+0w50dyQLSwExN2U9")],
        [InlineKeyboardButton("Download the Aviator Guide", url="https://www.thegambler.co.za/wp-content/uploads/2022/05/Aviator-PDF-11_compressed.pdf")]
    ])

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=open(os.path.join(BASE_DIR, "start.jpg"), "rb"),
        caption="""✈️ Aviator Game Guide

Aviator is a reaction-based game.

A plane takes off and a number increases.
Your goal is to stop at the right moment before the round ends.

How a round works:
1. Join the round
2. The plane takes off
3. The multiplier increases
4. The round ends randomly
""",
        reply_markup=get_cta()
    )

    await update.message.reply_text(
        "👇",
        reply_markup=reply_keyboard
    )

# MULTIPLIER
async def multiplier(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=open(os.path.join(BASE_DIR, "multiplier.jpg"), "rb"),
        caption="""The multiplier is a number that grows during the round.

Example:
1.00 → 1.50 → 2.00 → 5.00

The longer the round lasts — the higher the number.
Higher values are harder to reach.""",
        reply_markup=get_cta()
    )

# MECHANICS
async def mechanics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=open(os.path.join(BASE_DIR, "mechanics.jpg"), "rb"),
        caption="""Each round is generated randomly.

✔️ Every round is independent  
✔️ Previous rounds don't affect next results  
✔️ Results cannot be predicted""",
        reply_markup=get_cta()
    )

# TIPS
async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=open(os.path.join(BASE_DIR, "tips.jpg"), "rb"),
        caption="""Players use different approaches:

- Early stop — faster results  
- Balanced timing — moderate risk  
- Late stop — high difficulty  

There is no guaranteed outcome.""",
        reply_markup=get_cta()
    )

# MESSAGE ROUTER
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "Multiplier" in text:
        await multiplier(update, context)

    elif "Mechanics" in text:
        await mechanics(update, context)

    elif "Tips" in text:
        await tips(update, context)

    else:
        await start(update, context)

# MAIN
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()