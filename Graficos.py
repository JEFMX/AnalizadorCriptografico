import matplotlib.pyplot as plt 
import sys
import os

def get_data_cipher():
    files_path = os.path.abspath(os.getcwd())
    file_extension = r".txt"
    files = [_ for _ in os.listdir(files_path) if _.endswith(file_extension)]
    x = []
    for file_txt in files:
        aux = file_text.strip("Tiempo")
        x.append(aux.strip(".txt"))
        data_file = open(file_txt,"r")
        lines = data_file.readlines()
        data = 0
        for i in (0,100,2):
            data = data + float(lines[i].strip("\n"))
        data = data / 100
    y = []
    y.append(data)
    return x, y

def get_graphic_cipher():
    x, y = get_data_cipher()
    plt.bar(x, y)
    plt.ylabel("Promedio de ejecucion")
    plt.xlabel("Algoritmo")
    plt.title("Cifrado")
    plt.show()

get_graphic_cipher()

