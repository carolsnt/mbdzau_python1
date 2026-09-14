# Faça um programa que calcule o aumento de
#um salário. Ele deve solicitar o valor do salário
#e a porcentagem do aumento. Exiba o valor do
#aumento e do novo salário.

salario = float(input("Digite o salário atual: "))
porcentagem_aumento = float(input("Digite a porcentagem de aumento: "))
aumento = salario * (porcentagem_aumento / 100)
novo_salario = salario + aumento
print(f"O valor do aumento é: R$ {aumento:.2f}")
print(f"O novo salário é: R$ {novo_salario:.2f}")