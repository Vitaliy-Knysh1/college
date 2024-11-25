import telebot
import random
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

token = "7778416994:AAE0dWY2jUI6_X2XsqUeRF7I6EQ0b-fTmcE"

bot = telebot.TeleBot(token=token)


# Handle the /help command
@bot.message_handler(commands=["help"])
def send_help(message):
    help_text = "🥳Вітаємо в Віньєтці міста Луцьк!🥳\nНижче представлені ваші опції для прордовження, ви можете: \n-Дізнатися про історію луцьку,\n-Особисто вибрати популярне місце в місті,\n-або знайти випадкове! \nДля повторного викликання цього повідомлення, напишіть /help"
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Виберати місце!", callback_data="help_thing")
    button_2 = InlineKeyboardButton("Випадкове місце", callback_data="random_thing")
    button_3 = InlineKeyboardButton("Про місто🤔", callback_data="info_thing")

    markup.add(button_1, button_2, button_3)  # Add new button

    bot.send_message(message.chat.id, help_text, reply_markup=markup)


# setup
@bot.callback_query_handler(func=lambda call: call.data == "help_thing")
def handle_placeholder_callback_1(call):
    bot.answer_callback_query(call.id)
    markup = InlineKeyboardMarkup()
    # Creating buttons
    apple_button = InlineKeyboardButton("Замок Любарта", callback_data="apple")
    pear_button = InlineKeyboardButton("Луцький зоопарк", callback_data="pear")
    orange_button = InlineKeyboardButton("Музей Війська", callback_data="orange")
    grapes_button = InlineKeyboardButton("Центральний парк", callback_data="grapes")
    pineapple_button = InlineKeyboardButton("Korsak Art Museum", callback_data="pineapple")
    potato_button = InlineKeyboardButton("Лютеранська кірха", callback_data="potato")

    # Add buttons to markup
    markup.add(apple_button, pear_button, orange_button, grapes_button, pineapple_button, potato_button)

    # Send a message
    bot.send_message(call.message.chat.id, "Виберіть місце про яке хочете дізнатися!", reply_markup=markup)


# Handle random
@bot.callback_query_handler(func=lambda call: call.data == "random_thing")
def handle_random_callback(call):
    bot.answer_callback_query(call.id)
    random_place = random.choice(["apple", "pear", "orange", "grapes", "pineapple", "potato"])

    if random_place == "apple":
        send_apple(call.message)
    elif random_place == "pear":
        send_pear(call.message)
    elif random_place == "orange":
        send_orange(call.message)
    elif random_place == "grapes":
        send_grapes(call.message)
    elif random_place == "pineapple":
        send_pineapple(call.message)
    elif random_place == "potato":
        send_potato(call.message)


# 3rd button
@bot.callback_query_handler(func=lambda call: call.data == "info_thing")
def handle_info(call):
    bot.answer_callback_query(call.id)
    markup = InlineKeyboardMarkup()

    # a
    button_1 = InlineKeyboardButton("Географія", callback_data="send_geo")
    button_2 = InlineKeyboardButton("Детальніше про Історію", callback_data="send_history")
    markup.add(button_1, button_2)

    bot.send_message(call.message.chat.id, "Оберіть розділ:", reply_markup=markup)


# Geography and history
@bot.callback_query_handler(func=lambda call: call.data == "send_geo")
def handle_geo_button(call):
    bot.answer_callback_query(call.id)
    send_geo(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "send_history")
def handle_history_button(call):
    bot.answer_callback_query(call.id)
    send_history(call.message)


# inffo stuff
def send_geo(message):
    image_url = "https://images.app.goo.gl/WNeFgDYV93N6dhxW9"
    bot.send_photo(message.chat.id, image_url, caption="Луцьк розташований на заході України, на річці Стир, що є притокою Прип'яті."
                                                       "Місто знаходиться в центральній частині Волинської області, на відстані близько 160км"
                                                       "на південний захід від Львова та 300 км на захід від Києва. Луцьк розташований на рівнинній території, оточений лісами та водними ресурсами, що сприяє розвитку екологічного туризму.")

def send_history(message):
    image_url = "https://images.app.goo.gl/gP8BoF3HBDaPu2TJA"
    bot.send_photo(message.chat.id, image_url, caption="Луцьк — обласний центр Волині, що відіграє важливу роль в історії України. У XX столітті місто стало частиною Польщі (до 1939 року),"
                                                       " а після приєднання до СРСР у 1939 році було центром Волинської області. Під час Другої світової війни Луцьк зазнав окупації нацистами,"
                                                       " а після війни став частиною Української РСР. Після здобуття Україною незалежності в 1991 році Луцьк став важливим адміністративним і культурним центром."
                                                       " У 2000-х роках місто активно розвивається, зокрема в плані інфраструктури, бізнесу та туризму.")


# buttons
@bot.callback_query_handler(func=lambda call: call.data == "apple")
def handle_apple_button(call):
    send_apple(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "pear")
def handle_pear_button(call):
    send_pear(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "orange")
def handle_orange_button(call):
    send_orange(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "grapes")
def handle_grapes_button(call):
    send_grapes(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "pineapple")
def handle_pineapple_button(call):
    send_pineapple(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "potato")
def handle_potato_button(call):
    send_potato(call.message)


