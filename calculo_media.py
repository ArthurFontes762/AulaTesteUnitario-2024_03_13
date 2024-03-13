def calcular_media(lista):
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")
    soma = sum(lista)
    media = soma / len(lista)
    return media