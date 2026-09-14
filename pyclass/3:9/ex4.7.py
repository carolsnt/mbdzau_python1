#Rastreie o programa anterior e monte uma
#tabela com as linhas que seriam executadas
#com os inputs de 1 até 6.

categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
	preco = 10.00
else:
	if categoria == 2:
		preco = 18.00
	else:
		if categoria == 3:
			preco = 23.00
		else:
			if categoria == 4:
				preco = 26.00
			else:
				if categoria == 5:
					preco = 31.00
				else:
					print("Categoria inválida.")
					preco = 0.00

print("O preço do produto é: R$ %6.2f" % preco)

# Tabela de rastreamento:
# categoria 1: 1, 2, 3, 19
# categoria 2: 1, 2, 4, 5, 6, 19
# categoria 3: 1, 2, 4, 5, 7, 8, 9, 19
# categoria 4: 1, 2, 4, 5, 7, 8, 10, 11, 12, 19
# categoria 5: 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 15, 19
# outras:      1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 18, 19