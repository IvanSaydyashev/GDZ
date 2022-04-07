import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests

msg = ''
token = '5008620120:AAG18aU566Sls5K41SdvZ0Jb0z9fRyo62dA'
bot = telebot.TeleBot(token)

urlsrus = ['https://gdz.ru/class-8/russkii_yazik/trostencova-8/', 'https://gdz.ru/class-8/russkii_yazik/barhudarov-8/',
           'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/', 'https://gdz.ru/class-8/russkii_yazik/rybchenkova/']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Введите номер упражнения')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global msg
    if call.data == 'rus1':
        print(msg)
        url = f'https://gdz.ru/class-8/russkii_yazik/trostencova-8/{msg}-nom/'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        imgs = soup.findAll('img')
        for img in imgs:
            if img.has_attr('src'):
                if 'tasks' in img['src']:
                    url_image = f'https:{img["src"]}'
                    bot.send_photo(call.message.chat.id, photo=url_image)


@bot.message_handler(content_types=['text'])
def main(message):
    global msg
    msg = message.text
    keyboard = types.InlineKeyboardMarkup()
    btnrus1 = types.InlineKeyboardButton(text='Тростнецова, Ладыженская', callback_data='rus1')
    btnrus2 = types.InlineKeyboardButton(text='Бархударов, Крючков', callback_data='rus2')
    btnrus3 = types.InlineKeyboardButton(text='Разумовская, Львова, Капинос', callback_data='rus3')
    btnrus4 = types.InlineKeyboardButton(text='Рыбченкова', callback_data='rus4')
    keyboard.add(btnrus1, btnrus2, btnrus3, btnrus4)
    bot.send_message(message.chat.id, 'Выберите учебник', reply_markup=keyboard)

bot.infinity_polling()
