import sqlite3
import telebot
import json
import io

bot = telebot.TeleBot("xx")


#connect = sqlite3.connect('isvn_places.db')
#cursor = connect.cursor()


def isvn_db():
  pass


@bot.message_handler(commands=['start'])
def start(message):
  msg = bot.send_message(message.chat.id, "Введите название станции: ")
  bot.register_next_step_handler(msg, show_all)

def show_all(message):
  connect = sqlite3.connect('isvn_places.db')
  cursor = connect.cursor()
  cursor.execute(f'SELECT * FROM isvn WHERE station_id = ?', (message.text,))
  all_results = cursor.fetchall()
  print(all_results)
  result = all_results.encode('utf-8')
  bot.reply_to(message, io.StringIO(result))





@bot.message_handler(commands=['where_stk'])
def where_stk(message):
  pass



if __name__ == '__main__':
  while True:
    try:
      bot.polling(none_stop = True)
    except:
      time.sleep(10)
