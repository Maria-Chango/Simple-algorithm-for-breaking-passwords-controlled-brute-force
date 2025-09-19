import time
import matplotlib.pyplot as plt

minusculas = ['a','b','c','d','e','f','g','h','i','j',
              'k','l','m','n','o','p','q','r','s','t',
              'u','v','w','x','y','z']
mayusculas = ['A','B','C','D','E','F','G','H','I','J',
              'K','L','M','N','O','P','Q','R','S','T',
              'U','V','W','X','Y','Z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
digitos = ['!','@','#','$','%','&']

alfabeto = minusculas + mayusculas + numeros + digitos


def probar(longitud, actual, objetivo, intentos):
    if len(actual) == longitud:
        intentos[0] += 1
        iguales = True
        for i in range(longitud):
            if actual[i] != objetivo[i]:
                iguales = False
                break
        if iguales:
            return True
        return False

    for c in alfabeto:
        nuevo = actual + [c]  
        if probar(longitud, nuevo, objetivo, intentos):
            return True
    return False

def romper(objetivo):
    intentos = [0]
    inicio = time.time()
    longitud = 1
    while True:
        if probar(longitud, [], list(objetivo), intentos):
            fin = time.time()
            return intentos[0], fin - inicio, longitud
        longitud += 1

# -------- PRUEBAS VARIAS --------
claves = [ "abc"]

tiempos = []
longitudes = []

for clave in claves:
    intentos, duracion, lon = romper(clave)
    print("Contraseña encontrada:", clave)
    print("Intentos:", intentos)
    print("Tiempo:", duracion, "segundos\n")
    tiempos.append(duracion)
    longitudes.append(len(clave))

# Gráfico: tiempo en X y longitud en Y
plt.plot(tiempos, longitudes, linestyle='-', marker='o')
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Longitud de contraseña")
plt.title("Longitud vs Tiempo en ataque de fuerza bruta")
plt.grid(True)
plt.show()
