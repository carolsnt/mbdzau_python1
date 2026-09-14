#Escreva um programa para aprovar o empréstimo
#bancário para compra de uma casa. O programa
#deve perguntar o valor da casa a comprar, o
#salário e a quantidade de anos a pagar. O valor da
#prestação mensal não pode ser superior a 30% do
#salário. Calcule o valor da prestação como sendo
#o valor da casa a comprar dividido pelo número de
#meses a pagar.

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário: "))
anos = int(input("Digite a quantidade de anos a pagar: "))
prestacao_mensal = valor_casa / (anos * 12)
if prestacao_mensal > salario * 0.3:
    print("Empréstimo não aprovado. A prestação mensal excede 30% do salário.")
else:
    print("Empréstimo aprovado. A prestação mensal é de R$ %.2f" % prestacao_mensal)
    