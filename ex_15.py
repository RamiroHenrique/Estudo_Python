def final_placa(placa):
	if len(placa) == 7:
		return int(placa[len(placa) - 2] + placa[len(placa) - 1])
	else:
		print("Erro: formato inválido")
		return -1
final = final_placa("asd9921")
if final != -1:
	print("final da placa: %d" %final)
