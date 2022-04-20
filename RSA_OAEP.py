from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from MedidorTiempo import mide_tiempo_RSA_OAEP
import time

@mide_tiempo_RSA_OAEP 
def cifrado(key, text):
	cipher = PKCS1_OAEP.new(key)
	ciphertext = cipher.encrypt(text)
	time.sleep(0.0001)
	return ciphertext

@mide_tiempo_RSA_OAEP
def descifrado(key,ciphertext):
	cipher = PKCS1_OAEP.new(key)
	message = cipher.decrypt(ciphertext)
	time.sleep(0.0001)
	return message

def RSA_OAEP_algoritmo(text):
	text = bytes(text, "utf-8")
	archivo = open('keyRSA.txt', 'r')
	key =  RSA.import_key(archivo.read())
	archivo.close()
	ciphertext = cifrado(key, text)
	message = descifrado(key, ciphertext)
