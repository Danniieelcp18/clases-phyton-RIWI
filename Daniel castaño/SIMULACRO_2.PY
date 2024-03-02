# FIESTA CON AMIGOS EN UNA DISCOTECA


#1 LOS AMIGOS DEBEN TENER LA EDAD >= 18 O >=30 YA LA LISTA LA ENVIARO

#2 DECIDIR QUE LICOR TOMAR DE UNA LISTA ENVIADADA DE LA DISCOTECA

# 3 CALCULAR EL TOTAL DEL COVER QUE PAGA VALOR 15000 X PERSONA

#4 EN UN BUCLE PERMITIR QUE LICOR DESEA TOMAR SEBASTIAN
   # PERMITIR VERIFICAR EL LICOR DE LA LISTA Y RESTARLO DEL SALDO DE JULIAN
  # REPETIR ESTE PROCESO HASTA QUE JULIAN DESEE NO TOMAR MAS LICOR

# CALCULAR SALDO FINAL QUE SE GASTA 
   #  SUMARLE 20000 DE TAXI AL FINAL  DE Y MOSTRARLO EN PANTALLA

dineroSebast = float (input("cuanto dinero tienes sebastian ? "))
listaAamigos= [20,32,22,65,17]
edadIngreso = ">= 18 o <=30"
cover = 15000
taxi = 20000
licorDisco = (("ron " , 50000), ("vodka",40000) ,("ginebra" ,60000),("whisky", 80000),("cerveza" ,10000), ("tequila", 70000),("bandy",55000),("cognac",900000) , ("licorcafe" ,45000) )
contador= 0
# comparacion de edad de los amigos para comprobar el ingreso
# el for sirve para comparar y llamar una lista con variable
for x in listaAamigos:
  if x >=18 and x <= 30:
      contador  = contador +1
      print (f"la edad {x}  de amigo puede ingresar  ")
  else :
    print (f"la edad {x}  de amigo no puede ingresar " ) 

ingresAmigo = contador * 15000
print (f"el valor a pagar del cover es ", ingresAmigo)
