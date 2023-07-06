import telebot
from telebot import types, TeleBot
import os, random

forma = []
design1 = []

bot: TeleBot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def starter(message):
    letsgo = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lets = types.KeyboardButton("Погнали")
    letsgo.row(lets)
    bot.send_message(message.chat.id, "Привет, это наш маникюр-бот. Начнем?", reply_markup=letsgo)
    bot.register_next_step_handler(message, size)


def size(message):
    length = types.ReplyKeyboardMarkup(resize_keyboard=True)
    short = types.KeyboardButton("Короткие")
    length.row(short)
    long = types.KeyboardButton("Длинные")
    length.row(long)

    bot.send_message(message.chat.id, "Выбери длину", reply_markup=length)
    bot.register_next_step_handler(message, form)


def form(message):
    global forma
    forma = [message.text]
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

    forma.append(message.text)
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
    design1 = message.text
    forma_str = "/".join(forma)
    design1_str1 = ''.join(design1)
    global allp, cpt

    allp = forma_str + '.' + design1_str1
    cpt = sum([len(files) for r, d, files in os.walk("C:\\Users\\Mikhail\\Downloads\\Нужное\\Ксюша\\Программирование\\PycharmProjects\\nails-bot\\images\\"+allp)])
    if cpt > 1:
        pic = open('images/' + allp + '/' + str(random.randint(1, cpt)) + '.jpg', 'rb')
    else:
        pic = open('images/' + allp + '/1.jpg', 'rb')

    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    more = types.KeyboardButton('Еще!')
    menu.row(more)
    want = types.KeyboardButton('Хочу такие')
    menu.row(want)
    again = types.KeyboardButton("Сначала")
    menu.row(again)
    bot.send_photo(message.chat.id, pic, reply_markup=menu)
    bot.register_next_step_handler(message, menuli)


def menuli(message):
    if message.text == 'Еще!':
        if cpt > 1:
            pic = open('images/' + allp + '/' + str(random.randint(1, cpt)) + '.jpg', 'rb')
        else:
            pic = open('images/' + allp + '/1.jpg', 'rb')
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        more = types.KeyboardButton('Еще!')
        menu.row(more)
        want = types.KeyboardButton('Хочу такие')
        menu.row(want)
        again = types.KeyboardButton("Сначала")
        menu.row(again)
        bot.send_photo(message.chat.id, pic, reply_markup=menu)
        bot.register_next_step_handler(message, menuli)

    elif message.text == 'Хочу такие':
        bot.register_next_step_handler(message, appointment)

    elif message.text == 'Сначала':
        answer = types.ReplyKeyboardMarkup(resize_keyboard=True)
        yes = types.KeyboardButton('Да!')
        answer.row(yes)
        bot.send_message(message.chat.id, 'Точно?', reply_markup=answer)
        bot.register_next_step_handler(message, size)


def appointment(message):
    pass


bot.polling(none_stop=True)

