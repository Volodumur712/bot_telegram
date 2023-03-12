import telebot
import openai

bot = telebot.TeleBot("6154917026:")
openai.api_key = "sk-"
 
# python presentational.py

@bot.message_handler(content_types=['text'])
def lalala(message):
    if any(word in message.text.lower() for word in ["/start", "start", "stop", "end"]):
        bot.send_message(message.chat.id, "Привіт, я презентаційний варіант бота зі штучним інтелектом, такий самий може бути і в тебе, спробуй запитати у мене про що небудь")
    
    elif "путін" in message.text.lower():
        bot.send_message(message.chat.id, "цей гівнюк - XYйл0")
    elif "вова" in message.text.lower():
        bot.send_message(message.chat.id, "красавчик який написав цей код")
    elif "як тебе" in message.text.lower():
        bot.send_message(message.chat.id, "presentational")

    elif any(word in message.text.lower() for word in ["хто ти", "що ти", "можеш", "які твої", "можливості"]):
        bot.send_message(message.chat.id, "Я презентую можливості штучного інтелекту, постав мені запитання")
    elif any(word in message.text.lower() for word in ["автор", "шедевр", "бота", "розробник"]):
        bot.send_message(message.chat.id, "Слуценко Володимир Миколайович")
    elif any(word in message.text.lower() for word in ["контакт", "автор", "розробник", "резюме", "замовити"]):
        bot.send_message(message.chat.id, "http://citrus.infinityfreeapp.com/")
    elif any(word in message.text.lower() for word in ["олія", "цукор", "мука", "овочі"]):
        bot.send_message(message.chat.id, "товари на жіва")
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
