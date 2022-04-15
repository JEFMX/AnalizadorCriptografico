import time
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from MedidorTiempo import mide_tiempo_ChaCha20


@mide_tiempo_ChaCha20
def cifrado(key, nonce, TextoEnClaro):
    Cifrado = ChaCha20.new(key=key)
    TextoCifrado = Cifrado.encrypt(TextoEnClaro)
    time.sleep(0.0001)  # es necesario apra calcular el tiempo
    return TextoCifrado


@mide_tiempo_ChaCha20
def descifrar(resultCifrado, key, nonce):
    # Descifrar
    # Se le indica al algoritmo las entradas
    Descifrado = ChaCha20.new(key=key)
    # Inicia el Descifrado
    TextoDescifrado = Descifrado.decrypt(resultCifrado)
    time.sleep(0.0001)  # es necesario apra calcular el tiempo


def ChaCha20_algoritmo(key, nonce, TextoEnClaro):
    TextoEnClaro = bytes(TextoEnClaro, "utf-8")
    temp = cifrado(key, nonce, TextoEnClaro)
    #descifrar(temp, key, nonce)
