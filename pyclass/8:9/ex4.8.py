#Escreva um programa que leia dois números e
#que pergunte qual operação você deseja
#realizar. Você deve poder calcular a soma (+),
#subtração (-), multiplicação (*) e divisão (/).
#Exiba o resultado da operação solicitada.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    print("Operação inválida!")

print("O resultado da operação é: %6.2f" % resultado)
