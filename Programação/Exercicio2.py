dicio = {}
nome1 = str(input("Digite o nome"))
notas1 = float(input("Digite a nota"))
notas2 = float(input("Digite a nota:"))
dicio[nome1] = [notas1, notas2]

nome1 = str(input("Digite o nome"))
notas1 = float(input("Digite a nota"))
notas2 = float(input("Digite a nota:"))
dicio[nome1] = [notas1, notas2]

nome1 = str(input("Digite o nome"))
notas1 = float(input("Digite a nota"))
notas2 = float(input("Digite a nota:"))
dicio[nome1] = [notas1, notas2]

print(dicio)

def calcula_media(dicio, nome):
    if nome in dicio:
        return sum(dicio[nome]) / len(dicio[nome])


print(calcula_media(dicio, 'Renato'))