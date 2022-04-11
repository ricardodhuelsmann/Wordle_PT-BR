import random

def abrir_arquivo_sorteio() -> None:
    '''Abre arquivo que contém palavras disponíveis para sorteio no jogo'''
    global arquivo_sorteio
    global palavras_sorteio
    arquivo_sorteio = open(r'Docs\lista_curta_palavras.txt', 'r', encoding='utf-8')
    palavras_sorteio = arquivo_sorteio.readlines()

def fechar_arquivo_sorteio() -> None:
    '''Fecha arquivo que contém palavras disponíveis para sorteio no jogo'''
    arquivo_sorteio.close()

def sortear_palavra() -> str:
    '''Sorteia palavra para o jogo. Retorna palavra sorteada'''
    global palavra_sorteada
    abrir_arquivo_sorteio()
    palavra_sorteada = random.choice(palavras_sorteio)
    palavra_sorteada = palavra_sorteada.strip()
    fechar_arquivo_sorteio()
    return palavra_sorteada

def abrir_arquivo_geral() -> None:
    '''Abre arquivo geral que contém palavras válidas no jogo'''
    global arquivo_geral
    global palavras
    arquivo_geral = open(r'Docs\lista_completa_palavras.txt', 'r', encoding='utf-8')
    palavras = arquivo_geral.readlines()
    #print(random.sample(palavras, 15))

def fechar_arquivo_geral() -> None:
    '''Fecha arquivo geral que contém palavras válidas no jogo'''
    arquivo_geral.close()

def validar_palavra(palavra: str) -> bool:
    abrir_arquivo_geral()
    if palavra +'\n' in palavras:
        fechar_arquivo_geral()
        return True
    else:
        fechar_arquivo_geral()
        return False

def validar_entrada(palavra: str) -> bool:
    '''Valida entrada de palavra. Retorna True se for válida, False se não for válida'''
    if len(palavra) == 5:
        return validar_palavra(palavra)
    else:
        return False

def perguntar_palavra() -> str:
    '''Pergunta ao usuário qual a palavra esperada'''
    entrada = input("Digite uma palavra: ")
    return entrada