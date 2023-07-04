def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

# Solicitar as notas ao estudante
quantidade_notas = int(input("Digite a quantidade de notas: "))
notas = []
for i in range(quantidade_notas):
    nota = float(input("Digite a nota {}: ".format(i+1)))
    notas.append(nota)

# Calcular a média
media_aluno = calcular_media(notas)

# Verificar a aprovação
situacao = verificar_aprovacao(media_aluno)

# Imprimir o resultado
print("A média do aluno é:", media_aluno)
print("Situação do aluno:", situacao)
