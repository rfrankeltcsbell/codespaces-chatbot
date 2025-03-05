from chatterbot import ChatBot
talkbot=ChatBot("Chatbot")

exit_conditions=("quit")
while True:
    query= input("> ")
    if query in exit_conditions:
        break
    else:
        print((f"{talkbot.get_response(query)}"))