# actual stuff
def send_apple(message):
    apple_image_url = "https://images.app.goo.gl/yxsTpCeT9FLn5MyRA"
    bot.send_photo(message.chat.id, apple_image_url, caption="Луцький замок, або Замок Любарта, є однією з найдавніших та найкраще"
                                                             " збережених фортець України, головним об’єктом заповідника «Старий Луцьк»"
                                                             " і культурним центром міста. Його історія бере початок з Х століття, коли на місці сучасного замку"
                                                             " існувало укріплене поселення, засноване, ймовірно, Володимиром Великим. Вперше згадується в Іпатіївському літописі у 1085 році."
                                                             " Будівництво Верхнього замку почалося у 1350-х роках і тривало до 1430 року. Замок служив резиденцією литовських князів"
                                                             " і пізніше королівської адміністрації. У 1429 році тут відбувся з’їзд європейських монархів, а впродовж століть замок був "
                                                             "важливим політичним, адміністративним і релігійним центром Волині. У XVIII столітті замок почав втрачати свої функції,"
                                                             " а після анексії Волині Російською імперією остаточно занепав. У XIX–XX століттях замок реставрували, і тепер"
                                                             "він відкритий для відвідувачів. У XXI столітті частково відновлено фрагменти Окольного замку.")

def send_pear(message):
    pear_image_url = "https://images.app.goo.gl/jqVYgbbPeGs9Nmpc8"
    bot.send_photo(message.chat.id, pear_image_url, caption="Луцький зоопарк, заснований у 1979 році, розташований на 4 га території Центрального парку Луцька."
                                                            " У зоопарку утримується понад 500 тварин 94 видів, включаючи види, занесені до Червоної книги."
                                                            " Тут є вольєри, контактний зоопарк, ветеринарна клініка, а також проводяться екологічні заходи та свята."
                                                            " У 2015 році зоопарк пройшов масштабну реконструкцію, завдяки якій оновлено вольєри та благоустрій території."
                                                            " З 2017 року він є частиною міжнародної системи Species360.")

def send_orange(message):
    orange_image_url = "https://images.app.goo.gl/PNcjTevsKmZv3DAb7"
    bot.send_photo(message.chat.id, orange_image_url, caption="Волинський регіональний музей українського війська та військової техніки, відкритий у 1999 році,"
                                                              " є єдиним військовим музеєм Західної України. Розташований на території військового містечка"
                                                              " площею 1 га, музей є філією Центрального музею Збройних Сил України. З 2008 року його розвиток"
                                                              " підтримує Міністерство оборони України. У музеї зібрано понад 1000 експонатів, включаючи 74"
                                                              " зразки військової техніки, серед яких авіаційна техніка (Ан-2, Су-24М), бронетехніка"
                                                              " (Т-34-85, БМП-1), артилерія (Д-30, МТ-12), зенітно-ракетні комплекси («Оса», «Стріла-10»)"
                                                              " та оперативно-тактичні ракетні комплекси («Луна-М», «Ельбрус»).")

def send_grapes(message):
    grapes_image_url = "https://images.app.goo.gl/qM25ALoaJ5bhZGQS8"
    bot.send_photo(message.chat.id, grapes_image_url, caption="Центральний парк культури і відпочинку імені Лесі Українки в Луцьку засновано"
                                                              " 1964 року. Площа становить 60 га, розташований між старим і новим центром міста"
                                                              " біля річки Стир. Парк включає тематичні алеї, атракціони, зоопарк, спортивні комплекси"
                                                              ", дитяче містечко, зону відпочинку на воді, дамбу з велопішохідною доріжкою та комерційні"
                                                              " об'єкти. Парк зазнав значних змін із часів заснування: після періоду занепаду в 1990-х"
                                                              " розпочалася його модернізація, включаючи реконструкцію алей, очищення каналів і пляжів"
                                                              ", оновлення атракціонів та облаштування сучасної інфраструктури.")

def send_pineapple(message):
    pineapple_image_url = "https://images.app.goo.gl/dZ9fDkPZJLdKq5Re8"
    bot.send_photo(message.chat.id, pineapple_image_url, caption="Музей сучасного українського мистецтва Корсаків (МСУМК) у Луцьку, заснований у 2018 році,"
                                                                 " є найбільшим в Україні музеєм сучасного мистецтва. Розташований у переобладнаних цехах"
                                                                 " колишнього заводу на території «Адреналін Сіті», він має площу 12 500 м². У колекції понад"
                                                                 " 700 робіт 300 українських митців XX-XXI століть, що представляють різноманітні художні"
                                                                 " напрямки.Музей проводить змінні виставки, освітні програми, дослідницькі проєкти"
                                                                 " («Генеза», «Крок на шляху мистецтва») і фестивалі сучасного мистецтва («ПоліхромА»)."
                                                                 " У його структурі діє музей Миколи Кумановського з експозицією його робіт.Проєкт «Космогонія»"
                                                                 " включає найбільшу картину у світі (2000 м²) художника Петра Антипа, створену у 2022-2024 роках."
                                                                 " Музей активно розвиває мистецьку інфраструктуру і пропагує українське мистецтво.")

def send_potato(message):
    potato_image_url = "https://images.app.goo.gl/vMyNyvTWy5XmGSis6"
    bot.send_photo(message.chat.id, potato_image_url, caption="Лютеранська кірха в Луцьку, побудована в 1906 році в неоготичному стилі,"
                                                              " спочатку служила храмом для німецьких колоністів. Після Другої світової війни"
                                                              " споруда занепала, використовувалася різними установами, а в радянські часи — архівом."
                                                              " У 1991 році кірха була передана громаді баптистів, які провели реставрацію, відновили"
                                                              " зовнішній вигляд і інтер'єр. Сьогодні це пам’ятка архітектури, що належить баптистській"
                                                              " громаді під назвою «Дім Євангелія», із активною місіонерською діяльністю та недільною школою."
                                                              " Лютеранська громада Луцька використовує поруч розташований Будинок пастора."
                                                              " Кірха вирізняється жовтою цегляною кладкою, стрілчастими вікнами, контрфорсами"
                                                              " та 24-метровим шпилем. Вона є важливим архітектурним і естетичним елементом Старого міста Луцька.")


bot.polling(True)
