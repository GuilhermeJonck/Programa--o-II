from Palavras import escolha
from embaralhar import emb
from motiva import motivacional
import os

os.system('clear')

def main():
    while True:

        dificuldade=str(input("""
    ----JOGO DO EMBRALHA----
    
    Escolha Dificuldade:

    Fácil= F
    Médio= M
    Difícil= D

    =>"""))
        if dificuldade.lower() not in ('f','m','d') :
            print(f'\nDigite uma opção valida \n ') 
        else:
            break
    while True:

        tema=str(input(f"""
    Escolha um tema :

    cidades= 1
    objetos= 2
    paises= 3
    verbos= 4

    =>"""))
        if tema not in ('1','2','3','4') :
            print(f'\nDigite uma opção valida \n ')
        else:
            break 
            
    cores={'azul':'\033[7;34m','limpa':'\033[m','verde':'\033[7;32m','vermelho':'\033[7;31m'}
    palavra=escolha(tema,dificuldade)
    embaralhada=emb(palavra)
    chances=5

    while True:
        frase=motivacional()
        print("A palavra sorteada foi: {}{}{}\n".format(cores['azul'],embaralhada.upper(),cores['limpa']))

        print(f"Você tem {chances} chances para acertar\n")
    
        resposta= input("Qual é a {}palavra?{} \n=> ".format(cores['azul'],cores['limpa']))
        chances-=1
        if resposta.lower() == palavra:
            print("Parabéns sua resposta está {}CERTA{}\nA palavra era {}{}{}".format(cores['verde'],cores['limpa'],cores['verde'],palavra.upper(),cores['limpa']))
            break
        elif chances==0:
            print("Suas chances acabaram\nA palavra era: {}".format(palavra))
            break
        else:
            print("Resposta {}Incorreta{}\n{}\nNúmero de chances:{}".format(cores['vermelho'],cores['limpa'],frase,chances))
        

if __name__=="__main__":
    main()

