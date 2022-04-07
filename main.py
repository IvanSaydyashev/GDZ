import telebot
from bs4 import BeautifulSoup
import requests

token = '5008620120:AAG18aU566Sls5K41SdvZ0Jb0z9fRyo62dA'
bot = telebot.TeleBot(token)

url = 'https://gdz.ru/class-8/russkii_yazik/trostencova-8/'
page = requests.get(url)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Введите номер упражнения')


@bot.message_handler(content_types=['text'])
def main(message):
    global url, page
    url = f'https://gdz.ru/class-8/russkii_yazik/trostencova-8/{message.text}-nom/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    imgs = soup.findAll('img')
    for img in imgs:
        if img.has_attr('src'):
            if 'tasks' in img['src']:
                url_image = f'https:{img["src"]}'
                bot.send_photo(message.chat.id, photo=url_image)
    bot.send_message(message.chat.id, 'Введите номер упражнения')
bot.infinity_polling()
