from numpy import sign
from MedidorTiempo import mide_tiempo_ECDSA_PRIME_FIELD_S
from MedidorTiempo import mide_tiempo_ECDSA_PRIME_FIELD_V
from ecdsa import NIST521p, SigningKey

def key_generate():
     sk = SigningKey.generate(curve=NIST521p)
     return sk

@mide_tiempo_ECDSA_PRIME_FIELD_S
def firma(sk, text):
    signature = sk.sign(text)
    #print(signature)
    return signature
    
@mide_tiempo_ECDSA_PRIME_FIELD_V
def verificar(signature, sk, text):
    vk = sk.verifying_key
    assert vk.verify(signature, text)
    	
def ECDSA_PRIME_FIELD_algoritmo(text):
    text = bytes(text, "utf-8")
    sk = key_generate()
    signature = firma(sk, text)
    verificar(signature, sk, text)

#ECDSA_PRIME_FIELD_algoritmo()
