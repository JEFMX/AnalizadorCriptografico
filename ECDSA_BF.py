from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from ECDSA_PF import key_generate
from MedidorTiempo import mide_tiempo_ECDSA_BINARY_FIELD_S
from MedidorTiempo import mide_tiempo_ECDSA_PRIME_FIELD_V

def key_generate():
    sk = ec.generate_private_key(ec.SECT571K1())
    return sk

@mide_tiempo_ECDSA_BINARY_FIELD_S
def firma(sk ,text):
    signature = sk.sign(text, ec.ECDSA(hashes.SHA256()))
    #print(signature)
    return signature

@mide_tiempo_ECDSA_PRIME_FIELD_V
def verificar(signature, sk, text):
    spk = sk.public_key()
    spk.verify(signature, text, ec.ECDSA(hashes.SHA256()))

def ECDSA_BINARY_FIELD_algoritmo(text):
    text = bytes(text, "utf-8")
    sk = key_generate()
    signature = firma(sk, text)
    verificar(signature, sk, text)