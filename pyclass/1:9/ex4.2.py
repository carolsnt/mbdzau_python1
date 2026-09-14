#Escreva um programa que pergunte a velocidade
#do carro de um usuário. Caso ultrapasse 80 km/h,
#exiba uma mensagem dizendo que o usuário foi
#multado. Nesse caso, exiba o valor da multa,
#cobrando R$ 5 por km/h acima de 80 km/h.

velocidade = float(input("Digite a velocidade do carro: "))
if velocidade < 0:
    print("Velocidade inválida. Por favor, insira um valor positivo.")
elif velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você está acima do limite de velocidade em {velocidade - 80} km/h e foi multado em R$ {multa:.2f}")
else:
    print("Você está dentro do limite de velocidade.")