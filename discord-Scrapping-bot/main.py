import time

# Estos son archivos locales
from discord_scrap import DiscordScrap
import config

def start():
    ds = DiscordScrap(config.email,config.password)
    ds.start()

import chat_bot


#TODO: 2)  Cr ear la funcion principal que va a a acutar de manera inteligente en discord 
# va a combinar los usos y entrada dentro de los canales y los amigos de cada persona
def test_bot():
    chat_bot.start_bot()

def main():
    time.sleep(2)
    #start()
    test_bot()


if __name__ == '__main__':
    main()