ListaPaises = []
print("Cuantos paises desea ingresar?")
cant = int(input())
i = 0
while i < cant:
    print("Ingrese el pais ", i + 1)
    nom = input()
    ListaPaises.append(nom)
    i+=1
ordenada = set(sorted(ListaPaises))
print(ordenada)
