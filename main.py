from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *
import emoji


app = ApplicationBuilder().token("6069726115:AAHc98c_2wpPLRxnS93C5CRwWo7u1zsF2vw").build()
print('Start')

app.add_handler(CommandHandler("start", help_command))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.run_polling()