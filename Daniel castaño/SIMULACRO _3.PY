# PRUEBA 3

# GRUPO DE INGENIERO Y CIENTIFICOS DEBEN CUMPLIR 4 TAREAS



# # 1 )SUMAR INGENIERO INGRESADOS POR 2 AÑOS 
ingeIngresados = int (input( ("""TAREAS DE LABORATORIO ESPACIAL 
      BIENVENIDOS !!! 
                Cuanto profesionales ingresaron estos 2 años
                Dijite su numero : """)))



sumaIngenier= ingeIngresados * 1 

print("la cantidad de ingenineros ingresados en dos años es :",sumaIngenier)

# 2 ) RESTAR GASTOS 
presuInici= float (input("""Ingrese su presupuesto Inicial"""))
valorGastado= float (input("""Ingrese su gasto """))
saldoFinal= presuInici -valorGastado

print (" el saldo  final es : ",saldoFinal)

# 3) CALCULAR COMBUSTIBLE  GASTADO EN HORAS PERO LA MISION ES En DIAS


diasMision= int (input(""" HOLA , CIENTIFICOS.
                       Cuantos dias dura la mision: """))
combustible =  float (input("""ingrese conbustible que consume 
                            la nave de galones por hora """))

hora = 24


consumo = (diasMision * hora) 

final = combustible * consumo
print (" el combustible de la mision es : " ,final, "galones por hora ")


# 4)CALCULAR VELOCIDAD PROMEDIO

distancia = float (input("""HOLA , CIENTIFICOS
                         CUAL ES LA DISTANCIA QUE RECORREMOS ? EN KL/H """))

VeloPromedi = distancia / diasMision

print ("La velocidad promedio del recorrido es :" , VeloPromedi, " kilometro/hora ")