notas = []
for i in range(1, 6):
    nota = float(input(f"Ingrese la notas {i}: "))
    notas.append(nota)
    
promedio = sum(notas) / 5

if promedio >= 60:
    print("Aprobado :D")
elif 40 <= promedio < 60:
    print("En recuperación :/")
else:
    print("Reprobado :c")
