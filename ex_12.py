from math import sqrt
def funcao_bhaskara(a, b, c):
	x1 = 0
	x2 = 0
	delta = b ** 2 - 4 * a * c
	if delta >= 0:
		print("Raízes reais")
		x1 = (-b + sqrt(delta)) / (2 * a)
		x2 = (-b - sqrt(delta)) / (2 * a)
	else:
		print("Raízes complexas")
	return x1, x2
bha1, bha2 = funcao_bhaskara(1, 2, -3)
print("x 1 = %f" %bha1)
print("x 2 = %f" %bha2)
