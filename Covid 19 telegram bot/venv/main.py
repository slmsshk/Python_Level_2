import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='1862942603:AAEzW9QN8u09zBK79PdcUBk2AI2bml1TWaM', use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher

# def hello(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')
    
# hello_handler = CommandHandler('hello', hello)
# dispatcher.add_handler(hello_handler)

updater.start_polling()

# def unknown(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
    
# unknown_handler = MessageHandler(Filters.command, unknown)
# dispatcher.add_handler(unknown_handler)

def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code==200):
        data = response.json()
        date = data['Date'][:10]
        ans = f"Covid 19 Summary (as of {date}): \n";
        
        for attribute, value in data['Global'].items():
            if attribute not in ['NewConfirmed', 'NewDeaths', 'NewRecovered']:
                ans += 'Total ' + attribute[5::].lower() + " : " + str(value) + "\n"
        
        print(ans)
        context.bot.send_message(chat_id=update.effective_chat.id, text=ans)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")

corona_summary_handler = CommandHandler('summary', summary)
dispatcher.add_handler(corona_summary_handler)