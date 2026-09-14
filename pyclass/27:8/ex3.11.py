#Faça um programa que solicite o preço de uma
#mercadoria e o percentual de desconto. Exiba
#o valor do desconto e o preço a pagar.

preco_mercadoria = float(input("Digite o preço da mercadoria: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
valor_desconto = preco_mercadoria * (percentual_desconto / 100)
preco_a_pagar = preco_mercadoria - valor_desconto
print(f"O valor do desconto é: R$ {valor_desconto:.2f}")
print(f"O preço a pagar é: R$ {preco_a_pagar:.2f}")