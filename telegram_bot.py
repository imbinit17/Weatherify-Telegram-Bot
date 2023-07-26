from telegram.ext import *
import connection
from keep_alive import keep_alive
import os

def start(update,context):
    global user_name
    user_name = update.effective_user.first_name
    startMessage = "\nThis is @weatherify_bot .\nWeatherify Bot is a telegram bot aimed at delivering weather updates and forecasts seamlessly .\n\nEnter a location to get weather updates . \n \nEnter /help for more commands ."
    update.message.reply_text(f"Hi {user_name}"+startMessage)
    
def developer(update,context):
    update.message.reply_text("www.github.com/imbinit17")                            


def contribute(update,context):
    contributeMsg = 'Contribute to the project at : \n\nhttps://github.com/imbinit17/Weatherify-Telegram-Bot'
    update.message.reply_text(contributeMsg)

def discord(update,context):
    update.message.reply_text("We would be thrilled to have you in our server !\nJoin Apna Dimscord from the link below \n\nhttps://discord.gg/feK2aVXbXK")

def help(update,context):
    helpMsg = ''' Type in a location to get its weather forecast here ....

Following are the commands of the weatherify bot :-
/start : Starts the bot
/help : Brings about a help menu
/developer : Developer Info
/contribute : Get the source code for this project..Github Repository Link
/discord : Discord Server Link

Thank You !
'''
    update.message.reply_text(helpMsg)

def sendWeatherUpdates(update,context):
    update.message.reply_text("Please Wait.....fetching data")
    data = connection.getData(update.message.text)
    response = connection.dataProcessing(data)
    if(response[2]==True):
        update.message.reply_text(response[0])
        update.message.reply_text(response[1])
    else:
        update.message.reply_text(response[0])

def main():
    api = os.environ.get("TELEGRAM_KEY")
    updater = Updater(api, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    
    #dp.add_handler(CommandHandler('about', aboutBot))
    dp.add_handler(CommandHandler('developer', developer))
    dp.add_handler(CommandHandler('discord', discord))
    dp.add_handler(CommandHandler('contribute', contribute))
    dp.add_handler(MessageHandler(Filters.text, sendWeatherUpdates))
    updater.start_polling()
    updater.idle()
    keep_alive()


if __name__ == '__main__':
    main()
