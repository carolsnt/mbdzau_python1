#Escreva um programa que pergunte o salário
#do funcionário e calcule o valor do aumento.
#Para salários superiores a R$ 2.250,00, calcule
#um aumento de 10%. Para os inferiores ou
#iguais, de 15%.

salario = float(input("Digite o salário do funcionário: "))
if salario > 2250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

print(f"O valor do aumento é R$ {aumento:.2f}")
