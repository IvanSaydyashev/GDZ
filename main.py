import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests

isBack, msg, subject, stage = 0, '', '', 0
token = '5008620120:AAG18aU566Sls5K41SdvZ0Jb0z9fRyo62dA'
bot = telebot.TeleBot(token)

urlsrus = ['https://gdz.ru/class-8/russkii_yazik/trostencova-8/', 'https://gdz.ru/class-8/russkii_yazik/barhudarov-8/',
           'https://gdz.ru/class-8/russkii_yazik/razumovskaya-11/', 'https://gdz.ru/class-8/russkii_yazik/rybchenkova/']
urlsalg = ['https://gdz.ru/class-8/algebra/merzlyak/', 'https://gdz.ru/class-8/algebra/makarychev-8/',
           'https://gdz.ru/class-8/algebra/makarychev-uglublennoe-izuchenie/', 'https://gdz.ru/class-8/algebra/merzlyak-polyakov/',
           'https://gdz.ru/class-8/algebra/kolyagin-tkacheva/']
urlsgeom = ['https://gdz.ru/class-8/geometria/atanasyan-8/', 'https://gdz.ru/class-8/geometria/merzlyak/',
            'https://gdz.ru/class-8/geometria/merzlyak-polyakov-uglublennij-uroven/']
urlseng = ['https://gdz.ru/class-8/english/reshebnik-spotlight-8-angliyskiy-v-fokuse-vaulina-yu-e/',
           'https://gdz.ru/class-8/english/reshebnik-enjoy-english-biboletova-2013/', 'https://gdz.ru/class-8/english/kuzovlev-sb8/',
           'https://gdz.ru/class-8/english/afanaseva-miheeva-2008/', 'https://gdz.ru/class-8/english/spotlight-workbook/',
           'https://gdz.ru/class-8/english/activity-book-kuzovlev/', 'https://gdz.ru/class-8/english/activity-book-afanasjeva-miheeva/',
           'https://gdz.ru/class-8/english/gia-spotlight-vaulina/', 'https://gdz.ru/class-8/english/reshebnik-rabochaya-tetrad-enjoy-english-biboletova/']

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
    keyboard = types.InlineKeyboardMarkup()
    markup = types.ReplyKeyboardMarkup()
    backBtn = types.KeyboardButton("Перезапустить бота 👍")
    markup.add(backBtn)
    global msg, stage, subject, isBack
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
        if subject != 'english':
            if subject == 'geometry':
                bot.send_message(call.message.chat.id, 'Введите номер упражнения')
                bot.send_message(call.message.chat.id, 'Если ваш учебник "Мерзляк, Поляков Углубленный уровень" введите'
                                                       ' номер параграфа и номер упражнения')
                bot.send_message(call.message.chat.id, 'Пример: 1.1', reply_markup=markup)
            else:
                bot.send_message(call.message.chat.id, 'Введите номер упражнения', reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, 'Введите номер страницы', reply_markup=markup)
    if stage == 3:
        if call.data == 'back':
            stage = 1
            isBack = 1
            start_message(call.message)
        else:
            isBack = 0
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
        elif subject == 'algebra':
            if call.data == 'alg1':
                url = f'https://gdz.ru/class-8/algebra/merzlyak/{msg}-nom/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'alg2':
                url = f'https://gdz.ru/class-8/algebra/makarychev-8/{msg}-nom/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'alg3':
                url = f'https://gdz.ru/class-8/algebra/makarychev-uglublennoe-izuchenie/{msg}-nom/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'alg4':
                url = f'https://gdz.ru/class-8/algebra/merzlyak-polyakov/{msg}-nom/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'alg5':
                url = f'https://gdz.ru/class-8/algebra/kolyagin-tkacheva/{msg}-nom/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
        elif subject == 'geometry':
            if call.data == 'geom1':
                url = f'https://gdz.ru/class-8/geometria/atanasyan-8/{msg}-task/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'geom2':
                url = f'https://gdz.ru/class-8/geometria/merzlyak/{msg}-nom/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'geom3':
                url = f'https://gdz.ru/class-8/geometria/merzlyak-polyakov-uglublennij-uroven/{msg[0]}-item-{msg[2]}/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
        elif subject == 'english':
            if call.data == 'eng1':
                url = f'https://gdz.ru/class-8/english/reshebnik-spotlight-8-angliyskiy-v-fokuse-vaulina-yu-e/{msg}-s/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'eng2':
                if msg == '27':
                    msg = '26'
                elif msg == '36':
                    msg = '35'
                elif msg == '41':
                    msg = '40'
                elif msg == '67':
                    msg = '66'
                url = f'https://gdz.ru/class-8/english/kuzovlev-sb8/{msg}-s/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'eng3':
                if msg == '49':
                    msg = '48'
                url = f'https://gdz.ru/class-8/english/afanaseva-miheeva-2008/{msg}-s/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'eng4':
                url = f'https://gdz.ru/class-8/english/spotlight-workbook/{msg}-s/'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'eng5':
                if msg == '32':
                    msg = '31'
                elif msg == '80':
                    msg = '79'
                elif msg == '98':
                    msg = '97'
                url = f'https://gdz.ru/class-8/english/activity-book-kuzovlev/{msg}-s'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'eng6':
                url = f'https://gdz.ru/class-8/english/activity-book-afanasjeva-miheeva/{msg}-s'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
            elif call.data == 'eng7':
                if msg == '9':
                    msg = '8'
                elif msg == '11':
                    msg = '10'
                elif msg == '21':
                    msg = '20'
                elif msg == '24':
                    msg = '23'
                elif msg == '31':
                    msg = '30'
                elif msg == '34':
                    msg = '33'
                elif msg == '47':
                    msg = '46'
                elif msg == '58':
                    msg = '57'
                elif msg == '76':
                    msg = '75'
                elif msg == '84':
                    msg = '83'
                elif msg == '87':
                    msg = '86'
                elif msg == '96':
                    msg = '95'
                elif msg == '98':
                    msg = '97'
                elif msg == '101':
                    msg = '100'
                elif msg == '105':
                    msg = '104'
                url = f'https://gdz.ru/class-8/english/gia-spotlight-vaulina/{msg}-s'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, "html.parser")
                imgs = soup.findAll('img')
                for img in imgs:
                    if img.has_attr('src'):
                        if 'tasks' in img['src']:
                            url_image = f'https:{img["src"]}'
                            bot.send_photo(call.message.chat.id, photo=url_image)
        if isBack!=1:
            btnBack = types.InlineKeyboardButton(text='Назад', callback_data='back')
            keyboard.row(btnBack)
            bot.send_message(call.message.chat.id, 'Чтобы вернуться назад нажмите на кнопку', reply_markup=keyboard)
            if subject != 'english':
                if subject == 'geometry':
                    bot.send_message(call.message.chat.id, 'Введите номер упражнения')
                    bot.send_message(call.message.chat.id,
                                     'Если ваш учебник "Мерзляк, Поляков Углубленный уровень" введите'
                                     'номер параграфа и номер упражнения')
                    bot.send_message(call.message.chat.id, 'Пример: 1.1')
                else:
                    bot.send_message(call.message.chat.id, 'Введите номер упражнения')


