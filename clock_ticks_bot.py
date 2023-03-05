# installed pyTelegramBotAPI
import telebot
# import time

KEY_API = '5961703408:AAHLaZKvHtZ3RBRt51fRaGf-Y-mYWsKTJhw'
# creating a bot
bot = telebot.TeleBot(KEY_API)

# message handler zone
@bot.message_handler(commands=['greet'])
def greeting(message):
    bot.send_message(message.chat.id,'Hey there! Welcome to Clock Ticks.')

# @bot.message_handler(commands=['time'])
# def time_is(message):
#     seconds_passed_today = (time.time() + 5.5*3600)%(60*60*24)
#     HH = seconds_passed_today//(3600)
#     MM = (seconds_passed_today - HH*3600)//60
#     SS = (seconds_passed_today - (HH*3600 + MM*60))
#     time_now = f'Time >> {int(HH)} : {int(MM)} : {int(SS)}'
#     bot.send_message(message.chat.id , time_now)

bot.polling()


