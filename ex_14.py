def verificar_quadrante(x, y):
	if x >= 0 and y >= 0:
		return 1
	elif x < 0 and y >= 0:
		return 2
	elif x < 0 and y < 0:
		return 3
	else:
		return 4
n = verificar_quadrante(1, -1)
print("quadrante: %d" %n)
