
from random import shuffle

def emb(palavra):
    embaralha=list(palavra)
    shuffle(embaralha)
    p="".join(embaralha)
    return p