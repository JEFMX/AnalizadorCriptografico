import time

def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)
        #Para ver el tiempo en consola de todo el tiempo de ejecucion del programa
        print("Tiempo total de ejecución de todos los algoritmos: " + str(tiempo)) 
        return c
    return funcion_medida


def mide_tiempo_ChaCha20_C(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoChaCha20_C.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_ChaCha20_D(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoChaCha20_D.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_AES_ECB_C(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoAES_ECB_C.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_AES_ECB_D(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoAES_ECB_D.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_AES_GCM_C(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoAES_GCM_C.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_AES_GCM_D(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoAES_GCM_D.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_SHA2_384(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoSHA2_384.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_SHA2_512(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoSHA2_512.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_SHA3_384(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoSHA3_384.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_SHA3_512(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoSHA3_512.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_RSA_OAEP_C(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoRSA_OAEP_C.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_RSA_OAEP_D(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoRSA_OAEP_D.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_RSA_PSS_S(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoRSA_PSS_S.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_RSA_PSS_V(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoRSA_PSS_V.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_ECDSA_PRIME_FIELD_S(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoECDSA_PRIME_FIELD_S.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_ECDSA_PRIME_FIELD_V(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoECDSA_PRIME_FIELD_V.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_ECDSA_BINARY_FIELD_S(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoECDSA_BINARY_FIELD_S.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_ECDSA_BINARY_FIELD_V(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoECDSA_BINARY_FIELD_V.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida