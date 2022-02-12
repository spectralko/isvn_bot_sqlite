import sqlite3
import telebot
import json
import io
import time

bot = telebot.TeleBot("xxxxxxxxxxxxxxxxxxxxx")

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
  all_results = cursor.fetchone()
  result = f"""
*Ветка станции:* {all_results[2]}
*Имя станции:* {all_results[1]}
*ШТК:* {all_results[3]}
*ШТК-Комби:* {all_results[4]}
*ИБП:* {all_results[5]}
*Шкаф вестибюльный 1:* {all_results[6]}
*Шкаф вестибюльный 2:* {all_results[7]}
*Шкаф вестибюльный 3:* {all_results[8]}
*Шкаф вестибюльный 4:* {all_results[9]}
*Шкаф вестибюльный 5:* {all_results[10]}
*АРМ:* {all_results[11]}
*Комментарий:* {all_results[12]}
            """
  bot.reply_to(message, result, parse_mode= 'Markdown')

@bot.message_handler(commands=['where_stk'])
def where_stk(message):
  pass

if __name__ == '__main__':
  while True:
    try:
      bot.polling(none_stop = True)
    except:
      time.sleep(10)
