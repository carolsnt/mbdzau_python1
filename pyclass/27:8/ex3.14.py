#Escreva um programa que pergunte a
#quantidade de km percorridos por um carro
#alugado pelo usuário, assim como a
#quantidade de dias pelos quais o carro foi
#alugado. Calcule o preço a pagar, sabendo que
#o carro custa R$ 60 por dia e R$ 0,15 por km
#rodado

km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))
preco_a_pagar = (dias_alugados * 60) + (km_percorridos * 0.15)
print(f"O preço a pagar é: R$ {preco_a_pagar:.2f}")