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