import telebot
import openai

bot = telebot.TeleBot("6154917026:")
openai.api_key = "sk-"
 
# python presentational.py

@bot.message_handler(content_types=['text'])
def lalala(message):
    if "/start" in message.text.lower():
        bot.send_message(message.chat.id, "Привіт, я презентаційний бот, такий самий може бути і в тебе, запитай у мене що небудь")
    elif "путін" in message.text.lower():
        bot.send_message(message.chat.id, "цей гівнюк - XYйл0")
    elif "хто ти" in message.text.lower():
        bot.send_message(message.chat.id, "Я презентую можливості")
    elif "вова" in message.text.lower():
        bot.send_message(message.chat.id, "красавчик який написав цей код")
    elif "як тебе" in message.text.lower():
        bot.send_message(message.chat.id, "presentational")
    elif "автор бот" in message.text.lower():
        bot.send_message(message.chat.id, "Слуценко Володимир Миколайович")
    elif "контакт автор" in message.text.lower():
        bot.send_message(message.chat.id, "http://citrus.infinityfreeapp.com/")
    elif any(word in message.text.lower() for word in ["олія", "цукор", "мука", "овочі"]):
        bot.send_message(message.chat.id, "Я з масиву 1")
    elif any(word in message.text.lower() for word in ["візок", "гойдалка", "колиска", "заколис"]):
        bot.send_message(message.chat.id, "шукай дешевше")
    else:
        print(message.chat.title, message.chat.username)
        message.text = (message.text).replace("@present712_bot ", "")
        print(message.text)
        response = openai.Completion.create(model="text-davinci-003", prompt=message.text, max_tokens=1000)
        full_response = response['choices'][0]['text']  # Use the text property of the first element of the choices list to access the full response
        lines = full_response.splitlines()  # Split the response into individual lines 
        for line in lines:  # Iterate over the lines
            try:
                print(line)
                bot.send_message(message.chat.id, line)  # Send each line back to the user as a separate message
            except Exception as e:
                print(e)
bot.polling(none_stop=True, interval=0)
