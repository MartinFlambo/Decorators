def repetir(func):
    def wrapper_repetir():
        func()
        func()
    return wrapper_repetir

#Este decorador llama a la función decorada dos veces
#Importamos este decorador en nuestro archivo --> explicacion.py

def repetir(func):
    def wrapper_repetir(*args, **kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_repetir

#Ahora el decorador acepta cualquier numero de argumentos que se lo pase a la función que está decorando

def repetir(func):
    def wrapper_repetir(*args, **kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper_repetir

#Ahora el decorador retorna el valor de la ultima llamada a la funcion decorada

#Vamos a añadir un decorador que nos permita corregir el problema de trazabilidad que teniamos con nuestra función
import functools

def repetir(func):
    @functools.wraps(func)
    def wrapper_repetir(*args, **kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper_repetir


#Este decorado nos ayudará a saber el tiempo que tardan en ejecutarse nuestras funciones
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args,**kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Terminada la función {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer

#Ahora vamos con un decorador que nos imprima los argumentos de nuestras funciones el valor que nos devuelven cada vez que las invocamos

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Llamando a {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() devolvió {repr(value)}")
        return value
    return wrapper_debug

#Este codigo funciona de la siguiente manera:
#Creamos una lista de los argumentos posicionales, usamos repr() para obtener un string que representa cada argumento
#Creamos una lista de los argumentos de palabras clave, la funcion formatea cada argumento como clave = valir y volvemos a usar repr() para obtener un string con los valores
#En el signature unimos la lista de argumentos posicionales y argumentos de palabras clave en un string para cada argumento
#despues devolvemos el resultado cuando la funcion se ha ejecutado


#El siguiente decorador nos permite ralentizar la ejecución de nuestro código, imaginemos que tenemos una función que comprueba si ha habido cambios por ejemplo en una pagina web. Esto puede ser util para limitar la frecuencia con la que una función accede a un recurso como puede ser una API o una web para evitar sobrecargas. Tambien puede ser util para simular demoras artificial y observar el comportamiento del sistema

def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args,**kwargs):
        time.sleep(1)
        return func(*args,**kwargs)
    return wrapper_slow_down

#Vamos a crear nuestro diccionario de Plugins y crear nuestro decorador

PLUGINS = dict()

def register_func(func):
    PLUGINS[func.__name__] = func
    return func

#Vamonos a ver un ejemplo de como registramos un par de funciones --> ejemplos.py