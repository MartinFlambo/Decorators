#Creamos una funcion
def hola(name):
    return f"Hola compa {name}"

#Creamos otra funcion que toma como atributo la otra funcion, ya que las funciones pueden ser pasadas como argumentos como cualquier otro objeto
def saludar_martin(hola):
    return hola("martin")

#Hacemos un print para comprobar que funciona
print(saludar_martin(hola))


#Inner Functions
#Es posible definir funciones dentro de otras funciones

def padre():
    print("Printing from padre()")

    def primer_hijo():
        print("Printing from primer_hijo()")
    
    def segundo_hijo():
        print("Printing from segundo_hijo()")

#Llamada a las funciones de dentro del padre
    segundo_hijo()
    primer_hijo()

#Llamada a la funcion padre para ver que imprime

padre()

#Printing from padre()
#Printing from segundo_hijo()
#Printing from primer_hijo()

#Si intentamos llamada a una de las funciones que han sido definidas dentro del padre nos dará un error


#segundo_hijo()

#NameError: name 'segundo_hijo' is not defined

#Esto se debe a que esas funciones estan definidas en el momento en el que la funcion padre es llamada por lo tanto no existen fuera de esa función

#Python también permite devolver funciones dentro de funciones

def padre(numero):

    def primer_hijo():
        return "Hola, soy Martin"
    
    def segundo_hijo():
        return "Hola, soy Patricia"
    
    if numero == 1:
        return primer_hijo
    else:
        return segundo_hijo

#Importante, estamos retornando las funciones sin parentesis, es decir, estamos devolviendo una referencia a la función

print(padre(1))

#<function padre.<locals>.primer_hijo at 0x7f9cb7ff75b0>

#Si llamasemos directamente la funcion en el if pasaria lo siguiente
# if numero == 1:
#        return primer_hijo()
#    else:
#        return segundo_hijo()

# print(padre(1))
#Hola, soy Martin

################################################################################################################
#DECORADORES
################################################################################################################

def decorador(func):
    def wrapper():
        print("Algo ocurre antes de que se llame a la funcón")
        func()
        print("Algo ocurre despues de que se llame a la función")
    return wrapper

def hola():
    print("Holaaaaa")

hola = decorador(hola)

print(hola)

#Estamos apuntando a la Inner Function wrapper(). Devolvemos wrapper como funcion cuando llamamos al decorador(hola)
#<function decorador.<locals>.wrapper at 0x7ff738d4b5b0>
#Digamos que un decorador envuelve una función modificando su comportamiento

#Ahora un ejemplo en el que el decorador solo se aplicara bajo una determinada circustancia

from datetime import datetime

def no_durante_la_noche(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass #Sss, los vecinos están dormidos
    return wrapper

def hola():
    print("Holaaaaaaa")

hola = no_durante_la_noche(hola)

hola()

#El test del if ha pasado por lo que obtenemos como resultado Holaaaaaa, recordemos que estamos apuntando al wrapper
#Si estas probando esto entre las 22:00 y las 7:00 de la mañana el test fallará y no ocurrirá nada

#Esta forma de utilizar deocradores es digamos un poco tosca, python nos da una herramienta mucho mejor, utilizaremos a partir de ahora el @ para llamar a los decoradores

#Veamolo con el ejemplo anterior de la funcion entre dos prints

def decorador(func):
    def wrapper():
        print("Algo pasa antes de llamar a la función")
        func()
        print("Algo pasa despues de llamar a la funcón")

    return wrapper

@decorador
def hola():
    print("Holaaaaaa")

hola()

#Obtenemos el mismo output que anteriormente
#Algo pasa antes de llamar a la función
#Holaaaaaa
#Algo pasa despues de llamar a la funcón

#Los decoradores son funciones regulares de Python, todas las herramientas que python nos va para su reusabilidad estñan disponibles
#Vamos a crear un modulo donde guardaremos nuestros decoradores para usarlos en las funciones que queramos, decorators.py

from decorators import repetir

@repetir
def hola():
    print("Holaaa")

print(hola())

#Ahora nuestro Holaaa se imprime dos veces ya que hemos decorado la funcion con el decorador repetir

#Que pasa si queremos usar el decorador en una función que acepete algunos argumentos, nos dará un error ya que la funcion wrapper_repetir no toma ningún argumento
#Para solucionar esto usamos *args y **kwargs en la función wrapper para que acepte un numero arbitrario de argumentos

@repetir
def saludo(name):
    print(f"Hola {name}")

saludo("Martin")

#Nuestro output
#Hola Martin
#Hola Martin

#Es importante recordar que le estamos pasando un argumento a la función por lo que debemos procupar que no se nos olvide al llamarla

#Habremos notado que en muchas ocasiones las llamadas a nuestras funciones nos estan devolviendo un None como resultado, esto es porque nuestro decorador repetir de vuelve ningún valor en concreto

#Para arreglar esto volvamos a nuestro modulo de decoradores y realicemos algunos cambios --> decorators.py

@repetir
def saludo(nombre):
    print("Creando saludo")
    return f"Hola {nombre}"

print(saludo("Martin"))

#Esta vez la funcion retorna el saludo con nuestro nombre
#Creando saludo
#Creando saludo
#Hola Martín

#Si inspeccionamos nuestra función hola podemos ver que se ha vuelto un poco confusa sobre su propia identidad. Nos dice que es la función wrapper_repetir del modulo de decoradores

#help(hola)
#Lo dejo comentado para que no interfiera en nuestras ejecuciones de codigo

#Help on function wrapper_repetir in module decorators:
#wrapper_repetir(*args, **kwargs)

#Para areglar esto usaremos en nuestros decoradores @functools.wrap para preservar la información de la función original, vamos a nuestro decorators.py
#Ahora se nos mostrará lo siguiente
#Help on function hola in module __main__:
#hola()
