def add(x, y):
	return(x+y)
def sub(x, y):
	return(x-y)
def mult(x, y):
	return(x*y)
def div(x, y):
	if y == 0:
		return('ERRO: divisão por zero')
	return(x/y)
def calculadora(x, y, operador):
	if operador == '+':
		valor = add(x, y)
	elif operador == '-':
		valor = sub(x, y)
	elif operador == '*':
		valor = mult(x, y)
	elif operador == '/':
		valor = div(x, y)
	else:
		return('ERRO:operação inválida')
	return(valor)
resultado = calculadora(2, 2, '/')
print(resultado)
