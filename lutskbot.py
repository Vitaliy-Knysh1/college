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
    placeholder_button_1 = InlineKeyboardButton("Виберати місце!", callback_data="placeholder1")
    placeholder_button_2 = InlineKeyboardButton("Випадкове місце", callback_data="placeholder2")
    placeholder_button_3 = InlineKeyboardButton("Про місто🤔",
                                                callback_data="send_same_image")  # New button to send the same image

    markup.add(placeholder_button_1, placeholder_button_2, placeholder_button_3)  # Add new button

    bot.send_message(message.chat.id, help_text, reply_markup=markup)


# setup
@bot.callback_query_handler(func=lambda call: call.data == "placeholder1")
def handle_placeholder_callback_1(call):
    bot.answer_callback_query(call.id)
    markup = InlineKeyboardMarkup()
    # Creating buttons
    apple_button = InlineKeyboardButton("Apple", callback_data="apple")
    pear_button = InlineKeyboardButton("Pear", callback_data="pear")
    orange_button = InlineKeyboardButton("Orange", callback_data="orange")
    banana_button = InlineKeyboardButton("Banana", callback_data="banana")
    grapes_button = InlineKeyboardButton("Grapes", callback_data="grapes")
    pineapple_button = InlineKeyboardButton("Pineapple", callback_data="pineapple")
    potato_button = InlineKeyboardButton("Potato", callback_data="potato")

    # Add buttons to markup
    markup.add(apple_button, pear_button, orange_button, banana_button, grapes_button, pineapple_button, potato_button)

    # Send a message
    bot.send_message(call.message.chat.id, "Виберіть місце про яке хочете дізнатися!", reply_markup=markup)


# Handle random
@bot.callback_query_handler(func=lambda call: call.data == "placeholder2")
def handle_random_fruit_callback(call):
    bot.answer_callback_query(call.id)
    random_fruit = random.choice(["apple", "pear", "orange", "banana", "grapes", "pineapple", "potato"])

    if random_fruit == "apple":
        send_apple(call.message)
    elif random_fruit == "pear":
        send_pear(call.message)
    elif random_fruit == "orange":
        send_orange(call.message)
    elif random_fruit == "banana":
        send_banana(call.message)
    elif random_fruit == "grapes":
        send_grapes(call.message)
    elif random_fruit == "pineapple":
        send_pineapple(call.message)
    elif random_fruit == "potato":
        send_potato(call.message)


# 3rd button
@bot.callback_query_handler(func=lambda call: call.data == "send_same_image")
def handle_same_image_button(call):
    bot.answer_callback_query(call.id)
    markup = InlineKeyboardMarkup()

    # Add two buttons to send the same image but without further buttons
    button_1 = InlineKeyboardButton("Географія", callback_data="send_same_image_1")
    button_2 = InlineKeyboardButton("Детальніше про Історію", callback_data="send_same_image_2")
    # Add the two buttons to the markup
    markup.add(button_1, button_2)

    # Send a message with the two buttons
    bot.send_message(call.message.chat.id, "aaaa",
                     reply_markup=markup)


# History
@bot.callback_query_handler(func=lambda call: call.data == "Географія")
def handle_same_image_1_button(call):
    bot.answer_callback_query(call.id)
    send_same_image(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "Детальніше про Історію")
def handle_same_image_2_button(call):
    bot.answer_callback_query(call.id)
    send_same_image1(call.message)


# Function to send the same image (you can use any image URL)
def send_same_image(message):
    image_url = "https://images.app.goo.gl/WqTGuyJ8ptpdKT3j7"  # Replace with a valid image URL
    bot.send_photo(message.chat.id, image_url, caption="aaaca")

def send_same_image1(message):
    image_url = "https://images.app.goo.gl/WqTGuyJ8ptpdKT3j7"  # Replace with a valid image URL
    bot.send_photo(message.chat.id, image_url, caption="aaa")


# Handle button press for fruit commands
@bot.callback_query_handler(func=lambda call: call.data == "apple")
def handle_apple_button(call):
    send_apple(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "pear")
def handle_pear_button(call):
    send_pear(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "orange")
def handle_orange_button(call):
    send_orange(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "banana")
def handle_banana_button(call):
    send_banana(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "grapes")
def handle_grapes_button(call):
    send_grapes(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "pineapple")
def handle_pineapple_button(call):
    send_pineapple(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "potato")
def handle_potato_button(call):
    send_potato(call.message)


# Fruit command functions
@bot.message_handler(commands=["apple"])
def send_apple(message):
    apple_image_url = "https://images.app.goo.gl/dDk82bTJY5nnCGcZ6"  # Replace with valid apple image URL
    bot.send_photo(message.chat.id, apple_image_url, caption="Here's an image of an apple!")

@bot.message_handler(commands=["pear"])
def send_pear(message):
    pear_image_url = "https://images.app.goo.gl/WqTGuyJ8ptpdKT3j7"  # Replace with valid pear image URL
    bot.send_photo(message.chat.id, pear_image_url, caption="Here's an image of a pear!")

@bot.message_handler(commands=["orange"])
def send_orange(message):
    orange_image_url = "https://images.app.goo.gl/WqTGuyJ8ptpdKT3j7"  # Replace with valid orange image URL
    bot.send_photo(message.chat.id, orange_image_url, caption="Here's an image of an orange!")

@bot.message_handler(commands=["banana"])
def send_banana(message):
    banana_image_url = "https://images.app.goo.gl/WqTGuyJ8ptpdKT3j7"  # Replace with valid banana image URL
    bot.send_photo(message.chat.id, banana_image_url, caption="Here's an image of a banana!")

@bot.message_handler(commands=["grapes"])
def send_grapes(message):
    grapes_image_url = "https://images.app.goo.gl/WqTGuyJ8ptpdKT3j7"  # Replace with valid grapes image URL
    bot.send_photo(message.chat.id, grapes_image_url, caption="Here's an image of grapes!")

@bot.message_handler(commands=["pineapple"])
def send_pineapple(message):
    pineapple_image_url = "https://images.app.goo.gl/WqTGuyJ8ptpdKT3j7"  # Replace with valid pineapple image URL
    bot.send_photo(message.chat.id, pineapple_image_url, caption="Here's an image of a pineapple!")

@bot.message_handler(commands=["potato"])
def send_potato(message):
    potato_image_url = "https://images.app.goo.gl/WqTGuyJ8ptpdKT3j7"  # Replace with valid potato image URL
    bot.send_photo(message.chat.id, potato_image_url, caption="Here's an image of a potato!")


bot.polling(True)