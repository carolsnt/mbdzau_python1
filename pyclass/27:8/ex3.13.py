#Escreva um programa que converta uma
#temperatura digitada em °C em °F. A fórmula
#para essa conversão é:
#F = (9 * C /5) + 32

celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = (9 * celsius / 5) + 32
print(f"A temperatura em °F é: {fahrenheit:.2f}")