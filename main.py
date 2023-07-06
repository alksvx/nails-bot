import telebot
from telebot import types, TeleBot

forma = []
design1 = []

bot: TeleBot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def starter(message):
    bot.send_message(message.chat.id, "Привет, это наш маникюр-бот.")

    length = types.ReplyKeyboardMarkup(resize_keyboard=True)
    short = types.KeyboardButton("Короткие")
    length.row(short)
    long = types.KeyboardButton("Длинные")
    length.row(long)

    bot.send_message(message.chat.id, "Выбери длину", reply_markup=length)

    bot.register_next_step_handler(message, form)


def form(message):

    forma.append(message.text)
    form = types.ReplyKeyboardMarkup(resize_keyboard=True)
    square = types.KeyboardButton("Квадратная")
    form.row(square)
    almond = types.KeyboardButton("Миндалевидная")
    form.row(almond)
    pic = open('images/form.jpg', 'rb')
    bot.send_photo(message.chat.id, pic)
    bot.send_message(message.chat.id, 'Выбери форму', reply_markup=form)
    bot.register_next_step_handler(message, color)


def color(message):

    forma.append(message.text)
    colors = types.ReplyKeyboardMarkup(resize_keyboard=True)
    vivid = types.KeyboardButton("Яркий")
    colors.row(vivid)
    nude = types.KeyboardButton("Нюд")
    colors.row(nude)

    bot.send_message(message.chat.id,
                     'Выбери цвет',
                     reply_markup=colors)

    bot.register_next_step_handler(message, design)


def design(message):

    design1.append(message.text)
    design_list = types.ReplyKeyboardMarkup(resize_keyboard=True)
    nope = types.KeyboardButton('Без дизайна')
    design_list.row(nope)
    french = types.KeyboardButton('Френч')
    design_list.row(french)
    glitter = types.KeyboardButton("Блестки")
    design_list.row(glitter)
    hard = types.KeyboardButton("Сложный дизайн")
    design_list.row(hard)

    bot.send_message(message.chat.id, 'Выбери дизайн', reply_markup=design_list)

    bot.register_next_step_handler(message, ready)


def ready(message):
    design1.append(message.text)
    forma_str = "/".join(forma)
    design1_str1 = '.'.join(design1)
    pic = open('images/'+forma_str+'/'+design1_str1+'.jpg', 'rb')
    bot.send_photo(message.chat.id, pic)


bot.polling(none_stop=True)
