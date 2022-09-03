from random import choice
def escolha(tema,dificuldade):
    cidades = {"f":
             ["lages","flórida","fátima","belém","nates"],
               "m":["blumenal","criciúma","atalanta","barcelona","jaraguá"],
               "d":["joinville","florianópolis","trombudo Central","tessaquinha","tailândia"]}
    
    objetos = {"f":["anel","bolsa","garfo","faca","lápis"],
               "m":["lapiseira","teclado","borracha","óculos","grafite"],
               "d":["oxímetro","telescópio","paquímetro","micrometro"]}
    
    paises = {"f":["chile","nepal","suíça","russia","suécia","quênia"],
              "m":["brazil","equador","guiana","angola","zâmbia"],
              "d":["argentina","tanzânia","portugal"," Uzbequistão"]}

    verbos = {"f":["pular","correr","sentar","falar","comer"],
              "m":["encontrar","conseguir","entender","aprender","passear"],
              "d":["apaziguar","fotografar","equivaler","escorregar","relampejar"],}
    temas = {'1': cidades,'2': objetos, '3': paises, '4': verbos}
    
    lista=temas[tema][dificuldade]
    palavra=choice(lista)
    return palavra




