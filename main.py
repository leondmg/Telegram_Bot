import telebot
import constants
import cv2
import os
import numpy as np

bot = telebot.TeleBot(constants.token)
upd = bot.get_updates()

print(bot.get_me())

def log(message, answer):
    print("\n -------------------------------------")
    from datetime import datetime
    print("\n", datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(" Ответ - ", answer)


@bot.message_handler(commands=['start'])
def handle_start(message):
    answer = 'Привет!!!'
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/help', '/start')
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    log(message, answer)
    print("Команда start")


@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = """Просто отправь мне фотографию, и я все сделаю"""
    bot.send_message(message.chat.id, answer)
    log(message, answer)
    print("Команда help")


@bot.message_handler(commands=['stop'])
def handle_start(message):
    answer = '...Закрываю...'
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, answer, reply_markup=hide_markup)
    log(message, answer)
    print("Команда stop")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Я не понимаю("
    if message.text == "Привет":
        answer = "Привет!"
        bot.send_message(message.chat.id, answer)
        log(message, answer)

    elif message.text == "Пока":
        answer = "Пока("
        bot.send_message(message.chat.id, answer)
        log(message, answer)

    elif (message.text == "Привет!") and str(message.from_user.id) == "422822380":
        answer = "Приветствую тебя, создатель"
        bot.send_message(message.chat.id, answer)
        log(message, answer)

    elif (message.text == "Как дела"):
        answer = "У меня отлично, а как у тебя"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Отлично', 'Не очень(')
        user_markup.row('Не хочу отвечать')
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    elif (message.text == 'Отлично'):
        answer = 'Ну тогда все отлично'
        bot.send_message(message.chat.id, answer)
        log(message, answer)

    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    print("Пришло обычное соощение")

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    import cv2
    bot.send_message(message.chat.id, 'Обрабатываю, подождите пару секунд')
    photo_id = message.photo[2].file_id
    path = photo_id + ".jpg"
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('C:\Projects\Telegram_bot_2.0' + '/' + path, 'wb') as new_file:
        new_file.write(downloaded_file)

    imagePath = "C:\Projects\Telegram_bot_2.0/" + photo_id + ".jpg"
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.06,
        minNeighbors=8,
        minSize=(15, 15)
        # flags = cv2.CV_HAAR_SCALE_IMAGE
    )
    print("face:{0}".format(len(faces)))
    face = answer ="{0}".format(len(faces))
    if len(faces) == 0:
        bot.send_message(message.chat.id, 'Я никого не нашел(')
    elif len(faces) > 0:
        bot.send_message(message.chat.id, 'Найдено лиц: ' + face)


    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    # iniciate id counter
    id = 0

    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['Unknow', 'Dmitriy', 'Diana', 'Sergey', 'Sumbel', 'Alex']

    img = cv2.imread(imagePath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.06,
        minNeighbors=8,
        minSize=(13, 13),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        print(str(id))
        bot.send_message(message.chat.id, str(id))

    os.remove(imagePath)
    log(message, answer)
bot.polling(none_stop = True, interval=0)