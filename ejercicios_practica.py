#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números
    print("Ingrese dos numeros")
    numero_1 = float(input())
    numero_2 = float(input())

    resta = numero_1 - numero_2
    
    if resta > 0:
      print("El restulado es positivo")
    elif resta < 0:
      print("El resultado es negativo")
    else:
      print("El resultado es igual a cero")


    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
        
    '''

def ej2():
# Ejercicios de práctica con números

    print("Ingrese tres numero")
    numero_1 = int(input())
    numero_2 = int(input())
    numero_3 = int(input())

    division = numero_1 % 2
    if division == 0:
      print("numero par")
    else:
      print("numero impar")  
  
    division = numero_2 % 2
    if division == 0:
      print("numero par")
    else:
      print("numero impar")  

    division = numero_3 % 2
    if division == 0:
      print("numero par")
    else:
      print("numero impar")  



  
    #Realice un programa que solicite el ingreso de tres números
    #enteros, y luego en cada caso informe si el número es par
    #o impar.
    #Para cada caso imprimir el resultado en pantalla.
    

def ej3():
    # Ejercicios de práctica con números

    numero_1 = float(input("Ingrese el primer numero: \n"))
    numero_2 = float(input("ingrese el segundo numero: \n"))

    print("ingrese la operacion que desea realizar")
  
    operacion = input()
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    multiplicacion = numero_1 * numero_2
    division = numero_1 / numero_2
    potencia = numero_1 ** numero_2

    if operacion == "+":
      print("la suma es",suma)
    elif operacion == "-":
      print("la resta es:",resta) 
    elif operacion == "*":
      print("la multiplicacion es:",multiplicacion)
    elif operacion == "/":
      print("la division es:",division)
    elif operacion == "**":
      print(numero_1,"elevado a",numero_2,"es:",potencia)
    else:
      print("operacion invalida")

    
    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    

    '''

def ej4():
    # Ejercicios de práctica con cadenas
    
    print("ingrese tres palabras")
    palabra_1 = str(input())
    palabra_2 = str(input())
    palabra_3 = str(input())
    
    print("ingrese la operacion que quiere realizar")
    numero = int(input())

    if numero == 1:
      if (palabra_1 < palabra_2 < palabra_3):
        print(palabra_3,palabra_2,palabra_1)
      elif (palabra_1 < palabra_3 < palabra_2):
        print(palabra_2,palabra_3,palabra_1)
      elif (palabra_2 < palabra_1 < palabra_3):
        print(palabra_3,palabra_1,palabra_2)
      elif (palabra_2 < palabra_3 < palabra_1):
        print(palabra_1,palabra_3,palabra_2)
      elif (palabra_3 < palabra_1 < palabra_2):
        print(palabra_2,palabra_1,palabra_3)    
      elif (palabra_3 < palabra_2 < palabra_1):
        print(palabra_1,palabra_2,palabra_3)
      
    if numero == 2:
      if len(palabra_1) <= len(palabra_2) <= len(palabra_3):
        print(palabra_3,palabra_2,palabra_1)
      elif len(palabra_1) <= len(palabra_3) <= len(palabra_2):
        print(palabra_2,palabra_3,palabra_1)
      elif len(palabra_2) <= len(palabra_1) <= len(palabra_3):
        print(palabra_3,palabra_1,palabra_2)
      elif len(palabra_2) <= len(palabra_3) <= len(palabra_1):
        print(palabra_1,palabra_3,palabra_2)
      elif len(palabra_3) <= len(palabra_1) <= len(palabra_2):
        print(palabra_2,palabra_1,palabra_3)
      elif len(palabra_3) <= len(palabra_2) <= len(palabra_1):
        print(palabra_1,palabra_2,palabra_3)

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor

  '''

def ej5():
    # Ejercicios de práctica con números
    
    print("Igrese el valor de las temperaturas de los ultimos tres dias")

    temperatura_1 = float(input())
    temperatura_2 = float(input())
    temperatura_3 = float(input())

    maximo = max(temperatura_1,temperatura_2,temperatura_3)
    promedio = (temperatura_1 + temperatura_2 + temperatura_3) / 3

    print("la temperatura mayor es",maximo)
    print("la temperatura menor es",min(temperatura_1,temperatura_2,temperatura_3))
    print("la temperatura promedio es",promedio)

    # Inove: Perfecto que hayas aprovechado las funciones de "max" y "min" para
    # el cálculo, esas y otras funciones las veremos la clase que viene
    # junto con los métodos de bucles o loops, y listas.

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado  

    '''

if __name__ == '__main__':
    #print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
