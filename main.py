from time import time
from Chacha20 import ChaCha20_algoritmo
from AES_ECB import AES_ECB_algoritmo
from AES_GCM import AES_GCM_algoritmo
from MedidorTiempo import mide_tiempo
from Hasheos_SHA import hasheo_SHA2_384, hasheo_SHA2_512, hasheo_SHA3_384, hasheo_SHA3_512
from KeyNonceVector import generar_key_nonce_entrada
import os, platform

@mide_tiempo
def main():
    # Se generan los vectores de prueba, la llave y el nonce
    key, nonce, linea = generar_key_nonce_entrada()
    # Se realizan los algoritmos por cada vector
    p = 0
    for i in linea:
        ChaCha20_algoritmo(key, i.strip('\n'))
        AES_ECB_algoritmo(key, i.strip('\n'))
        AES_GCM_algoritmo(key, i.strip('\n'))
        hasheo_SHA2_384(i.strip('\n'))
        hasheo_SHA2_512(i.strip('\n'))
        hasheo_SHA3_384(i.strip('\n'))
        hasheo_SHA3_512(i.strip('\n'))
        # Se muestra el porcentaje
        p = p + 1
        if(p == len(linea)):
            if(platform.system()== "Windows"): 
                os.system("cls")
                print(".: Analisis finalizado :.")
                print("Porcentaje: {}%".format(p/10))
            else: 
                os.system("clear")
                print(".: Analisis finalizado :.")
                print("Porcentaje: {}%".format(int(p/10)))
        elif(p % (len(linea)/10) == 0):
            if(platform.system()== "Windows"): 
                os.system("cls")
                print(".: Analizando Espere :.")
                print("Porcentaje: {}%".format(int(p/10)))
            else: 
                os.system("clear")
                print(".: Analizando Espere :.")
                print("Porcentaje: {}%".format(int(p/10)))
        
    
main()
os.system("py "+ os.path.abspath(os.getcwd()) + "/Graficos.py")