import time
from Crypto.Cipher import ChaCha20
from MedidorTiempo import mide_tiempo_ChaCha20_C
from MedidorTiempo import mide_tiempo_ChaCha20_D


@mide_tiempo_ChaCha20_C
def cifrado(key, TextoEnClaro):
    Cifrado = ChaCha20.new(key=key)
    TextoCifrado = Cifrado.encrypt(TextoEnClaro)
    time.sleep(0.0001)  # es necesario apra calcular el tiempo
    return TextoCifrado

@mide_tiempo_ChaCha20_D
def descifrar(resultCifrado, key):
    # Descifrar
    # Se le indica al algoritmo las entradas
    Descifrado = ChaCha20.new(key=key)
    # Inicia el Descifrado
    Descifrado.decrypt(resultCifrado)
    time.sleep(0.0001)  # es necesario apra calcular el tiempo

def ChaCha20_algoritmo(key, TextoEnClaro):
    TextoEnClaro = bytes(TextoEnClaro, "utf-8")
    temp = cifrado(key, TextoEnClaro)
    descifrar(temp, key)
