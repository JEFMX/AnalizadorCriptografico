from base64 import b64encode
from base64 import b64decode
import time
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from MedidorTiempo import mide_tiempo


@mide_tiempo
def cifrado(key, nonce, TextoEnClaro):
    Cifrado = ChaCha20.new(key=key, nonce=nonce)
    TextoCifrado = Cifrado.encrypt(TextoEnClaro)
    time.sleep(0.0001)  # es necesario apra calcular el tiempo
    return TextoCifrado


def CifradoChacha20(key, nonce, TextoEnClaro):
    TextoCifrado = cifrado(key, nonce, TextoEnClaro)
    # Es importante ya que permite hacer el descifrado lo pasa a base64
    ct = b64encode(TextoCifrado).decode('utf-8')
    resultCifrado = {'nonce': nonce, 'TextoCifrado': ct}
    # print(resultCifrado)
    return resultCifrado


def ChaCha20_algoritmo(key, nonce, TextoEnClaro):
    TextoEnClaro = bytes(TextoEnClaro, "utf-8")
    temp = CifradoChacha20(key, nonce, TextoEnClaro)
    #descifrar(temp, key, nonce)


'''
@mide_tiempo
def descifrar(resultCifrado,key,nonce):
    #Descifrar
    TextoADescifrar = b64decode(resultCifrado['TextoCifrado'])
    #Se le indica al algoritmo las entradas
    Descifrado = ChaCha20.new(key=key, nonce=nonce)
    #Inicia el Descifrado
    TextoDescifrado = Descifrado.decrypt(TextoADescifrar)
    time.sleep(0.0001) #es necesario apra calcular el tiemp
    resultDescifrado = {'nonce':nonce, 'TextoDescifrado':TextoDescifrado}
    #print(resultDescifrado)
'''
