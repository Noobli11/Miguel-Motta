# Programa para calcular el promedio de 5 calificaciones y determinar la situación académica
# Solicitar las 5 calificaciones al estudiante (el usuario)
calificaciones = []
for i in range(1, 6):
    nota = float(input(f"Ingrese la calificación {i}: "))
    calificaciones.append(nota)
# Calcular el promedio
promedio = sum(calificaciones) / 5
# Determinar la situación académica
if promedio >= 60:
    print("Aprobado")
elif 40 <= promedio < 60:
    print("En recuperación")
else:
    print("Reprobado")