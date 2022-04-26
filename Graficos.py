
import matplotlib.pyplot as plt 
import os

def get_avg(files):
    x = []
    y = []
    for file_txt in files:
        data_file = open(file_txt,"r")
        lines = data_file.readlines()
        avg = 0
        for i in range(0, len(lines)):
            avg = avg + float(lines[i].strip("\n"))
        avg = avg / len(lines)
        var = 0
        for i in range(0, len(lines)):
            var = var + (float(lines[i].strip("\n")) - avg)**2
        var = (var/(len(lines)-1))**(1/2)
        data = 0
        aux = 1
        incorrect_values = open("FueraDeRango.txt", 'a')
        incorrect_values.write("-----------------------------------------\n{}\nCondicion: {} < X < {}\nValores fuera de rango:\n".format(file_txt, avg - var, avg + var))
        for i in range(0, len(lines)):
            value = float(lines[i].strip("\n"))
            if((avg - var) < value < (avg + var)):
                aux = aux + 1
                data = data + value
            else:
                incorrect_values.write("{}\n".format(value))
        incorrect_values.close()
        data = data / aux
        y.append(data)
        aux = file_txt.strip("Tiempo")
        aux = aux.strip(".txt")
        x.append(aux + "\n" + f"{data:.6f}" + "[s]")
    return x, y

def get_data(flag):
    x = []
    y = []
    color = []
    if(flag == 0):
        files = ["TiempoChaCha20_C.txt", "TiempoAES_ECB_C.txt", "TiempoAES_GCM_C.txt", "TiempoRSA_OAEP_C.txt"]
        x, y = get_avg(files)
        color = ['blue','red','green', 'purple']
    elif(flag == 1):
        files = ["TiempoChaCha20_D.txt", "TiempoAES_ECB_D.txt", "TiempoAES_GCM_D.txt", "TiempoRSA_OAEP_D.txt"]
        x, y = get_avg(files)
        color = ['blue','red','green', 'purple']
    elif(flag == 2):
        files = ["TiempoSHA2_384.txt", "TiempoSHA2_512.txt", "TiempoSHA3_384.txt", "TiempoSHA3_512.txt"]
        x, y = get_avg(files)
        color = ['blue','red','green', 'purple']
    elif(flag == 3):
        files = ["TiempoRSA_PSS_S.txt", "TiempoECDSA_PRIME_FIELD_S.txt", "TiempoECDSA_BINARY_FIELD_S.txt"]
        x, y = get_avg(files)
        color = ['blue','green', 'red']
    elif(flag == 4):
        files = ["TiempoRSA_PSS_V.txt", "TiempoECDSA_PRIME_FIELD_V.txt", "TiempoECDSA_BINARY_FIELD_S.txt"]
        x, y = get_avg(files)
        color = ['blue', 'green', 'red']
    return x, y, color

def get_graphic():
    flag = [0, 1, 2, 3, 4]
    values = ["Cifrado", "Descifrado", "Hash", "Firma", "Verificacion"]
    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.9, wspace = 0.75)
    for i in flag:
        ax = fig.add_subplot(3, 2, i + 1)
        x, y, color = get_data(i)
        x_aux = []
        for j in range(0,len(x)):
            x_aux.append(j)
        ax.bar(x, y, bottom = 0, log = True, align = "center",  color = color)
        ax.set_xticks(x_aux,x)
        ax.set_ylabel("Promedio de ejecución")
        ax.set_xlabel("Algoritmo")
        ax.set_title(values[i])
    fig.suptitle("Análisis de datos", fontweight = "bold")
    fig.canvas.manager.set_window_title('Análisis de datos')
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.show()
    
get_graphic()
