import telebot
bot = telebot.TeleBot("")

joinedFile = open("id")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())

@bot.message_handler(commands=['start'])
def startJoin(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("id", "a")
        joinedFile.write(str(message.chat.id)+"\n")
        joinedUsers.add(message.chat.id)
        bot.send_message(message.chat.id, "Спасибо что подписались на рассылку!")

@bot.message_handler(commands=['admes'])
def mess(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])

@bot.message_handler(commands=['info'])
def mess(message):
    bot.send_message(message.chat.id, "Вы можете со мной связаться в различных соцсетях")


bot.polling(none_stop = True)