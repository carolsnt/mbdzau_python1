#Escreva um programa que calcule o preço a
#pagar pelo fornecimento de energia elétrica.
#Pergunte a quantidade de kWh consumida e o
#tipo de instalação: R para residências, I para
#indústrias e C para comércios. Calcule o preço
#a pagar de acordo com a tabela a seguir.

kwh = float(input("Digite a quantidade de kWh consumida: "))
tipo = input("Digite o tipo de instalação (R, I ou C): ").upper()

if tipo == "R":
	if kwh <= 500:
		preco_por_kwh = 0.40
	else:
		preco_por_kwh = 0.65
elif tipo == "C":
	if kwh <= 1000:
		preco_por_kwh = 0.55
	else:
		preco_por_kwh = 0.60
elif tipo == "I":
	if kwh <= 5000:
		preco_por_kwh = 0.55
	else:
		preco_por_kwh = 0.60
else:
	print("Tipo de instalação inválido.")
	preco_por_kwh = 0

preco = kwh * preco_por_kwh
print(f"Preço a pagar: R$ {preco:.2f}")


