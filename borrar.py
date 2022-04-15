import os


def borrar_datos():
    # Se verifica si ya hay llave
    if(os.path.exists("key.txt") == True):
        os.remove("key.txt")
    # Se verifica si ya hay nonce
    if(os.path.exists("nonce.txt") == True):
        os.remove("nonce.txt")
    # Se verifica si ya hay vectores
    if(os.path.exists("vectores.txt") == True):
        os.remove("vectores.txt")
    # Se verifica si ya hay resultados ChaCha20
    if(os.path.exists("TiempoChaCha20.txt") == True):
        os.remove("TiempoChaCha20.txt")
    # Se verifica si ya hay resultados AES_ECB
    if(os.path.exists("TiempoAES_ECB.txt") == True):
        os.remove("TiempoAES_ECB.txt")
    '''
    # Se verifica si ya hay resultados AES_GCM
    if(os.path.exists("TiempoAES_GCM.txt") == True):
        os.remove("TiempoAES_GCM.txt")
    '''
