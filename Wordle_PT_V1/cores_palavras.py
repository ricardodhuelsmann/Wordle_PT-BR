from termcolor import colored

letra_certa = lambda x: colored(x, 'green', attrs=['bold'])
letra_errada = lambda x: colored(x, 'red', attrs=['bold'])
letra_semicerta = lambda x: colored(x, 'yellow', attrs=['bold'])

def converter_string_lista(string: str)->list:
    '''Converte uma string em uma lista de caracteres'''
    string = string.upper()
    lista=[]
    lista[:0]=string
    return lista

def avalia_palavra(palavra_certa: list, palavra_entrada: list) -> None:
    '''Avalia a palavra inserida pelo usuário'''
    for posicao in range(5):
        if palavra_entrada[posicao] in palavra_certa:
            if palavra_entrada[posicao] == palavra_certa[posicao]:
                print(letra_certa(palavra_entrada[posicao]), end=' ')
            else:
                print(letra_semicerta(palavra_entrada[posicao]), end=' ')
        else:
            print(letra_errada(palavra_entrada[posicao]), end=' ')
    print()