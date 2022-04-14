from base64 import b64encode
from base64 import b64decode
import time
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo =(time.time() - inicio)-0.0001
        #print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoChaCha.txt", 'a')
        archivo.write(str(tiempo)+ '\n')
        return c
    return funcion_medida

def generar_key_nonce_entrada(vector_prueba):
    #Implementacion de cifrado y descifrado con CHACHA20 usando PyCryptodome
    TextoEnClaro = bytes(vector_prueba, 'utf-8')
    #Se genera la llave y el nonce entradas para el algoritmo 
    key = get_random_bytes(32) #Esto equivale a 256 bits = 32 bytes
    nonce = get_random_bytes(12) #Se genera el nonce esto deacuerdo al RFC7539
    #Se le indica al algoritmo las entradas
    return key, nonce, TextoEnClaro

@mide_tiempo
def cifrado(key, nonce,TextoEnClaro):  
    Cifrado = ChaCha20.new(key=key, nonce=nonce)
    TextoCifrado = Cifrado.encrypt(TextoEnClaro)
    time.sleep(0.0001) #es necesario apra calcular el tiempo
    return TextoCifrado

def CifradoChacha20(key,nonce,TextoEnClaro): 
    TextoCifrado = cifrado(key, nonce, TextoEnClaro)
    ct = b64encode(TextoCifrado).decode('utf-8') #Es importante ya que permite hacer el descifrado lo pasa a base64
    resultCifrado = {'nonce': nonce, 'TextoCifrado':ct}
    #print(resultCifrado)
    return resultCifrado

def ChaCha20_algoritmo(vector_prueba):
    key,nonce,TextoEnClaro = generar_key_nonce_entrada(vector_prueba)
    temp = CifradoChacha20(key,nonce,TextoEnClaro)
    decifrar(temp, key, nonce)
    
@mide_tiempo
def decifrar(resultCifrado,key,nonce):
    #Descifrar
    TextoADescifrar = b64decode(resultCifrado['TextoCifrado'])
    #Se le indica al algoritmo las entradas
    Descifrado = ChaCha20.new(key=key, nonce=nonce)
    #Inicia el Descifrado
    TextoDescifrado = Descifrado.decrypt(TextoADescifrar)
    time.sleep(0.0001) #es necesario apra calcular el tiemp 
    resultDescifrado = {'nonce':nonce, 'TextoDescifrado':TextoDescifrado}
    #print(resultDescifrado)