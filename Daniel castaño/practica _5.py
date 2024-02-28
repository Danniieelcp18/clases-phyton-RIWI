"""  # lista de numeros pares e impares del 10 a 30 CON RANGE
pares = list (range (10,31,2))

print (pares)

impares = list(range (11,30,2))

print (impares)
# multiplos de 4 entre el 10 y 40

multiplos= list(range(12,41,4))
print(multiplos)

 # imprimir una lista del 0-10

lista0_10 = range(11)
print ( list (lista0_10))

# imprimir lista del 5-8

lista5_8= range (5,9)
print (list(lista5_8))

# imprimir los multiplos de 5 de 1 al 10
multiplo_5 = range(5,11,5)
print (list (multiplo_5))

#conteo regresivo del 5 
conteo = range(5,-1,-1)
print (list (conteo))
 """
# lista del 0 a 10 e imprima los numero pares e impares
""" for intem in range(11):
  print ("yo soy el ciclo numero " , intem)
  if (intem % 2 ==0):
    print ( " el valor de ciclo es par ", intem)

  else :
    print ( "este numero es impar ", intem) 
 """
""" """ # tabla multiplicar donde el usuario ingrese el numero de la tabla que quiere ver
""" tablamult= input("ingrese el numero de la tabla que desee :")

for numero in range(1,11):
  print (tablamult, "*" ,numero,"=", int(tablamult)*numero) """

# comparativo de edad en una discoteca para ver si continua la fiesta o no 

  
""" edad = int (input("digame su edad "))

while (edad >=18):
  print ("siga la fiesta ")
  edad = int (input("indique su edad "))

if  (edad<18) :
    print ("se nos acabo la fiesta")
     """

# imprimir los numero del 1 al 10

""" numue = range(1,11,1)
print ("lista de numero del 1 a 10")
print (list(numue))

 """
#calcular la suma de los numero del 1 al 100

""" print ("esta es la suma consecutiva de los numero de 1 a 100")
for numero in range (0,100,):
  print ("la suma de 1 +", numero ,"es",(numero +1 ))

  """

# generar una tabla de multiplicar para un numero dado por el usuario

numero = int(input ("dijete el numero de la tabla que desea escogiste el numero : "))

for tablaMulti in range (1,12):
  print (numero ,"*", tablaMulti ,"=" , int(numero)* tablaMulti)


# con el while realizar un menu para un cajero electronico que con un saldo inicial
#dado puedan realizar las operaciones mostrar saldo retirar y consignar.