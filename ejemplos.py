#Mas ejemplos de decoradores utiles, seguimos usando el patrón visto en la explicación

import functools

#Este es nuestro modelo de decorador
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        #hace algo antes 
        value = func(*args, **kwargs)
        #Hace algo despues
        return value
    return wrapper_decorator

#Seguimos añadiendo los decoradores en nuestro modulo de decorators.py

from decorators import timer

@timer
def waste_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])

waste_time(1)

#De esta forma si escribiesemos waste_time(100) el resultado seria: Terminada la función waste_time() in 0.1727 secs
# Y en el caso de escrubir waste_time(900) el resultado seria: Terminada la función waste_time() in 1.5520 secs

from decorators import debug

@debug
def dar_bienvenida(name, age=None):
    if age is None:
        return f"Hola {name}!"
    else:
        return f"Wow {name}, ya tienes {age} años, como has crecido!"

dar_bienvenida("Martin")

#Obtendremos este resultado 
#Llamando a dar_bienvenida('Martin')
#dar_bienvenida() devolvió 'Hola Martin!'

#Si le pasamos el argumento edad:

dar_bienvenida("Martin", 25)
#Llamando a dar_bienvenida('Martin', 25)
#dar_bienvenida() devolvió 'Wow Martin, ya tienes 25 años, como has crecido!'

#Vamos a crear un funcion de cuenta regresiva en la que inlcuiremos el decorador slow_down
from decorators import slow_down

@slow_down
def countdown(number):
    if number >= 1:
        print(number)
        countdown(number - 1)
    else:
        print ("Se acabó")

countdown(5)

#Al ejecutar este codigo tenemos una pausa de 1 segundo entre cada llamada a la función countdown

#Los decoradores no siempre tienen por que hacer wrap a la función que están decorando. Pueden simplemente registrar que una función existe y devolveral sin wrap.
#Vamos a crear por ejemplo una arquitectura de plugins ligera. --> decorators.py

from decorators import PLUGINS, register_func

@register_func
def decir_buenas(nombre):
    return f"Hola {nombre}"

@register_func
def decir_adios(nombre):
    return f"Hasta luego {nombre}"

print (PLUGINS)

#Al imprimir nuestro diccionario obtendremos las funciones que ha almacenado: {'decir_buenas': <function decir_buenas at 0x7f4a57dadab0>, 'decir_adios': <function decir_adios at 0x7f4a57dadb40>}


#Ahora podemos usar nuestro diccionario de plugins para llamar a estas funciones

import random

def random_interaction(nombre):
    nombre_func, func = random.choice(list(PLUGINS.items()))
    print(f"Usando{nombre_func!r}") #!r tiene la misma función que el repr que hemos visto anteriormente
    return func(nombre)

print(random_interaction("Martin"))

#Hemos creado una funcion que nos devuelva de forma aleatoria una de las funciones almacenadas en el diccionario de Plugins y nos indique cual de esas funciones estamos utilizando para al final devolver el resultado de la función
#Usando'decir_buenas'
#Hola Martin