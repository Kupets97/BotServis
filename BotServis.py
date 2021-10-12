import telebot
import sqlite3
from telebot import types

TOKEN = '1908684588:AAGxUE8Oj0IYycW-j2tfVXD_uTCNMCXhtTg'

bot = telebot.TeleBot(TOKEN)
chat_id = '534248630'
connect = sqlite3.connect('users1.db', check_same_thread=False)
cursor = connect.cursor()


def db_table_val(user_id: int, user_name: str, user_surname: str,
                 username: str):
    cursor.execute(
        'INSERT OR IGNORE INTO users1 (user_id, user_name, user_surname, '
        'username) VALUES (?, ?, ?, ?)',
        (user_id, user_name, user_surname, username))
    connect.commit()

def db(user_id: int):
    cursor.execute(
        'SELECT user_id FROM users1')
    if cursor.fetchone() is None:
        pass
    else:
        pass
    connect.commit()


def otv(message):
    bot.send_message(message.chat.id,
                     'Такой позьзователь уже существует, ждите ответа мастера.')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, )
    markup.add(types.KeyboardButton('Оставьте заявку мастеру🛠.'))
    markup.add(types.KeyboardButton('Список услуг и цены📋.'))
    markup.add(types.KeyboardButton('Позвоните Мне и Ваша проблема будет решена👨‍🔧.'))

    bot.send_message(message.chat.id,
                     'Приветствую вас в нашей мастерской, {0.first_name}!'.format(
                         message.from_user), reply_markup=markup)

    return markup


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Оставьте заявку мастеру🛠.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Назад⬅️.'))
        bot.forward_message(chat_id, message.chat.id,
                            message.message_id)
        bot.send_message(message.chat.id,
                         'Вы оставили заявку мастеру(приём заявок '
                         'осуществляется один раз), '
                         '\nможете ознакомиться со списком наших услуг при '
                         'нажатии кнопки Назад👇',
                         reply_markup=markup)

        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val(user_id=us_id, user_name=us_name,
                     user_surname=us_sname,
                     username=username)
        db(user_id=us_id)

        return message.text

    elif message.text == 'Список услуг и цены📋.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Ремонт стиральных машин:')
        item2 = types.KeyboardButton('Диагностика:')
        back = types.KeyboardButton('Назад⬅️.')
        markup.add(item1, item2, back)

        bot.send_message(message.chat.id, 'Список доступных услуг:',
                         reply_markup=markup)

    elif message.text == 'Диагностика:':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         'Стоимость диагностики 20 рублей '
                         '\n(оплачивается в случае отказа от ремонта или не '
                         'целесообразности данного). '
                         '\nВ случае ремонта диагностика и выезд мастера '
                         'БЕСПЛАТНО!!!!',
                         reply_markup=markup)

    elif message.text == 'Ремонт стиральных машин:':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         'Ремонт стиральных машин всех марок в Минске.'
                         '\nВыезд и диагностика БЕСПЛАТНО (при условии дальнейшего ремонта)'
                         '\nПроизвожу работы по ремонту стиральных машин:замена '
                         '\nзамена подшипников (гремит,стучит, гудит) от 150 рублей'
                         '\n* замена насоса (нет слива воды,выбивает ошибку) от 70 рублей'
                         '\n* замена щёток электродвигателя (двигатель не хочет крутить барабан, бьёт ошибку, не выходит на отжим) от 70 рублей'
                         '\n* замена ТЭНа (нагревательного элемента) — (выбивает узо, не греется вода, програматор ходит по кругу, зависает время) от 70 рублей.'
                         '\n* замена блокиратора двери (не закрывается люк, дверь) от 50 рублей.'
                         'ремонт электронного блока (запах гари, не включается, выдаёт ошибку) от 80 рублей.'
                         '\n* замена уплотнительной резины — манжеты — люка (подтекает, порвана) от 80 рублей.'
                         '\nремонт электродвигателя (запах гари, нет отжима, слабое вращение барабана) от 70 рублей.'
                         '\n* замена трубок, ручек, клапанов, датчиков температуры, датчиков уровня воды, проводки, лотков, стёкол, шлангов, петли люка и другое от 30 рублей.'
                         '\nМарки ремонтируемых машин :'
                         '\nSamsung (Самсунг), LG (ЛЖ Элджи), Ardo (Ардо), Indesit (Индезит)'
                         '\nHotpoint-Ariston (Хотпоинт Аристон), Bosch (Бош), Zanussi (Занусси)'
                         '\nAEG (АЕГ), Electrolux (Электролюкс), Siemens (Сименс), Candy (Канди)'
                         '\nWhirlpool (Вирпул), Iberna (Иберна), Gorenje (Горенье), Beko (Беко)'
                         '\nHansa (Ханса), Atlant (Атлант), Miele (Милли), Hoover (Хувер)'
                         '\nZerowatt (Зероватт), Bauknecht (Баукхнехт), Fagor (Фагор), Haier (Хаер)'
                         '\nKaiser(Кайзер), NEFF (Нефф), Panasonic (Панасоник), De Dietrich (Де Дитрих)'
                         '\nIT Wash (ИТ Вош, Айти Вош), Korting (Кертинг), Brandt (Бранд)'
                         '\nEurosoba (Еврособа), Hitachi (Хитачи), Kuppersberg (Купперсберг)'
                         '\nKuppersbusch (Купперсбуш), Smeg (Смег), Asko (Аско).'
                         '\nСвяжитесь со мной и я Вам всё разъясню.'
                         '\nЯ ценю каждого клиента.',
                         reply_markup=markup)

    elif message.text == 'Назад⬅️.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('Оставьте заявку мастеру🛠.'))
        markup.add(types.KeyboardButton('Список услуг и цены📋.'))
        markup.add(types.KeyboardButton('Связаться c мастером на прямую👨‍🔧.'))

        bot.send_message(message.chat.id,
                         'Выберете интересующий вас раздел, '
                         '{0.first_name}!'.format(
                             message.from_user), reply_markup=markup)

    elif message.text == 'Позвоните Мне и Ваша проблема будет решена👨‍🔧.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         'Спасибо что обратились в нашу мастерскую, '
                         '{0.first_name}! '
                         '\n Вот номер нашего мастера,'
                         '\n +375293334450 Сергей Леонидович.'
                         .format(
                             message.from_user), reply_markup=markup)


bot.polling(none_stop=True, interval=0)



