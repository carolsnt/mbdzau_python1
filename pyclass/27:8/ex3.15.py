#Escreva um programa para calcular a redução
#do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e
#quantos anos ele já fumou. Considere que um
#fumante perde 10 minutos de vida a cada
#cigarro, calcule quantos dias de vida um
#fumante perderá. Exiba o total em dias.

cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Digite quantos anos você já fumou: "))
total_cigarros = cigarros_por_dia * anos_fumando * 365
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / (24 * 60)
print(f"Você perdeu aproximadamente {dias_perdidos:.2f} dias de vida com as pessoas que você mais ama.")
