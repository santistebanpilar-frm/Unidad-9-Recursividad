#Trabajo Practico Unidad 9 Recursividad - Pilar Santisteban
#EJERCICIO 1
#Crea una función recursiva que calcule el factorial de un número. 
#Luego, utiliza esa función para calcular y mostrar en pantalla el  factorial de todos los números enteros entre 1 y el número que indique el usuario
print("----------------- EJERCICIO 1 -----------------")
def factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

num : int = int(input("Ingrese un numero para calcular su factorial: "))
while num < 1:
    num : int = int(input("Ingrese un numero entero mayor o igual 1: "))
else:
    print(f"Los factoriales desde 1 hasta {num} son: ")
    for i in range(1, num + 1):
        print(f"{i}! = {factorial(i)}")  

#EJERCICIO 2
#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
#Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
print("----------------- EJERCICIO 2 -----------------")
def fibonacci(num:int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
num : int = int(input("Ingrese la posicion de la serie Fibonacci que desea calcular: "))
while num < 0:
    num : int = int(input("Ingrese un numero entero mayor o igual a 0: "))
else:
    print(f"La serie Fibonacci hasta la posicion {num} es: ")
    for i in range(num + 1):
        print(fibonacci(i), end=" ")
    print()

#EJERCICIO 3
#Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). 
# Prueba esta función en un algoritmo general.
print("----------------- EJERCICIO 3 -----------------")
def potencia(base: float, exponente:int) -> float:
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)
base : float = float(input("Ingrese la base en formato 0.0: "))
while base.is_integer() == False:
    base : float = float(input("Ingrese un numero valido para la base: "))
exponente : int = int(input("Ingrese el exponente, debe ser un numero entero mayor o igual a 0): "))
if exponente < 0:
    exponente : int = int(input("Ingrese un exponente entero mayor o igual a 0: "))
else:
    print(f"{base} elevado a la {exponente} es: {potencia(base, exponente)}")


#EJERCICIO 4
#Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
print("----------------- EJERCICIO 4 -----------------")
def decimal_a_binario(num:int) -> str:
    if num == 0:
        return "0"
    else:
        return decimal_a_binario(num // 2) + str(num % 2)
num : int = int(input("Ingrese un numero entero positivo para convertir a binario: "))
while num < 0:
    num : int = int(input("Ingrese un numero entero positivo: "))
else:
    print(f"La representacion binaria de {num} es: {decimal_a_binario(num)}")

#EJERCICIO 5
#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo 
# o False si no lo es. Requisitos: La solución debe ser recursiva. No se debe usar [::-1] ni la función reversed()
print("----------------- EJERCICIO 5 -----------------")
def es_palindromo(palabra: str, i: int = 0, j: int = None) -> bool:
    palabra = palabra.lower().strip()
    if j is None:
        j = len(palabra) - 1
    if i >= j:
        return True
    if palabra[i] != palabra[j]:
        return False
    return es_palindromo(palabra, i + 1, j - 1)

palabra = input("Ingrese una palabra (sin espacios ni tildes): ").strip()
resultado = es_palindromo(palabra)
print(f"¿'{palabra}' es palíndromo? {resultado}")
#EJERCICIO 6
#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
#Restricciones: No se puede convertir el número a string. Usá operaciones matemáticas (%, //) y recursión.
print("----------------- EJERCICIO 6 -----------------")
def suma_digitos(num:int) -> int:
    if num == 0:
        return 0
    return num % 10 + suma_digitos(num // 10)
num : int = int(input("Ingrese un numero entero positivo para sumar sus digitos: "))
while num < 0:
    num : int = int(input("Ingrese un numero entero positivo: "))
else:
    print(f"La suma de los digitos de {num} es: {suma_digitos(num)}")

#EJERCICIO 7
#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar 
# al último nivel con un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el 
# total de bloques que necesita para construir toda la pirámide
print("----------------- EJERCICIO 7 -----------------")
def contar_bloques(num:int) -> int:
    if num == 1:
        return 1
    return num + contar_bloques(num - 1)   
num : int = int(input("Ingrese la base de la piramide (numero de bloques en el nivel mas bajo): "))
while num <= 0:
    num : int = int(input("Ingrese un numero entero mayor a 0: "))
else:
    print(f"La cantidad de bloques necesarios para construir la piramide es: {contar_bloques(num)}")

#EJERCICIO 8
#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y 
# devuelva cuántas veces aparece ese dígito dentro del número
print("----------------- EJERCICIO 8 -----------------")
def contar_digito(numero:int, digito:int) -> int:
    if numero == 0:
        return 0
    contador = 1 if numero % 10 == digito else 0
    return contador + contar_digito(numero // 10, digito)
num : int = int(input("Ingrese un numero entero positivo: "))
digito : int = int(input("Ingrese un digito entre 0 y 9: "))
while num < 0 or digito < 0 or digito > 9:
    print("Ingrese valores validos.")
    num : int = int(input("Ingrese un numero entero positivo: "))
    digito : int = int(input("Ingrese un digito entre 0 y 9: "))
else:
    print(f"El digito {digito} aparece {contar_digito(num, digito)} veces en el numero {num}.")
