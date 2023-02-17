from telegram import Update
from telegram.ext import ContextTypes
import datetime
import emoji
import DayToNewYear

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/D2NY')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.datetime.now()}')

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(emoji.emojize(f'Привет {update.effective_user.first_name} :green_heart:'))

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    a = int(items[1])
    b = int(items[2])
    await update.message.reply_text(a+b)

async def dayToNewYear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{DayToNewYear.daysToNewYear()}')