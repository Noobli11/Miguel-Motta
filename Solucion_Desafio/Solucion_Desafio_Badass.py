# Versión avanzada con listas y for
notas = []

for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)

print("numero de notas ingresadas son:", len(notas))
print("El promedio es:", promedio)

if promedio >= 60:
    print("¡Pasaste el curso :D!")
elif 40 <= promedio <=59:
    print("En recuperación :/")
else:
    print("No pasaste el curso :c")