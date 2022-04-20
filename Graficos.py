
import matplotlib.pyplot as plt 
import os

def get_avg(files, init, jump):
    x = []
    y = []
    for file_txt in files:
        data_file = open(file_txt,"r")
        lines = data_file.readlines()
        data = 0
        for i in range(init, len(lines), jump):
            data = data + float(lines[i].strip("\n"))
        data = data / 100
        y.append(data)
        aux = file_txt.strip("Tiempo")
        x.append(aux.strip(".txt"))
    return x, y

def get_data(flag):
    x = []
    y = []
    color = []
    if(flag == 0):
        files = ["TiempoChaCha20.txt", "TiempoAES_ECB.txt", "TiempoAES_GCM.txt"]
        x, y = get_avg(files, 0,2)
        color = ['blue','red','green']
    elif(flag == 1):
        files = ["TiempoChaCha20.txt", "TiempoAES_ECB.txt", "TiempoAES_GCM.txt"]
        x, y = get_avg(files, 1,2)
        color = ['blue','red','green']
    elif(flag == 2):
        files = ["TiempoSHA2_384.txt", "TiempoSHA2_512.txt", "TiempoSHA3_384.txt", "TiempoSHA3_512.txt"]
        x, y = get_avg(files, 0,1)
        color = ['blue','red','green']
    return x, y, color

def get_graphic():
    flag = [0, 1, 2]
    values = ["Cifrado", "Descifrado", "Hash", "Firma"]
    fig = plt.figure(figsize = (15,7.5))
    fig.subplots_adjust(hspace = 0.9, wspace = 0.75)
    for i in flag:
        ax = fig.add_subplot(2, 2, i + 1)
        x, y, color = get_data(i)
        x_aux = []
        for j in range(0,len(x)):
            x_aux.append(j)
        ax.bar(x, y, bottom = 0, log = True, align = "center",  color = color)
        ax.set_xticks(x_aux,x)
        ax.set_ylabel("Promedio de ejecucion")
        ax.set_xlabel("Algoritmo")
        ax.set_title(values[i])
    fig.suptitle("Analisis de datos", fontweight = "bold")
    fig.canvas.manager.set_window_title('Analisis de datos')
    plt.show()
    
get_graphic()