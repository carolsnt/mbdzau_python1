#Faça um programa que leia a categoria de um
#produto e determine o preço pela tabela:
#    categoria 1: R$ 10,00
#   categoria 2: R$ 18,00
#   categoria 3: R$ 23,00
#   categoria 4: R$ 26,00
#   categoria 5: R$ 31,00

categoria = int(input("Digite a categoria do produto (1 a 5): "))
if categoria == 1:
    preco = 10.00
elif categoria == 2:
    preco = 18.00
elif categoria == 3:
    preco = 23.00
elif categoria == 4:
    preco = 26.00
elif categoria == 5:
    preco = 31.00
else: 
    print("Categoria inválida. Por favor, insira um valor entre 1 e 5.")
    preco = 0.00

print("O preço do produto é: R$%6.2f" % preco)