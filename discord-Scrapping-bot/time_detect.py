'''
# Esta es una clase que va a generar la informacion importante dle dia 
# y ademas va a hacer un conteo de la informacon que se esta generando 


Vamos almacena la informacion del dia con el texto
cada texto de informacon se generara con (<name channel> + <fecha definida>)
ejemplo:
tetas-27-09-2021 // de esta forma sabemos y es una conversacion antigua o no para el uso de las cnoversacion
'''
import time
import os
import datetime

# TODO: 2) definicion de las funciones de tiempo para poder guardar los datos de manera ordenada e ir comparandola


# ver si esto es compatible con el formato
# funciones como saver el dia de hoy
def date_now():
    return datetime.datetime.now()


# TODO: No se si esta funcion realmente esta bien
def compareDate(date_prev,date_current):
    if(date_prev < date_current):
        date_dif = date_prev - date_current
        print(date_current)
        return date_dif
    else:
        return date_current


