import sympy as sp
import numpy as np

# Declaramos la variable s
s, K = sp.symbols('s K')

# Definimos numerador y denominador como polinomios en s
# Ejemplo: G(s) = (2s + 3) / (s^2 + 4s + 5)

numerador = 2*s + 3
denominador = s**2 + 4*s + 5

# Función de transferencia G(s)
G = numerador / denominador

# Mostrar G(s)
print("Función de transferencia G(s):")
sp.pprint(G, use_unicode=True)

# Expandimos y factorizamos si hace falta
print("\nNumerador factorizado:")
sp.pprint(sp.factor(numerador))

print("\nDenominador factorizado:")
sp.pprint(sp.factor(denominador))

# Encontrar los ceros (raíces del numerador)
ceros = sp.solve(numerador, s)
print("\nCeros del sistema (raíces del numerador):")
print(ceros)

# Encontrar los polos (raíces del denominador)
polos = sp.solve(denominador, s)
print("\nPolos del sistema (raíces del denominador):")
print(polos)



m = len(ceros)

n = len(polos)

print(f"Cantidad de polos {n}, cantidad de ceros {m}")


# Ahora deberiamos tomar los valores de asintotas


angulos_asintota = []
for k in range(5): # para 5 valores de k 0,1,2,3,4
    theta_rad = ((2*k + 1)*np.pi)/(n-m)
    theta = theta_rad * ((180)/(np.pi))
    angulos_asintota.append(theta)

print(f"Angulos de asintota: {angulos_asintota}")

# Pensar una logica para eliminar las vueltas extras 
# Por ejemplo 540 - 360, con restar una vez ya estaría bien.



# sigma de corte

sigma_corte = (sum(polos)-sum(ceros))/(n-m)

print(f"punto de corte: {sigma_corte}")



lazo_cerrado = denominador + K*numerador 

sp.pprint(lazo_cerrado)
# Derivar el denominador (polinomio característico)
metodo_routh = sp.diff(denominador + numerador, s)

print("\n Derivada lazo cerrado:")
sp.pprint(metodo_routh)

# Encontrar raíces de la derivada (valores críticos)
valores_criticos = sp.solve(metodo_routh, s)

print("\nPuntos críticos del polinomio característico (donde la derivada = 0):")
print(valores_criticos)