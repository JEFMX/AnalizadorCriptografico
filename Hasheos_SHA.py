from Crypto.Hash import SHA384, SHA3_384, SHA512, SHA3_512
from MedidorTiempo import mide_tiempo_SHA2_384, mide_tiempo_SHA2_512, mide_tiempo_SHA3_384, mide_tiempo_SHA3_512
import time

@mide_tiempo_SHA2_384
def hasheo_SHA2_384(text): 
    h = SHA384.new()
    text = bytes(text, "utf-8")
    h.update(text)
    #print(h.hexdigest())
    time.sleep(0.0001) # es necesario apra calcular el tiempo

@mide_tiempo_SHA2_512
def hasheo_SHA2_512(text):
    h = SHA512.new()
    text = bytes(text, "utf-8")
    h.update(text)
    #print(h.hexdigest()
    time.sleep(0.0001) # es necesario apra calcular el tiempo

@mide_tiempo_SHA3_384
def hasheo_SHA3_384(text):
    h = SHA3_384.new()
    text = bytes(text, "utf-8")
    h.update(text)
    #print(h.hexdigest())
    time.sleep(0.0001) # es necesario apra calcular el tiempo

@mide_tiempo_SHA3_512
def hasheo_SHA3_512(text):
    h = SHA3_512.new()
    text = bytes(text, "utf-8")
    h.update(text)
    #print(h.hexdigest())
    time.sleep(0.0001) # es necesario apra calcular el tiempo