# Aritimética modular


Na matemática, a aritmética modular é um sistema de aritmética para números inteiros, onde os números "envolvem" ao atingir um determinado valor, chamado de módulo.

A definição de módulo é dada por:

Dado um inteiro $n \gt 1$ , chamado módulo, e dois inteiros $a$ e $b$ são ditos congruentes módulo $n$, se e somente se $n$ é um divisor da diferença entre eles.

$$
    a - b = k*n
$$

Para $k \in \mathbb{Z}$

Logo é dito que:

$$
    a \equiv b (\mathrm{mod}\ n)
$$

Note que pela notação o trecho $(\mathrm{mod}\ n)$ deve aparecer sempre ao lado direito da equação e é aplicado a ambos os lados da equação, e não só ao lado em que ele aparece. Ou seja, ambos os exemplos abaixo são verdade:

$$
    4 \equiv 9 (\mathrm{mod}\ 5)
$$

$$
    9 \equiv 4 (\mathrm{mod}\ 5)
$$ 

## Numeros negativos

A definição de congruencia também é aplicada a valores negativos. Por exemplo:

$$
    2 \equiv -3 (\mathrm{mod}\ 5)
$$

$$
    -8 \equiv 7 (\mathrm{mod}\ 5)
$$

$$
    -3 \equiv -8 (\mathrm{mod}\ 5)
$$

Perceba que pela definição, o módulo de um número não pode ser negativo. E que o módulo de um número negativo pode ser diferente para o mesmo número absoluto.


## Propriedades

Primeiramente, a relação de módulo satisfazem todas as condições de relação de equivalência:
* Reflexividade: $a\equiv a(\mathrm{mod}\ n)$
* Simetria: $a\equiv b(\mathrm{mod}\ n)$ se $b\equiv a(\mathrm{mod}\ n)$ para todo $a$, $b$ e $n$
* Transitividade: Se $a\equiv b(\mathrm{mod}\ n)$ e $b\equiv c(\mathrm{mod}\ n)$ então $a\equiv c(\mathrm{mod}\ n)$


Seja $a_1 \equiv b_1 (\mathrm{mod}\ n)$, $a_2 \equiv b_2 (\mathrm{mod}\ n)$ e $a \equiv b (\mathrm{mod}\ n)$ e $k \in \mathbb{Z}$ então:

* $a+k\equiv b+k (\mathrm{mod}\ n)$ 
* $a.k\equiv b.k (\mathrm{mod}\ n)$ 
* $a.k\equiv b.k (\mathrm{mod}\ n.k)$
* $a_1+a_2\equiv b_1+b_2 (\mathrm{mod}\ n)$ Compatibilidade com soma
* $a_1-a_2\equiv b_1+b_2 (\mathrm{mod}\ n)$ Compatibilidade com subtração
* $a_1.a_2\equiv b_1.b_2 (\mathrm{mod}\ n)$ Compatibilidade com multiplicação 
* $a^k\equiv b^k (\mathrm{mod}\ n)$ Para $k$ não negativo. Compatibilidade com exponenciação
* $p(a)\equiv p(b) (\mathrm{mod}\ n)$ Para qualquer função polinomial $p(x)$ com coeficientes inteiros.

Se $a\equiv b (\mathrm{mod}\ n)$, é geralmente falsto que $k^a \equiv k^b (\mathrm{mod}\ n)$, porém a seguinte regra é verdade:

* Se $c\equiv d (\mathrm{mod}\ φ(n))$, onde $φ$ é a [função tociente de Euler](https://en.wikipedia.org/wiki/Euler%27s_totient_function), então $a^c \equiv a^d (\mathrm{mod}\ n)$ desde que $a$ seja [coprimo](https://en.wikipedia.org/wiki/Coprime_integers) de $n$.

## Inverso Modular

O inverso modular de $a$ com módulo $m$ é um número $x$ tal que, quando multiplicado com $a$, gera um valor cujo resto da divisão com $m$ é 1. Ou seja, $$ax \equiv1 (\mathrm{mod}\ m)$$

**Notação:** $a^{-1}$

**Exemplo:** $a = 5$ e $m = 7$ resulta em $a^{-1} = 3$ , pois $3 * 5 = 15$ e $15 \equiv1 (\mathrm{mod}\ 7)$

**OBS:** O inverso modular existe se, e somente se, $a$ e $m$ forem coprimos (ou primos entre si), isto é: $mdc(a, m) = 1$.

O algoritmo para calcular o inverso modular utiliza o algoritmo extendido de Euclides (`egcd`). Note que a função `modInv` retorna 0 caso não exista o inverso modular. É interessante apontar que questões que envolvem módulo - na maioria das vezes - possuem um número $m$ primo (geralemente, $10^9 + 7$). Isso garante que o inverso modular irá existir caso $a$ não seja múltiplo de $m$. Portanto, dependendo da questão, pode-se remover a verificação da função `modInv`.

(NÃO TESTADO)
```python
# algoritmo extendido de Euclides
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# a^-1 mod m = 1
def modInv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return 0 # inverso modular não existe
    else:
        return x % m
```
Fontes do inverso modular:

[Definições](https://link-url-here.org](https://cp-algorithms.com/algebra/module-inverse.html#practice-problems)https://cp-algorithms.com/algebra/module-inverse.html#practice-problems)

[Algoritmo original](https://link-url-here.org](https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python)https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python)


