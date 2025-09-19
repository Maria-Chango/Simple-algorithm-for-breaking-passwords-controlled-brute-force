import time
import matplotlib.pyplot as plt


minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"

alfabeto = minusculas + mayusculas + numeros

def probar_contraseña(contraseña_probar, objetivo, intentos):
    intentos[0] += 1
    if contraseña_probar == objetivo:
        return True
    
    
    if len(contraseña_probar) >= len(objetivo):
        return False
        
    for char in alfabeto:
        if probar_contraseña(contraseña_probar + char, objetivo, intentos):
            return True
            
    return False


def ejecutar_ataque(contraseña_objetivo):
    intentos_totales = [0]
    tiempo_inicio = time.time()
    
    print(f"Ataque de fuerza bruta para: '{contraseña_objetivo}'")
    
    encontrada = probar_contraseña("", contraseña_objetivo, intentos_totales)
    
    tiempo_fin = time.time()
    duracion = tiempo_fin - tiempo_inicio

    if encontrada:
        print(f"Contraseña encontrada: '{contraseña_objetivo}'")
        print(f"Intentos realizados: {intentos_totales[0]:,}")
        print(f"Tiempo de ejecución: {duracion:.4f} segundos")
        return duracion, intentos_totales[0]
    else:
        print("La contraseña no fue encontrada")
        return None, None

# ----- PROGRAMA CON LAS CLAVES DESIGNADAS--------
claves_de_prueba = ["a","ab", "abc"] 
tiempos = []
longitudes = []

print("-" * 30)

for clave in claves_de_prueba:
    duracion, intentos = ejecutar_ataque(clave)
    if duracion is not None:
        tiempos.append(duracion)
        longitudes.append(len(clave))
    print("-" * 30)

# --- GRAFICA---
if tiempos:
    plt.figure(figsize=(10, 6))
    plt.plot(longitudes, tiempos, marker='o', linestyle='-', color='b')
    plt.title("Rendimiento del Ataque de Fuerza Bruta")
    plt.xlabel("Longitud de la Contraseña")
    plt.ylabel("Tiempo de Ejecución en segundos")
    plt.grid(True)
    plt.show()
