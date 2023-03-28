
from telebot import types
import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config
import datetime
import datetime
bot = telebot.TeleBot('5621776992:AAGok5yQaVEG-jEgoBsz52HSTPwldeAdhCE')

data_dict = {}

now = datetime.datetime.now()
y, mth, d, h, m, s = now.year, now.month, now.day, now.hour, now.minute, now.second
text = 'STARTING: {} YER, {} MONTH, {} DAY, {} HOUR, {} MIN, {} SEC'
print(text.format(y, mth, d, h, m, s))


@bot.message_handler(commands=['start'])
def starts(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    lang_2 = types.InlineKeyboardButton('Ukrainian🇺🇦', callback_data='uk')
    markup.add(lang_2)

    now = datetime.datetime.now()
    y, mth, d, h, m, s = now.year, now.month, now.day, now.hour, now.minute, now.second
    text = 'Visited: {} yer, {} month, {} day, {} hour, {} min, {} sec'
    
    res = text.format(y, mth, d, h, m, s)

    data_dict[str(message.from_user.first_name)] = res
    print(data_dict)

    bot.send_message(message.chat.id, 'Привіт, '+ str(message.from_user.first_name)+'👋'+'\n\nОбери мову:', reply_markup=markup)

    mor = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key = types.KeyboardButton('/more')
    mor.add(key)
    bot.send_message(message.chat.id, '🔴Більше інформації - /more', reply_markup=mor)


@bot.message_handler(commands=['more'])
def site(message):
    photo = open('fon.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

    markups = types.InlineKeyboardMarkup()
    markups.add(types.InlineKeyboardButton('Instagram', url='https://www.instagram.com/deennill/'))
    bot.send_message(message.chat.id, 'Перейти за посиланням👇', reply_markup=markups)

@bot.callback_query_handler(func=lambda message:True)
def start_lang(call):
    if call.message:
        if call.data == 'uk':

            bot.answer_callback_query(call.id, 'Вибрано Українську🇺🇦')
            
            mark = types.InlineKeyboardMarkup(row_width=1)
            butt_1 = types.InlineKeyboardButton('погода⛅️', callback_data='weath1')
            mark.add(butt_1)
            bot.send_message(call.message.chat.id, 'Привіт, '+ str(call.from_user.first_name)+'👋'+'\n\nЯ Ассі бот, і я маю такy опції як:', reply_markup=mark)

                
        elif call.data == 'weath1':
                
            @bot.message_handler(content_types=['text'])
            def eny(message):
                try:
                    place = message.text
                                                        
                    config_dict = get_default_config()
                    config_dict['language'] = 'uk'
                                                
                    owm = OWM('cab1c46d340e36eca587a8cb7798886b', config_dict)
                    mgr = owm.weather_manager()
                    observation = mgr.weather_at_place(place)
                    w = observation.weather
                                                            
                    t = w.temperature('celsius')
                    t1 = t['temp']
                    t2 = t['feels_like']
                    wi = w.wind()['speed']
                                                            
                    bot.send_message(message.chat.id, 'В місті:  ' + str(place) + '\n\n'
                            'температура: ' + str(t1) + ' °C' + '\n' + 
                            'відчувається: ' + str(t2) + ' °C' + '\n' +
                            'вітер: ' + str(wi) + ' m/s')
                except:
                    bot.send_message(message.chat.id, f'Не знайдено!')
        
        # elif call.data == 'QR':
        #     @bot.message_handler()

bot.polling(none_stop=True, interval=0)