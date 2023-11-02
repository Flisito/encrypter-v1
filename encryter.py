#Importar librerias
import numpy
import random
import datetime

def encriptar(text, llave):
# Metodo de encriptado por XoR
    mensaje_encriptado = ""
    for i in range(len(text)):
        mensaje_encriptado += chr(ord(text[i]) ^ ord(llave[i % len(llave)]))
    return mensaje_encriptado.encode("utf-8").hex()

def desencriptar(ciphertext, llave):
# Formatear mensaje y desencriptar mensaje
  txtformat = bytes.fromhex(ciphertext)
  txtformat = txtformat.decode("utf-8")
  mensaje_original = ""
  for i in range(len(txtformat)):
    mensaje_original += chr(ord(txtformat[i]) ^ ord(llave[i % len(llave)]))
  return mensaje_original

def generadorllave(Msjlen): #Generamos una llave para encriptar el mensaje

# Establecer variables de arrays con caracteres
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    prm_numbers = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    spc_cha = ['!', '@', '$', '^', '&', '*', '(', ')', '_', '+', '?', '~', '<', '>']

# Extraer los minutos y segundos del sistema en ese momento para realizar operaciones
    act_time = datetime.datetime.now()
    minutes = int(act_time.minute)
    seconds = int(act_time.second)

# Tomar lista de primos y multiplicar por los minutos del sistema en ese momento
    prm_number_minute =[]
    for i in range(len(prm_numbers)):
        prm_number_minute.append(minutes * prm_numbers[i])

# Tomar lista de primos y multiplicar por los segundos del sistema en ese momento
    prm_number_second = []
    for i in range(len(prm_numbers)):
        prm_number_second.append(seconds * prm_numbers[i] * prm_number_minute[i])

# Concatenar los Arrays creados y hacer la llave combinada final
    vararrconc1 = numpy.append(prm_numbers, prm_number_second)
    vararrconc2 = numpy.append(vararrconc1, prm_number_minute)
    vararrconc3 = numpy.append(vararrconc2, spc_cha)
    combined_key = numpy.append(abc, vararrconc3)

# Combinar todos los arrays combinados
    numpy.random.shuffle(combined_key)

# Crear una semilla en crudo
    seed_raw = []
    for i in range(500):
        seed_raw.append(random.randint(0,999))

# Combinar la semilla con la llave combinada
    seed = []
    for i in range(len(random.sample(seed_raw, len(Msjlen)))):
        seed.append(combined_key[i])

# Convertir lista random que generamos en string
    strkey = ""
    for ele in seed:
        strkey += ele

    return (strkey)

