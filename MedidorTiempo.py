import time

def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        tiempo =(time.time() - inicio)-0.0001
        #print(tiempo) #Para ver el tiempo en consola es temporal
        archivo = open("TiempoChaCha20.txt", 'a')
        archivo.write(str(tiempo)+ '\n')
        return c
    return funcion_medida