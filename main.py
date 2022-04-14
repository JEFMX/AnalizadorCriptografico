from Chacha20 import ChaCha20_algoritmo
import random
import string

def generacion_vector_prueba():
    for i in range(100):
        longitud_vector = random.randint(10,300)
        vector_prueba = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(longitud_vector))
        archivo = open("vectores.txt", 'a')
        archivo.write(vector_prueba + '\n')

def main():
    generacion_vector_prueba()
    archivo = open("vectores.txt", 'r')
    linea = archivo.readlines()
    p = 0
    for i in linea: 
        p += 1
        print("Porcentaje: {}%".format(p))
        ChaCha20_algoritmo(i.strip('\n'))
main()