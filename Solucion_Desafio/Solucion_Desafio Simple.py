nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))
nota4 = float(input("Ingresa la cuarta nota: "))
nota5 = float(input("Ingresa la quinta nota: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("el promedio es:", promedio)

if promedio >= 60:
    print("PASASTE EL CURSO :D")
elif 40<= promedio <=59:
    print("En Recuperacion :/")
else:
    print("No pasate el curso :c")