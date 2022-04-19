import matplotlib.pyplot as plt 
import numpy as np
import sys
import os

def get_data_cipher():
    files_path = os.path.abspath(os.getcwd())
    file_extension = r".txt"
    files = [_ for _ in os.listdir(files_path) if _.endswith(file_extension)]
    x = []
    y = []
    for file_txt in files:
        data_file = open(file_txt,"r")
        lines = data_file.readlines()
        if(len(lines) >= 200):
            data = 0
            for i in range(0,200,2):
                data = data + float(lines[i].strip("\n"))
            data = data / 100
            y.append(data)
            aux = file_txt.strip("Tiempo")
            x.append(aux.strip(".txt"))
    #y = np.array(y)
    return x, y

def get_graphic_cipher():
    x, y = get_data_cipher()
    x_aux = []
    for i in range(0,len(x)):
        x_aux.append(i + 1)
    plt.bar(x_aux, y, bottom = 0, log = True, align = "center")
    plt.xticks(x_aux,x)
    plt.ylabel("Promedio de ejecucion")
    plt.xlabel("Algoritmo")
    plt.title("Cifrado")
    plt.show()

get_graphic_cipher()
