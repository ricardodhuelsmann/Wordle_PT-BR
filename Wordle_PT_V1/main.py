import funcoes_wordle as fw
import cores_palavras as cp

def executar_jogo() -> None:
    '''Função principal, executa o jogo'''
    print('\nBem vindo ao jogo Wordle em português!\n')
    palavra_sorteada = fw.sortear_palavra()
    palavra_entrada = None
    while palavra_sorteada != palavra_entrada:
        palavra_entrada = fw.perguntar_palavra()
        if fw.validar_entrada(palavra_entrada): 
            lista_entrada = cp.converter_string_lista(palavra_entrada)
            lista_palavra_certa = cp.converter_string_lista(palavra_sorteada)
            cp.avalia_palavra(palavra_certa= lista_palavra_certa, palavra_entrada= lista_entrada)
        else:
            print('\nPalavra inválida! Favor inserir palavra válida com cinco letras!\n')
    print('Parabéns! Você acertou!\n')

if __name__ == "__main__":
    executar_jogo()