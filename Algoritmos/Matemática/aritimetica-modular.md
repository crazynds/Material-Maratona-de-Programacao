# Aritimética modular

$$
    \documentclass{scrartcl}
    \newcommand{\Mod}[1]{\ (\mathrm{mod}\ #1)}
$$

Na matemática, a aritmética modular é um sistema de aritmética para números inteiros, onde os números "envolvem" ao atingir um determinado valor, chamado de módulo.

A definição de módulo é dada por:

Dado um inteiro $ n \gt 1 $, chamado módulo, e dois inteiros $a$ e $b$ são ditos congruentes módulo $n$, se e somente se $n$ é um divisor da diferença entre eles.
$$
    a - b = k*n
$$
Para $k \in \mathbb{Z}$

Logo é dito que:

$$
    a \equiv b \Mod{n}
$$

Note que pela notação o trecho $\Mod{n}$ deve aparecer sempre ao lado direito da equação e é aplicado a ambos os lados da equação, e não só ao lado em que ele aparece. Ou seja, ambos os exemplos abaixo são verdade:

$$
    4 \equiv 9 \Mod{5}\\
    9 \equiv 4 \Mod{5}
$$ 

## Numeros negativos

A definição de congruencia também é aplicada a valores negativos. Por exemplo:

$$
    2 \equiv -3 \Mod{5}\\
    -8 \equiv 7 \Mod{5}\\
    -3 \equiv -8 \Mod{5}
$$

Perceba que pela definição, o módulo de um número não pode ser negativo. E que o módulo de um número negativo pode ser diferente para o mesmo número absoluto.


## Propriedades

Primeiramente, a relação de módulo satisfazem todas as condições de relação de equivalência:
* Reflexividade: $a\equiv a\Mod{n}$
* Simetria: $a\equiv b\Mod{n}$ se $b\equiv a\Mod{n}$ para todo $a$,$b$ e $n$
* Transitividade: Se $a\equiv b\Mod{n}$ e $b\equiv c\Mod{n}$ então $a\equiv c\Mod{n}$


Seja $a_1 \equiv b_1 \Mod{n}$, $a_2 \equiv b_2 \Mod{n}$ e $a \equiv b \Mod{n}$ e $k \in \mathbb{Z}$ então:

* $a+k\equiv b+k \Mod{n}$ 
* $a*k\equiv b*k \Mod{n}$
* $a*k\equiv b*k \Mod{k*n}$
* $a_1+a_2\equiv b_1+b_2 \Mod{n}$ Compatibilidade com soma
* $a_1-a_2\equiv b_1+b_2 \Mod{n}$ Compatibilidade com subtração
* $a_1*a_2\equiv b_1*b_2 \Mod{n}$ Compatibilidade com multiplicação 
* $a^k\equiv b^k \Mod{n}$ Para $k$ não negativo. Compatibilidade com exponenciação
* $p(a)\equiv p(b) \Mod{n}$ Para qualquer função polinomial $p(x)$ com coeficientes inteiros.

Se $a\equiv b \Mod{n}$, é geralmente falsto que $k^a \equiv k^b \Mod{n}$, porém a seguinte regra é verdade:

* Se $c\equiv d \Mod{φ(n)}$, onde $φ$ é a [função tociente de Euler](https://en.wikipedia.org/wiki/Euler%27s_totient_function), então $a^c \equiv a^d \Mod{n}$ desde que $a$ seja [coprimo](https://en.wikipedia.org/wiki/Coprime_integers) de $n$.



