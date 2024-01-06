import telebot
bot = telebot.TeleBot("")

joinedFile = open("id")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())

@bot.message_handler(commands=['admes'])
def mess(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])

@bot.message_handler(content_types=["photo"])
def photo(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])
   idphoto = message.photo[0].file_id
   bot.send_photo(message.chat.id, idphoto )

bot.polling(none_stop = True)