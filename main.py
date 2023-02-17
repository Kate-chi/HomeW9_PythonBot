from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from bot_command import *


app = ApplicationBuilder().token("").build()
print('Start')

app.add_handler(CommandHandler("start", help_command))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("D2NY", dayToNewYear))
app.run_polling()