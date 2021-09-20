import telebot
import sqlite3, datetime
from telebot import types


TOKEN = '1908684588:AAGxUE8Oj0IYycW-j2tfVXD_uTCNMCXhtTg'

bot = telebot.TeleBot(TOKEN)
chat_id = '534248630'
#grup_url = 'https://t.me/joinchat/LYpw-68R1iFmZjAy'


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Оставьте заявку мастеру🛠.'),
               types.KeyboardButton('Список услуг и цены📋.'))

    bot.send_message(message.chat.id,
                     'Приветствую вас в нашей мастерской, {0.first_name}!'.format(
                         message.from_user), reply_markup=markup)
    return markup


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Оставьте заявку мастеру🛠.':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад⬅️.')
            markup.add(back)
            bot.forward_message(chat_id, message.chat.id,
                                message.message_id)
            bot.send_message(message.chat.id, 'Вы оставили заявку мастеру(приём заявок осуществляется один раз),'
                                              ' можете ознакомиться со списком наших услуг при нажатии кнопки Назад👇',
                             reply_markup=markup)

            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()

            cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
                            name INTEGER
                            )""")

            connect.commit()

            people_id = message.chat.id

            cursor.execute(f"SELECT name FROM login_id WHERE name = {people_id}")
            data = cursor.fetchone()
            if data is None:
                first_name = [message.chat.first_name]
                # user_name = [message.from_user.username]
                cursor.execute("INSERT INTO login_id VALUES(?);", first_name)
                connect.commit()
            else:
                bot.send_message(message.chat.id,
                                 'Ваша заявка находится в обработке, ждите ответа.')
            connect.close()

        elif message.text == 'Список услуг и цены📋.':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Ремонт стиральных машин:')
            item2 = types.KeyboardButton('Диагностика:')
            back = types.KeyboardButton('Назад⬅️.')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Список доступных услуг:', reply_markup=markup)

        elif message.text == 'Диагностика:':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id,
            'Стоимость диагностики 20 рублей '
            '\n(оплачивается в случае отказа от ремонта или не целесообразности данного). '
            '\nВ случае ремонта диагностика и выезд мастера БЕСПЛАТНО!!!!',
                             reply_markup=markup)

        elif message.text == 'Ремонт стиральных машин:':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Ремонт стиральных машин всех марок в Минске.'
                             '\nВыезд и диагностика БЕСПЛАТНО (при условии дальнейшего ремонта)'
                             '\nПроизвожу работы по ремонту стиральных машин:замена '
                             '\nподшипников (гремит,стучит, гудит)'
                             '\n* замена насоса (нет слива воды,выбивает ошибку)'
                             '\n* замена щёток электродвигателя (двигатель не хочет крутить барабан, бьёт ошибку, не выходит на отжим)'
                             '\n* замена ТЭНа (нагревательного элемента) — (выбивает узо, не греется вода, програматор ходит по кругу, зависает время)'
                             '\n* замена блокиратора двери (не закрывается люк, дверь)'
                             'ремонт электронного блока (запах гари, не включается, выдаёт ошибку)'
                             '\n* замена уплотнительной резины — манжеты — люка (подтекает, порвана)'
                             '\nремонт электродвигателя (запах гари, нет отжима, слабое вращение барабана)'
                             '\n* замена трубок, ручек, клапанов, датчиков температуры, датчиков уровня воды, проводки, лотков, стёкол, шлангов, петли люка и другое.'
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
            item1 = types.KeyboardButton('Оставить заявку мастеру🛠.')
            item2 = types.KeyboardButton('Список услуг и цены📋.')

            markup.add(item1, item2)

            bot.send_message(message.chat.id,
                             'Выберете интересующий вас раздел, {0.first_name}!'.format(
                                 message.from_user), reply_markup=markup)


bot.polling(none_stop=True, interval=0)



