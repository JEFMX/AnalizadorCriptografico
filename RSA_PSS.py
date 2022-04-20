from Crypto.Signature import pss
from Crypto.Hash import SHA3_256
from Crypto.PublicKey import RSA	
from Crypto import Random
from MedidorTiempo import mide_tiempo_RSA_PSS_S
from MedidorTiempo import mide_tiempo_RSA_PSS_V
import time

@mide_tiempo_RSA_PSS_S
def firma(key, h):
	signature = pss.new(key).sign(h)
	time.sleep(0.0001)
	return signature

@mide_tiempo_RSA_PSS_V
def verificar(key, h, signature):
	verifier = pss.new(key)
	try:
		verifier.verify(h, signature)
	except (ValueError,TypeError):
		print("No se verifico")
	return 0

def RSA_PSS_algoritmo(text):
	text = bytes(text, "utf-8")
	archivo = open('keyRSA.txt', 'r')
	key =  RSA.import_key(archivo.read())
	archivo.close()
	h = SHA3_256.new(text)
	signature = firma(key, h)
	x = verificar(key, h, signature)
