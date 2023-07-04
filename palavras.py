letras_disponiveis = ['a', 'b', 'c', 'd', 'e']

def formar_palavras(letras, comprimento):
    palavras = []
    for i in range(comprimento):
        if i == 0:
            palavras = letras[:]
        else:
            novas_palavras = []
            for palavra in palavras:
                for letra in letras:
                    nova_palavra = palavra + letra
                    novas_palavras.append(nova_palavra)
            palavras = novas_palavras[:]
    return palavras

comprimento_desejado = 3
palavras_formadas = formar_palavras(letras_disponiveis, comprimento_desejado)

print(palavras_formadas)
