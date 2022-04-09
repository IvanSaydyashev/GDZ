import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests

msg, subject, stage = '', '', 0
token = '5008620120:AAG18aU566Sls5K41SdvZ0Jb0z9fRyo62dA'
bot = telebot.TeleBot(token)

urlsrus = ['https://gdz.ru/class-8/russkii_yazik/trostencova-8/', 'https://gdz.ru/class-8/russkii_yazik/barhudarov-8/',
           'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/', 'https://gdz.ru/class-8/russkii_yazik/rybchenkova/']


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup()
    global stage
    stage = 1
    btn1 = types.InlineKeyboardButton(text='Алгебра', callback_data='algebra')
    btn2 = types.InlineKeyboardButton(text='Русский язык', callback_data='rus')
    btn3 = types.InlineKeyboardButton(text='Английский язык', callback_data='english')
    btn4 = types.InlineKeyboardButton(text='Геометрия', callback_data='geometry')
    keyboard.row(btn1)
    keyboard.row(btn2)
    keyboard.row(btn3)
    keyboard.row(btn4)
    bot.send_message(message.chat.id, 'Выберите предмет', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global msg, stage, subject
    if stage == 1:
        if call.data == 'rus':
            subject = 'rus'
        elif call.data == 'algebra':
            subject = 'algebra'
        elif call.data == 'geometry':
            subject = 'geometry'
        elif call.data == 'english':
            subject = 'english'
        stage = 2
        bot.send_message(call.message.chat.id, 'Введите номер упражнения')
    if stage == 3:
        if subject == 'rus':
            if call.data == 'rus1':
                url = f'https://gdz.ru/class-8/russkii_yazik/trostencova-8/{msg}-nom/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'rus2':
                url = f'https://gdz.ru/class-8/russkii_yazik/barhudarov-8/{msg}-nom/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'rus3':
                if int(msg) < 34:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg)}-nom/'
                elif 33 < int(msg) < 63:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg)+1}-nom/'
                elif 62 < int(msg) < 66:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg)+2}-nom/'
                elif 65 < int(msg) < 112:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg) + 3}-nom/'
                elif 111 < int(msg) < 127:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg) + 4}-nom/'
                elif 126 < int(msg) < 200:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg)+5}-nom/'
                elif 199 < int(msg) < 226:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg)+6}-nom/'
                elif 225 < int(msg) < 245:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg) + 7}-nom/'
                elif 244 < int(msg) < 284:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg) + 8}-nom/'
                elif 283 < int(msg) < 322:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg)+9}-nom/'
                elif 321 < int(msg) < 355:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg)+10}-nom/'
                elif 354 < int(msg) < 365:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg) + 11}-nom/'
                elif 364 < int(msg) < 401:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg) + 12}-nom/'
                elif 400 < int(msg) < 418:
                    url = f'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/{int(msg)+13}-nom/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'rus4':
                url = f'https://gdz.ru/class-8/russkii_yazik/rybchenkova/{msg}-nom/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
        bot.send_message(call.message.chat.id, 'Введите номер упражнения')
        bot.send_message(call.message.chat.id, 'Чтобы вернуться назад введите "назад"')


@bot.message_handler(content_types=['text'])
def main(message):
    global msg, stage
    msg = message.text
    if stage == 2:
        try:
            a = int(msg)
            stage = 3
        except:
            pass
    keyboard = types.InlineKeyboardMarkup()
    if stage == 1:
        btn1 = types.InlineKeyboardButton(text='Алгебра', callback_data='algebra')
        btn2 = types.InlineKeyboardButton(text='Русский язык', callback_data='rus')
        btn3 = types.InlineKeyboardButton(text='Английский язык', callback_data='english')
        btn4 = types.InlineKeyboardButton(text='Геометрия', callback_data='geometry')
        keyboard.row(btn1)
        keyboard.row(btn2)
        keyboard.row(btn3)
        keyboard.row(btn4)
        bot.send_message(message.chat.id, 'Выберите предмет', reply_markup=keyboard)
    elif stage == 3:
        if msg == 'назад' or msg == 'Назад' or msg == 'НАЗАД':
            stage = 1
            start_message(message)
        if stage == 3:
            if subject == 'rus':
                btnrus1 = types.InlineKeyboardButton(text='Тростнецова, Ладыженская', callback_data='rus1')
                btnrus2 = types.InlineKeyboardButton(text='Бархударов, Крючков', callback_data='rus2')
                btnrus3 = types.InlineKeyboardButton(text='Разумовская, Львова, Капинос', callback_data='rus3')
                btnrus4 = types.InlineKeyboardButton(text='Рыбченкова', callback_data='rus4')
                keyboard.row(btnrus1)
                keyboard.row(btnrus2)
                keyboard.row(btnrus3)
                keyboard.row(btnrus4)
            bot.send_message(message.chat.id, 'Выберите учебник', reply_markup=keyboard)


bot.infinity_polling()
