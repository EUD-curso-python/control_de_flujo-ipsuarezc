nombre = None
edad  = None
apellido = None

def nombre_completo():
    return nombre + ' ' + apellido

def cumplir_anios():
    global edad
    edad += 1
    