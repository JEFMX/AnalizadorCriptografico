import random
import string
import os
from Crypto.Random import get_random_bytes
from borrar import borrar_datos
from Crypto.PublicKey import RSA


def generar_key_nonce_entrada():
    # Se borran los archivos preexistentes
    borrar_datos()

    # Se genera la llave
    key = get_random_bytes(32)  # Esto equivale a 256 bits = 32 bytes
    # Se crea el archivo para almacenar la llave
    archivo = open("key.txt", "w")
    # Se escribe la llave en el archivo
    archivo.write(str(key))
    # Se cierra el archivo
    archivo.close()

    # Se genera la llave de RSA
    keyRSA = RSA.generate(2048) # Se genera una lalve de 2048 bits
    # Se crea el archivo para almacenar la llave
    f = open('keyRSA.txt','wb')
    # Se escribe la lalve en el archivo
    f.write(keyRSA.export_key('PEM'))
    # Se cierra el archivo
    f.close()

    # Se genera el nonce
    nonce = get_random_bytes(12)  # Se genera el nonce esto deacuerdo al RFC7539
    # Se crea el archivo para almacenar el nonce
    archivo = open("nonce.txt", "w")
    # Se escribe la llave en el archivo
    archivo.write(str(nonce))
    # Se cierra el archivo
    archivo.close()

    # Se crea el archivo para almacenar los vectores
    archivo = open("vectores.txt", 'a')
    # Se generan los vectores de prueba
    vectores = []
    for i in range(1, 101):
        # Se determina la longitud del vector de prueba
        longitud_vector = i * 2
        # Se genera el vector de prueba
        vector_prueba = ''.join(random.choice(string.ascii_letters + string.digits)
                                for _ in range(longitud_vector))
        # Se almacena en el archivo
        archivo.write(vector_prueba + '\n')
        vectores.append(vector_prueba)
    # Se cierra el archivo
    archivo.close()

    return key, nonce, vectores
