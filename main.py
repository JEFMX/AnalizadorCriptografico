from Chacha20 import ChaCha20_algoritmo
from AES_ECB import AES_ECB_algoritmo
from KeyNonceVector import generar_key_nonce_entrada
import os


def main():
    # Se generan los vectores de prueba, la llave y el nonce
    key, nonce, linea = generar_key_nonce_entrada()
    # Se realizan los algoritmos por cada vector
    p = 0
    for i in linea:
        ChaCha20_algoritmo(key, i.strip('\n'))
        AES_ECB_algoritmo(key, i.strip('\n'))
        # Se muestra el porcentaje
        p = p + 1
        if(p == 100):
            print(".: Analisis finalizado :.")
        elif(p % 10 == 0):
            print("Porcentaje: {}%".format(p))
            os.system("clear")
        


main()
