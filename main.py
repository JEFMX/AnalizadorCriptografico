from time import time
from Chacha20 import ChaCha20_algoritmo
from AES_ECB import AES_ECB_algoritmo
from AES_GCM import AES_GCM_algoritmo
from MedidorTiempo import mide_tiempo
from Hasheos_SHA import hasheo_SHA2_384, hasheo_SHA2_512, hasheo_SHA3_384, hasheo_SHA3_512
from RSA_PSS import RSA_PSS_algoritmo
from RSA_OAEP import RSA_OAEP_algoritmo
from ECDSA_PF import ECDSA_PRIME_FIELD_algoritmo
from ECDSA_BF import ECDSA_BINARY_FIELD_algoritmo
from KeyNonceVector import generar_key_nonce_entrada
import os, platform, psutil

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
        RSA_OAEP_algoritmo(i.strip('\n'))
        RSA_PSS_algoritmo(i.strip('\n'))
        ECDSA_PRIME_FIELD_algoritmo(i.strip('\n'))
        ECDSA_BINARY_FIELD_algoritmo(i.strip('\n'))
    
        
        # Se muestra el porcentaje
        p = p + 1
        if(p == len(linea)):
            if(platform.system()== "Windows"): 
                os.system("cls")
                print(".: Analisis finalizado :.")
                print("Porcentaje: 100")
                uname = platform.uname()
                print(f"Sistema: {uname.system}")
                print(f"Nombre del dispositivo: {uname.node}")
                print(f"Version: {uname.version}")
                print(f"Arquitectura: {uname.machine}")
                print(f"Procesador: {uname.processor}")
                print("Nucleos fisicos:", psutil.cpu_count(logical= False))
                print("Total de nuclos:", psutil.cpu_count(logical= True))
                cpufreq = psutil.cpu_freq()
                print(f"Frecuencia Maxima: {cpufreq.max:.2f} [Mhz]")
                print(f"Frecuencia Minima: {cpufreq.min:.2f} [Mhz]")
                print(f"Frecuencia Actual: {cpufreq.current:.2f} [Mhz]")
            else: 
                os.system("clear")
                print(".: Analisis finalizado :.")
                print("Porcentaje: 100")
                uname = platform.uname()
                print(f"Sistema: {uname.system}")
                print(f"Nombre del dispositivo: {uname.node}")
                print(f"Version: {uname.version}")
                print(f"Arquitectura: {uname.machine}")
                print(f"Procesador: {uname.processor}")
                print("Nucleos fisicos:", psutil.cpu_count(logical= False))
                print("Total de nuclos:", psutil.cpu_count(logical= True))
                cpufreq = psutil.cpu_freq()
                print(f"Frecuencia Maxima: {cpufreq.max:.2f} [Mhz]")
                print(f"Frecuencia Minima: {cpufreq.min:.2f} [Mhz]")
                print(f"Frecuencia Actual: {cpufreq.current:.2f} [Mhz]")
        elif((p % 10) == 0):
            if(platform.system()== "Windows"): 
                os.system("cls")
                print(".: Analizando Espere :.")
                print("Porcentaje: {}%".format(p))
                uname = platform.uname()
                print(f"Sistema: {uname.system}")
                print(f"Nombre del dispositivo: {uname.node}")
                print(f"Version: {uname.version}")
                print(f"Arquitectura: {uname.machine}")
                print(f"Procesador: {uname.processor}")
                print("Nucleos fisicos:", psutil.cpu_count(logical= False))
                print("Total de nuclos:", psutil.cpu_count(logical= True))
                cpufreq = psutil.cpu_freq()
                print(f"Frecuencia Maxima: {cpufreq.max:.2f} [Mhz]")
                print(f"Frecuencia Minima: {cpufreq.min:.2f} [Mhz]")
                print(f"Frecuencia Actual: {cpufreq.current:.2f} [Mhz]")
            else: 
                os.system("clear")
                print(".: Analizando Espere :.")
                print("Porcentaje: {}%".format(10))
                uname = platform.uname()
                print(f"Sistema: {uname.system}")
                print(f"Nombre del dispositivo: {uname.node}")
                print(f"Version: {uname.version}")
                print(f"Arquitectura: {uname.machine}")
                print(f"Procesador: {uname.processor}")
                print("Nucleos fisicos:", psutil.cpu_count(logical= False))
                print("Total de nuclos:", psutil.cpu_count(logical= True))
                cpufreq = psutil.cpu_freq()
                print(f"Frecuencia Maxima: {cpufreq.max:.2f} [Mhz]")
                print(f"Frecuencia Minima: {cpufreq.min:.2f} [Mhz]")
                print(f"Frecuencia Actual: {cpufreq.current:.2f} [Mhz]")
    
main()
if(platform.system()== "Windows"):
    os.system("py " + os.path.abspath(os.getcwd()) + "/Graficos.py")
else:
    os.system("python3 " + os.path.abspath(os.getcwd()) + "/Graficos.py")