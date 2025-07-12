import requests

def pegar_palavra()->str:
    """pegar_palavra serve para retornar uma palavra aleatória por meio de uma API.""" 
    url = "https://api.dicionario-aberto.net/random"
    resposta = requests.get(url)
    entrada = resposta.json()
    palavra = entrada["word"]
    return palavra

def montar_forca(palavra:str)->list:
    """montar_forca serve para retornar os espaços de uma palavra em uma lista. 

    palavra: 
        um valor string.""" 
    forca = ["_" for _ in palavra]
    return forca

def entrada()->str:
    """montar_forca serve para retornar os espaços de uma palavra em uma lista. 

    palavra: 
        um valor string."""
    entrada = input("Digite uma letra: ")
    while entrada == "" or not entrada.isalpha():
        entrada = input("Erro, digite uma letra: ")
    return entrada

def preencher_forca(palavra:str,tentativa:str,forca:list)->int:
    """preencher_forca serve para adicionar tentativas a lista da forca e retornar a posição da. 

    palavra: 
        um valor string.
    tentativa:
        um valor string.
    forca:
        uma lista."""
    posicao = 0
    quant = 0
    for i in palavra:
        posicao += 1
        if i == tentativa:
            quant += 1
            forca[posicao-1] = tentativa
    return quant

def imprimir_forca(tentativa:str,quant:int):
    """imprimir_forca serve para exibir o resultado. 

    tentativa: 
        um valor string.
    quant:
        um valor int."""
    if tentativa in palavra:
            print("A letra ({}) aparece {}x na palavra.".format(tentativa,quant))
            print("A palavra até o momento é: ")
            print("[", end=" ")
            for i in forca:
                print(i, end=" ")
            print("]", )
            print("")
    else: 
        print("A letra ({}) não está palavra.".format(tentativa))
    

palavra = pegar_palavra()
forca = montar_forca(palavra)

print("A palavra tem",len(palavra),"letras.")

while True:
    tentativa = entrada()
    if len(tentativa) <= len(palavra):
        if tentativa == palavra:
            print("Parabéns, a palavra é {}!".format(tentativa))
            break
        quant = preencher_forca(palavra,tentativa,forca)
        imprimir_forca(tentativa,quant)
    else:
        print("A palavra é menor.")