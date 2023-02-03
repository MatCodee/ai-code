''''
Esta esuna implementacion simple pero me va a servir como inicio del proyecto
De esta manera voy a poder responder de forma normal como si fuera yo el que responde 

En el futuro se va a implementar un procesamiento de palabras usando la propia red neuronal del sistema
'''
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from enum import Enum


#TODO: 3) mejorar el chatbot usando redes neuronales para el procesamiento de lengauje
# el objetivo es implementar el reconocimiento de lengyuaje Chileno y ser capaz de moverse con los modismos chilenos

class State_bot(Enum):
    LISTENING = 1,
    PROCESSING = 2,

conversation = [
        "hola mi compadre como esta",

        "mati estas?",
        "dime?",

        "Quieres jugar el lol?",
        "No puedo jugar triste",
        "no puedo jugar al lol",
    
        "uff, estoy full no puedo conectarme, gome",
        "no puedo ajja adios",
        "sin tiempo",
        "full horario",
        "algun dia me conecto",
        "lo dudo, no me conectare",
        
        "que",
        "que pasa?",
        "Hola gente como estan", 
        "que riko escuchar musica",
        "hola y adios",
        "viva la droga LOL",

        "Son prioridades",
        "prioridades perra",
    ]

# Esto es una mierda pero por el momento me sirve para poder testeae las cosas
def start_bot():
    chatbot = ChatBot("mati")
    trainer = ListTrainer(chatbot)
    trainer.train(conversation)

    while True:
        try:
            bot_input = chatbot.get_response(input())
            print(bot_input)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break
