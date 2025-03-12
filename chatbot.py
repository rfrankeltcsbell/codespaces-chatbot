from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
import nltk 
nltk.download('punkt_tab')

chatbot = ChatBot("ChatBot")
trainer= ListTrainer(chatbot)
trainer.train(["hello world","how can I help you"])
trainer.train(["What is your Name"])
trainer.train(["my name is chatbot"])

exit_conditions=("quit")
while True:
    query= input("> ")
    if query in exit_conditions:
        break
    else:
        print((f"{chatbot.get_response(query)}"))
