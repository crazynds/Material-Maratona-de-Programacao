# Manacher

O algoritmo de Manacher é utilizado para encontrar todos os palíndromos de uma palavra em tempo O(n). 

O Manacher funciona somente com strings de tamanho ímpar, portanto, caso o a string tenha tamanho par, é necessário adicionar '.' entre cada caracter, para que dessa forma ela tenha um tamanho ímpar.

O Manacher utilizar propriedades dos palíndromos para descobrí-los todos em O(n). Ele funciona verificando qual o maior palíndromo que tenha centro em i. A propriedade principal que ele utiliza é que palíndromos dentro de palíndromos são espelhados. Ou seja, no caso 'abacaba', há um palíndromo maior com centro em 'c'. O algoritmo ao verificar qual o maior palíndromo em todos os caracteres que estão a direita de 'c', sabe que eles tem pelo menos o tamanho dos palíndromos que estão a esquerda de 'c', e assim evitam cálculos repetidos.

O retorno do algoritmo é uma lista que representa: para a posição i, o maior palíndromo é LPS[i]. A partir disso, todos os palíndromos podem ser recuperados da string.

## Python

```python
def PreProcessWord(word):
    return "." + "".join([c + "." for c in word])

def Manacher(string):
    string = PreProcessWord(string)
    LPS = [0 for _ in range(len(string))]
    C = 0
    R = 0

    for i in range(len(string)):
        iMirror = 2*C - i
        if R > i:
            LPS[i] = min(R-i, LPS[iMirror])
        else:
            LPS[i] = 0
        try:
            while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass
        
        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]
    
    return LPS
    r, c = max(LPS), LPS.index(max(LPS))
    result = string[c - r : c + r].replace(".","")

```