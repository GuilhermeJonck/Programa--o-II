
from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
def main():
    BASE_DIR=Path(__file__).resolve().parent
    with open(f'{BASE_DIR}/PT-rev_bichos.txt') as file:
            portuguese= file.read().lower()
    with open(f'{BASE_DIR}/Libaunt.txt') as file:
            estoniana= file.read().lower()

    letra_texto1=[c for c in portuguese if c.isalpha()]

    letra_texto2=[c for c in estoniana if c.isalpha()]

    qtd_letras=Counter(letra_texto1)
    qtd_letras2=Counter(letra_texto2)
    rotulos, valores = zip(*qtd_letras.most_common(10))
    _, valores2 = zip(*qtd_letras2.most_common(10))
   
    largura=0.3
    pos1=np.arange(len(valores))
    
    pos2=[x+largura for x in pos1]

    plt.title('Frequência de letras em Língua Portuguesa e Língua Estoniana')
    plt.ylabel('frequência das letras')
    plt.xlabel('Letras')
    plt.bar(rotulos, valores,color='red',width=largura,label='Portuguesa')
    plt.bar(pos2,valores2,color='blue',width=largura,label='Estoniana')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()