import math
import random
#from random import uniform, random, choice, sample
TABLERO_FILAS=3     #Defino el valor de las filas
TABLERO_COLUMNAS=3  #Defino las columnas
tablero=[]          #Un vector lineal sera nuestro almacen todas las tiradas
fila=3              #Fila de prueba     
columna=3           #Columna de prueba 
pieza=""
fichasColocadas=1
casillasVasias=[]   #Casillas vasias 

                    #Primero que nada vamos a definir las casillas optimas para las tiradas
                    #Despues de realizar varia jugadas en una libreta     
                    #Los lugares más optimos es el central y las esquinas y los comenzaremos a definir 
                    #
                    #Tambien se tendra que ver si se nos puede ganar el otro jugador o no y conforme a ello 
                    #Se tomara la decision para la tirada.     
casillasOptimasX=[1,3,1,3]
casillasOptimasY=[1,1,3,3]
casillasOptimasSecundarias=[1,3,7,9]
casillasOptimasPrimarias=[5]
                    #Esas son las pocisiones optimas secundarias pero tambien tendremos que tener
                    #Las pocisiones optimas primarias, hasta el momento solo he definido una pos 
                    #Como primaria y es el centro 
casillasOptimasX=[2]
casillasOptimasY=[2]


i=1
for i in range(10):
	tablero.append(' ')
	casillasVasias.append(i) 

def casVasia(valor):
    contador=1            
    while(contador<=9):
        #print(casillasVasias[contador])
        if(casillasVasias[contador]==valor):
            casillasVasias[contador]=90
            return True
        contador+=1        

def recorridoPrinciopal(can):
    for ai in range(1):
        if(casillasOptimasPrimarias[ai]==can):
            return True

def recorridoSecundario(can):
    for aii in range(4):
        if(casillasOptimasSecundarias[aii]==can):
            return True

def minmax():
    valor=random.randint(1,9)
    if(casVasia(valor) and recorridoSecundario(valor)):
        return valor
    else:       
        while(True):
            valor=random.randint(1,9)
            if(casVasia(valor)):
                return valor
    


def numeroFicha():
    while(True):
        valor=minmax()
        return valor

#print(numeroFicha())

def colocarFicha(valore):
    pos=numeroFicha()
    print("La pos a colocar es: ",pos)
    #print("Esta o no desocupada la pos",casVasia(pos))
    if(pos!=0):
        tablero[pos]=valore
        return 1

def pintarTablero():
	pos=1
	for fila in range(3):
		for columna in range(3):
			print("| ",tablero[pos]," ", end=" ")
			pos+=1
		print("|\n",("-"*20))	


while(fichasColocadas<=9):  
    numeroComputadora=(fichasColocadas&1)
    valor=random.uniform(5, 10)
    print(" "," ")
    if(numeroComputadora==1):
        pieza="0"
        fichasColocadas+=colocarFicha(pieza)
    else:
        pieza="x"
        fichasColocadas+=colocarFicha(pieza)
    pintarTablero()     
print("////////////////////////////////////////////////////////////")

