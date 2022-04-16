import time
from Crypto.Cipher import AES
from MedidorTiempo import mide_tiempo_AES_GCM
from Crypto.Util.Padding import pad, unpad

@mide_tiempo_AES_GCM
def cifrado(key, text):
    cipher = AES.new(key, AES.MODE_GCM)
    cipherText = cipher.encrypt(pad(text, 32))
    time.sleep(0.0001)  # es necesario apra calcular el tiempo
    return cipherText

#Esta fallando el descifrado 
'''''
#@mide_tiempo_AES_GCM
def descifrado(key, cipherText):
    decipher = AES.new(key, AES.MODE_GCM)
    plainText = unpad(decipher.decrypt(cipherText), 32)
    time.sleep(0.0001)  # es necesario apra calcular el tiempo
    return plainText
'''

def AES_GCM_algoritmo(key, text):
    text = bytes(text, "utf-8")
    cipherText = cifrado(key, text)
    #plainText = descifrado(key, cipherText)
    #print(str(text) + "\n" + str(cipherText) + "\n" + str(plainText))