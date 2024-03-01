""" 

lista = ["daniel " , 31 , False, "masculino",[69,25,17]]

print (lista)
print (lista[3])

# cambiar el valor de una lista ya determinada

lista [3]= 3116927655
print(lista [3])

# utilizar el insert

lista.insert (3 ,"manzana" )
print (lista)
 """

# lista  sencilla

lista1 = [1, 2.3 ,"hola" ,True]

entero = 100
floatante = 12.3
texto = "adios"
boleano = False
listaInterna= ["estoy dentro", True]

# con variable

lista2=[ entero,floatante,texto,boleano,listaInterna]
""" 
print (lista2) """

#buscando solo un indice
""" print (lista1[2])
 """
#bloque de rango

    #lista1[1:3]= 12 error
  #lista1 [0:4]=[12] cambia todos los itens de la lista y los reemplaza por 12
  # lista1[:] = [12] cambiar todos los itens de la lista y los reemplaza por 12
# lista1=  [] otra forma de cambiar o vaciar toda la lista

# insert(indice,valor)
""" lista2.insert(0, "me modificaron")
print (lista2)
lista2.insert(0,[listaInterna])
print(lista2)
 """
# append(valor)

""" lista2.append(listaInterna)
print(lista2) """

# .extend()

""" lista1.extend(lista2)
lista2.extend(lista1)

print(lista1)
print(lista2) """

# del lista[]
""" del lista1 [0]
del lista2[4]

print (lista1)
print(lista2) """


# remove()

""" lista1.remove("hola")

print(lista1) """

lista3 = [12,1,2,[1,2,[1,2]]]

""" print (lista3)

print (lista3[4])

lista3 [4][2].remove(1)

print (lista3[4][2])
lista3[4].remove(1)
lista3.remove(1)  """
# clear 

""" lista3.clear()
print (lista3) """

""" #.pop()
print(lista3)
lista3.pop()
print (lista3)
lista3.pop(1)
print(lista3) """


"""organizar elementos de una lista
como organizar una lista que tenga numeros y letras
dandole prioridad a los numeros y despues a las letras
"""