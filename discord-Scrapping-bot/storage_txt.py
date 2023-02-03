
# funciones locales
import config

# Esta son las funciones para la creacion de archivos txt para almacenar la informacion
def create_file(path,mode,name_data,message):
    with open(path + '/' + name_data,mode) as f:
        f.write(message)




    
