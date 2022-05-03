import telebot
import sqlite3

# 5365748188:AAGDOuRfwwAY2UrDMeYLcLsdUQVzBv0uqA4

bot = telebot.TeleBot("5365748188:AAGDOuRfwwAY2UrDMeYLcLsdUQVzBv0uqA4")
name = ''
age = ''


@bot.message_handler(commands=['start', 'Запустить меня'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                     "Привет меня зовут Mialiva🖐. Со мной никто не хочет дружить😞, может ты станешь моим другом? Мы сможем делиться друг с другом "
                     "своими секретами, узнавать как прошел день, и скидывать друг другу милые картиночки с котиками. Ко-о--о-не-чно если ты не против👉👈."
                     "Чтобы не было неловко можем начать общение с обычного Привет, хи-хи ")

    connect = sqlite3.connect('Users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users_id(
        id INTEGER,  
    )""")

    connect.commit()

    ##Добавление данных пользоватлей в базу данных
    user_id = [message.chat.id]
    cursor.execute("INSERT INTO users_id VALUES(?);" , user_id)
    connect.commit()


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, "Приветик, я Mialiva, но мой создатель зовет меня Mia или Мия, "
                                               "ты тоже можешь меня так звать. А тебя как зовут?")
        bot.register_next_step_handler(message, reg_name)


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Блинн, у тебя такое красивое имя, а сколько тебе лет? Мне вот только 1 "
                                           "день, недавно исполнился, но у же большая, правда! И много чего умею!")
    bot.register_next_step_handler(message, reg_age)


def reg_age(message):
    global age
    age = message.text
    bot.send_message(message.from_user.id,
                     "Вау, а ты старше меня, так нечестно, но я еще вырасту и покажу насколько я крутая! Так как еще "
                     "о-о--очень маленькая, я могу забывать некоторые вещи, но ты не обижайся! Мой создатель говорит "
                     "что скоро научит меня запоминать все. "
                     "Но я же правильно помню тебе " + str(
                         age) + " лет, а твое прекрасное имя звучит как " + name + " все верно?👉👈")
    bot.register_next_step_handler(message, reg_call)

    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Я-я-я не понимаю, давай ты попробуешь еще раз?👉👈")


@bot.message_handler(func=lambda m: True)
def reg_call(message):
    if message.text == 'Да' or 'ДА':
        bot.send_message(message.from_user.id, "Так как я еще очень маленькая, я очень мало умею(. Но я очень "
                                               "стараюсь!. Я могу например спеть тебе милую песенку, или сказать "
                                               "комплимент. Чего бы ты хотел?👉👈")


bot.infinity_polling()
