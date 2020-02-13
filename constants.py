
tag = 'C:\Projects\Telegram_bot_2.0\trainer/trainer.yml'
token = "616458226:AAFZGaWoBtVjTYqKtKBNtQcMItwqi8-X9eY"




'''
bot.send_chat_action(message.from_user.id, 'upload_photo')
bot.send_photo(message.from_user.id, constants.template_photo_id)

         all_files_in_dictionary = os.listdir(directory)
         print(all_files_in_directory)
         for file in all_files_in_directory:
             img = open(directory + '/' + file, 'rb' )
             bot.send_chat_action(message.from_user.id, 'upload_photo')
             bot.send_photo(message.from_user.id, img)
             img.close()
             
    elif message.text == 'фото':
         directory = 'C:\Projects\Telegram_bot_2.0\pictures'
         all_files_in_directory = os.listdir(directory)
         random_files = random.choice(all_files_in_directory)
         img = open(directory + '/' + random_files, 'rb' )
         bot.send_chat_action(message.from_user.id, 'upload_photo')
         bot.send_photo(message.from_user.id, img)
         img.close()
         
    elif message.text == 'фото':
         url = constants.urlp
         urllib2.urlretrieve(url, 'url_image.jpg')
         img = open('url_image.jpg', 'rb')
         bot.send_chat_action(message.from_user.id, 'upload_photo')
         bot.send_photo(message.from_user.id, img)
         img.close()
'''