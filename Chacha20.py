import json
from base64 import b64encode
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

TextoEnClaro = b'Attack at dawn'
key = get_random_bytes(32) #Esto equivale a 256 bits = 32 bytes
print(key)
Cifrado = ChaCha20.new(key=key)
TextoCifrado = Cifrado.encrypt(TextoEnClaro)

nonce = b64encode(Cifrado.nonce).decode('utf-8')
ct = b64encode(TextoCifrado).decode('utf-8')
result = json.dumps({'nonce':nonce, 'TextoCifrado':ct})
print(result)