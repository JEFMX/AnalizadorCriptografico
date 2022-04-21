import os
import shutil

def borrar_datos():

#PARA LA CACHE GENERADA POR PYCRYPTODOME
    if(os.path.exists("__pycache__") == True):
        shutil.rmtree("__pycache__")

#PARA ALGORITMOS DE CIFRADO Y DESCIFRADO
    # Se verifica si ya hay llave
    if(os.path.exists("key.txt") == True):
        os.remove("key.txt")
    # Se verifica si ya hay llave
    if(os.path.exists("keyRSA.txt") == True):
        os.remove("keyRSA.txt")
    # Se verifica si ya hay nonce
    if(os.path.exists("nonce.txt") == True):
        os.remove("nonce.txt")
    # Se verifica si ya hay vectores
    if(os.path.exists("vectores.txt") == True):
        os.remove("vectores.txt")
    # Se verifica si ya hay resultados ChaCha20
    if(os.path.exists("TiempoChaCha20_C.txt") == True):
        os.remove("TiempoChaCha20_C.txt")
    if(os.path.exists("TiempoChaCha20_D.txt") == True):
        os.remove("TiempoChaCha20_D.txt")
    # Se verifica si ya hay resultados AES_ECB
    if(os.path.exists("TiempoAES_ECB_C.txt") == True):
        os.remove("TiempoAES_ECB_C.txt")
    if(os.path.exists("TiempoAES_ECB_D.txt") == True):
        os.remove("TiempoAES_ECB_D.txt")
    # Se verifica si ya hay resultados AES_GCM
    if(os.path.exists("TiempoAES_GCM_C.txt") == True):
        os.remove("TiempoAES_GCM_C.txt")
    if(os.path.exists("TiempoAES_GCM_D.txt") == True):
        os.remove("TiempoAES_GCM_D.txt")
    # Se verifica si ya hay resultados RSA_OAEP
    if(os.path.exists("TiempoRSA_OAEP_C.txt") == True):
        os.remove("TiempoRSA_OAEP_C.txt")
    if(os.path.exists("TiempoRSA_OAEP_D.txt") == True):
        os.remove("TiempoRSA_OAEP_D.txt")

#PARA ALGORITMOS DE HASHEO
    # Se verifica si ya hay resultados SHA2-384
    if(os.path.exists("TiempoSHA2_384.txt") == True):
        os.remove("TiempoSHA2_384.txt")
    # Se verifica si ya hay resultados SHA2-512
    if(os.path.exists("TiempoSHA2_512.txt") == True):
        os.remove("TiempoSHA2_512.txt")
    # Se verifica si ya hay resultados SHA3-384
    if(os.path.exists("TiempoSHA3_384.txt") == True):
        os.remove("TiempoSHA3_384.txt")
    # Se verifica si ya hay resultados SHA3-512
    if(os.path.exists("TiempoSHA3_512.txt") == True):
        os.remove("TiempoSHA3_512.txt")
    
#PARA ALGORITMOS DE FIRMA
    # Se verifica si ya hay resultados RSA PSS
    if(os.path.exists("TiempoRSA_PSS_S.txt") == True):
        os.remove("TiempoRSA_PSS_S.txt")
    # Se verifica si ya hay resultados RSA PSS
    if(os.path.exists("TiempoRSA_PSS_V.txt") == True):
        os.remove("TiempoRSA_PSS_V.txt")
