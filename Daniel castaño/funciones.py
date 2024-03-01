""" # FUNCIONES
# SIN ARGUMENTOS
def saludar (): # sirve para seguir el codigo sin generar error . cuando no se que poner
  print ("hola soy funcion saludar")


saludar()

# FUNCION CON ARGUMENTOS

def saludopersonalizado(nombre):
  print ("bienvenido a los juegos del hambre", nombre)

saludopersonalizado("daniel" )
saludopersonalizado (12544)

# para que el usuario ingrese algo 
ingresanombreUsuario = input ("dame tu nombre  ")

saludopersonalizado (ingresanombreUsuario)

# FUNCIONES CON RETORNO 
    # funcion numero par 
def espar(numero):
  if numero %2 == 0:
    return f"el numero {numero} es par"
  else:
    return  f"el numero, {numero} , es impar"
print (espar(123))
 """
""" def esimpar ():
    numero = int(input ("ingresa tu numero "))
    if numero % 2 != 0:
     print ( f"el numero {numero} es impar")

    if not (numero % 2 == 0):
       print(f"el numero {numero} es impar")
       """
""" esimpar()
 """
# crear una funcion que diga si es mayor de edad
# debe de recibir la edad del usuario
# si es mayor imprimir "eres mayor de edad

def esMayorEdad (edad2):
   if edad2 >= 18:
      return "eres mayor edad "

edad2 = int(input("dame tu edad : "))
print (esMayorEdad(edad2))

def mayoredad ():
   edad = int (input("ingrese su edad "))
   if edad >= 18 :
     return f"eres mayor de edad"
  

def menoredad():
   edadM= int (input("ingrese su edad "))
   if edadM <18 :
      return f"no puedes ingresar "
 
# dato NONE : es una funcion que no retorna nada