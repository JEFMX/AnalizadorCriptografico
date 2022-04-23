from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from MedidorTiempo import mide_tiempo_RSA_OAEP_C
from MedidorTiempo import mide_tiempo_RSA_OAEP_D
import time

@mide_tiempo_RSA_OAEP_C
def cifrado(file_key, text):
	key =  RSA.import_key(file_key)
	cipher = PKCS1_OAEP.new(key)
	ciphertext = cipher.encrypt(text)
	time.sleep(0.0001)
	return ciphertext, key

@mide_tiempo_RSA_OAEP_D
def descifrado(key, ciphertext):
	cipher = PKCS1_OAEP.new(key)
	message = cipher.decrypt(ciphertext)
	time.sleep(0.0001)
	return message

def RSA_OAEP_algoritmo(text):
	text = bytes(text, "utf-8")
	archivo =  open('keyRSA.txt', 'r')
	file_key = archivo.read()
	archivo.close()
	ciphertext, key = cifrado(file_key, text)
	message = descifrado(key, ciphertext)
