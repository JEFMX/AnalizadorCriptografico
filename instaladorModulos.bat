REM Este archivo se encarga de instalar lo modulos de python para el Analizador Criptografico
@echo on
REM Instalacion del modulo python que contien el set de algoritmos
pip install pycryptodome
timeout 1
REM Instalacion del modulo python matplotlib para graficar
pip install matplotlib
timeout 1
REM Instalacion del modulo python ecdsa para curvas elipticas
pip install ecdsa
timeout 1
REM Instalacion del modulo python ecdsa BF Koblitz Curve para curvas elipticas 
pip install cryptography
timeout 1
REM Instalacion del modulo python ecdsa BF Koblitz Curve para curvas elipticas 
pip install psutil
timeout 1
echo Complete
timeout 5