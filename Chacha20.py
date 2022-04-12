from base64 import b64encode
from base64 import b64decode
from webbrowser import get
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

#Implementacion de cifrado y descifrado con CHACHA20 usando PyCryptodome
TextoEnClaro = b'Attack at dawn'

#Se genera la llave y el nonce entradas para el algoritmo 
key = get_random_bytes(32) #Esto equivale a 256 bits = 32 bytes
nonce = get_random_bytes(12) #Se genera el nonce esto deacuerdo al RFC7539
#Se le indica al algoritmo las entradas
Cifrado = ChaCha20.new(key=key, nonce=nonce)
#Inicia el cifrado
TextoCifrado = Cifrado.encrypt(TextoEnClaro)
ct = b64encode(TextoCifrado).decode('utf-8') #Es importante ya que permite hacer el descifrado lo pasa a base64
resultCifrado = {'nonce':nonce, 'TextoCifrado':ct}
print(resultCifrado)

#Descifrar
TextoADescifrar = b64decode(resultCifrado['TextoCifrado'])
#Se le indica al algoritmo las entradas
Descifrado = ChaCha20.new(key=key, nonce=nonce)
#Inicia el Descifrado
TextoDescifrado = Descifrado.decrypt(TextoADescifrar)
resultDescifrado = {'nonce':nonce, 'TextoDescifrado':TextoDescifrado}
print(resultDescifrado)