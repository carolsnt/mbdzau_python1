# Escreva uma expressão para determinar se
# uma pessoa deve ou não pagar imposto.
# Considere que pagam imposto pessoas cujo
# salário é maior que R$ 2.200,00.

salario = float(input("Digite o salário da pessoa: "))
imposto = salario > 2200

if imposto:
	print("A pessoa deve pagar imposto.")
else:
	print("A pessoa não deve pagar imposto.")