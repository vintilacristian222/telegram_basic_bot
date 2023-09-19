import os
import telebot
import schedule
import time
import threading
import datetime
import chirie2

bot = telebot.TeleBot(chirie2.botToken)
@bot.message_handler(commands=['excel'])
def send_welcome(message):
    bot.reply_to(message, chirie2.excelLink)

@bot.message_handler(commands=['folder'])
def send_welcome(message):
    bot.reply_to(message, chirie2.GoogleDriveFolder)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# send the messages to a specific date and time
def send_message(messageText):
    bot.send_message(chirie2.chatId, messageText)

def job_for_messageText(day, message):
    if datetime.datetime.now().day == day:
        send_message(message)


# Schedule the tasks
schedule.every().day.at("10:00").do(job_for_messageText, chirie2.day1, chirie2.messageText1)
schedule.every().day.at("10:00").do(job_for_messageText, chirie2.day2, chirie2.messageText2)
schedule.every().day.at("10:00").do(job_for_messageText, chirie2.day3, chirie2.messageText3)

def run_bot():
    bot.infinity_polling()

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Run bot and scheduler on separate threads
    t1 = threading.Thread(target=run_bot)
    t2 = threading.Thread(target=run_schedule)
    
    t1.start()
    t2.start()
