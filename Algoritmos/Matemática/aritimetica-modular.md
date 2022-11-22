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
* $a*k\equiv b*k (\mathrm{mod}\ n)$ 
* $a*k\equiv b*k (\mathrm{mod}\ k*n)$ 
* $a_1+a_2\equiv b_1+b_2 (\mathrm{mod}\ n)$ Compatibilidade com soma
* $a_1-a_2\equiv b_1+b_2 (\mathrm{mod}\ n)$ Compatibilidade com subtração
* $a_1*a_2\equiv b_1*b_2 (\mathrm{mod}\ n)$ Compatibilidade com multiplicação 
* $a^k\equiv b^k (\mathrm{mod}\ n)$ Para $k$ não negativo. Compatibilidade com exponenciação
* $p(a)\equiv p(b) (\mathrm{mod}\ n)$ Para qualquer função polinomial $p(x)$ com coeficientes inteiros.

Se $a\equiv b (\mathrm{mod}\ n)$, é geralmente falsto que $k^a \equiv k^b (\mathrm{mod}\ n)$, porém a seguinte regra é verdade:

* Se $c\equiv d (\mathrm{mod}\ φ(n))$, onde $φ$ é a [função tociente de Euler](https://en.wikipedia.org/wiki/Euler%27s_totient_function), então $a^c \equiv a^d (\mathrm{mod}\ n)$ desde que $a$ seja [coprimo](https://en.wikipedia.org/wiki/Coprime_integers) de $n$.