@bot.message_handler(content_types=['text'])
def main(message):
    global msg, stage, isBack
    msg = message.text
    if msg == "Перезапустить бота 👍":
        start_message(message)
        isBack = 1
    else:
        isBack = 0
    if stage == 2:
        try:
            a = int(msg)
            stage = 3
        except:
            try:
                print(msg[0], msg[2])
                stage = 3
            except:
                pass
    keyboard = types.InlineKeyboardMarkup()
    if isBack != 1:
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
                elif subject == 'algebra':
                    btnalg1 = types.InlineKeyboardButton(text='Мерзляк, Полонский, Якир', callback_data='alg1')
                    btnalg2 = types.InlineKeyboardButton(text='Макарычев, Миндюк, Нешков, Суворова', callback_data='alg2')
                    btnalg3 = types.InlineKeyboardButton(text='Макарычев, Миндюк, Нешков Углубленный уровень', callback_data='alg3')
                    btnalg4 = types.InlineKeyboardButton(text='Мерзляк, Поляков Углубленный уровень', callback_data='alg4')
                    btnalg5 = types.InlineKeyboardButton(text='Колягин, Ткачева, Федорова', callback_data='alg5')
                    keyboard.row(btnalg1)
                    keyboard.row(btnalg2)
                    keyboard.row(btnalg3)
                    keyboard.row(btnalg4)
                    keyboard.row(btnalg5)
                elif subject == 'geometry':
                    btngeom1 = types.InlineKeyboardButton(text='Атанасян, Бутузов', callback_data='geom1')
                    btngeom2 = types.InlineKeyboardButton(text='Мерзляк, Полонский', callback_data='geom2')
                    btngeom3 = types.InlineKeyboardButton(text='Мерзляк, Поляков Углубленный уровень', callback_data='geom3')
                    keyboard.row(btngeom1)
                    keyboard.row(btngeom2)
                    keyboard.row(btngeom3)
                elif subject == 'english':
                    btneng1 = types.InlineKeyboardButton(text='Spotlight 8 Ваулина Ю.Е', callback_data='eng1')
                    btneng2 = types.InlineKeyboardButton(text='Кузовлев, Лапа Учебник Student`s book', callback_data='eng2')
                    btneng3 = types.InlineKeyboardButton(text='English-8 Student`s book. Афанасьева О.В., Михеева, И.В.', callback_data='eng3')
                    btneng4 = types.InlineKeyboardButton(text='рабочая тетрадь Ваулина, Дули', callback_data='eng4')
                    btneng5 = types.InlineKeyboardButton(text='рабочая тетрадь Кузовлев, Перегудова', callback_data='eng5')
                    btneng6 = types.InlineKeyboardButton(text='Activity Book Афанасьева, Михеева', callback_data='eng6')
                    btneng7 = types.InlineKeyboardButton(text='тренировочные упражнения Spotlight 8 Ваулина, Подоляко', callback_data='eng7')
                    keyboard.row(btneng1)
                    keyboard.row(btneng2)
                    keyboard.row(btneng3)
                    keyboard.row(btneng4)
                    keyboard.row(btneng5)
                    keyboard.row(btneng6)
                    keyboard.row(btneng7)
                bot.send_message(message.chat.id, 'Выберите учебник', reply_markup=keyboard)


bot.infinity_polling()
