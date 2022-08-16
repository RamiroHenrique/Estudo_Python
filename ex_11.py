from math import sqrt
def calcular_hipotenusa(cateto_adjacente, cateto_oposto):
	return sqrt(cateto_adjacente ** 2 + cateto_oposto ** 2)
a = float(input("cateto adjacente = "))
b = float(input("cateto oposto = "))
print("Hipotenusa = %.2f" %calcular_hipotenusa(a, b))
