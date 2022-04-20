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


def mide_tiempo_ChaCha20(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoChaCha20.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida


def mide_tiempo_AES_ECB(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoAES_ECB.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida

def mide_tiempo_AES_GCM(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoAES_GCM.txt", 'a')
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

def mide_tiempo_RSA_PSS_S(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo = (time.time() - inicio)-0.0001
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
        tiempo = (time.time() - inicio)-0.0001
        # print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoRSA_PSS_V.txt", 'a')
        archivo.write(str(tiempo) + '\n')
        archivo.close()
        return c
    return funcion_medida