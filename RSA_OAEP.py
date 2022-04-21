from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from MedidorTiempo import mide_tiempo_RSA_OAEP_C
from MedidorTiempo import mide_tiempo_RSA_OAEP_D
import time

@mide_tiempo_RSA_OAEP_C
def cifrado(text):
	archivo = open('keyRSA.txt', 'r')
	key =  RSA.import_key(archivo.read())
	cipher = PKCS1_OAEP.new(key)
	ciphertext = cipher.encrypt(text)
	time.sleep(0.0001)
	return ciphertext

@mide_tiempo_RSA_OAEP_D
def descifrado(ciphertext):
	archivo = open('keyRSA.txt', 'r')
	key =  RSA.import_key(archivo.read())
	cipher = PKCS1_OAEP.new(key)
	message = cipher.decrypt(ciphertext)
	time.sleep(0.0001)
	return message

def RSA_OAEP_algoritmo(text):
	text = bytes(text, "utf-8")
	ciphertext = cifrado(text)
	message = descifrado(ciphertext)
