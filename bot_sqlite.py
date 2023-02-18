import sqlite3
import telebot
import json
import io
import time

bot = telebot.TeleBot("XXXXX:XXXXX")

def isvn_db():
  pass

@bot.message_handler(commands=['isvn'])
def start(message):
  msg = bot.send_message(message.chat.id, "Введите название станции ИСВН: ")
  bot.register_next_step_handler(msg, show_all_isvn)

def show_all_isvn(message):
  connect = sqlite3.connect('isvn_places.db')
  cursor = connect.cursor()
  mini_text = ((message.text).lower())
  cursor.execute(f'SELECT * FROM isvn WHERE stattion_name is not null AND stattion_name = ?', (mini_text,))
  all_results = cursor.fetchone()
  if not all_results:
    bot.reply_to(message, "Такой станции в базе не найдено, начните заново! /isvn")
  else:
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
   connect.close()

@bot.message_handler(commands=['skpt'])
def start(message):
  msg = bot.send_message(message.chat.id, "Введите название станции СКПТ: ")
  bot.register_next_step_handler(msg, show_all_skpt)

def show_all_skpt(message):
  connect = sqlite3.connect('isvn_places.db')
  cursor = connect.cursor()
  lower_name_station = ((message.text).lower())
  cursor.execute(f'SELECT * FROM skpt WHERE station_name is not null AND station_name = ?', (lower_name_station,))
  all_results = cursor.fetchone()
  if not all_results:
    bot.reply_to(message, "Такой станции в базе не найдено, начните заново! /skpt")
  else:
   result = f"""
        *Код станции:*
        {all_results[0]}
        *Ветка станции:*
        {all_results[1]}
        *Имя станции:*
        {all_results[2]}
        *QTECH:*
        ssh:{all_results[7]}
        *Сервер СПО:*
        rdp:{all_results[5]}
        https://{all_results[5]}/
        *iLo Сервер СПО:*
        http://{all_results[3]}
        *Сервер ВН:*
        ssh:{all_results[6]}
        http://{all_results[6]}:9200/
        *iLo Сервер ВН:*
        http://{all_results[4]}
        *Lantan:*
        http://{all_results[10]}
        *Контроллер:*
        http://{all_results[11]}
        *АРМ:*
        rpd:{all_results[8]}
        *Терминал:*
        ssh:{all_results[9]}
        """
   bot.reply_to(message, result, parse_mode= 'Markdown')
   connect.close()

@bot.message_handler(commands=['where_stk'])
def where_stk(message):
  pass

if __name__ == '__main__':
  while True:
    try:
      bot.polling(none_stop = True)
    except:
      time.sleep(10)
