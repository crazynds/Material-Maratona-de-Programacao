# Fibonacci 
Na matemática, a sucessão de Fibonacci (ou sequência de Fibonacci), é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores. 

Definição: $fib(n) = fib(n-1) + fib(n-2)$, para $n \gt 1$. 
Note que $fib(0) = 0$ e $fib(1) = 1$


$0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, ...$


## Teoria
**Teorema de Zeckendorf:** Qualquer número inteiro positivo pode ser escrito como a soma de um ou mais números de Fibonacci distintos e não consecutivos. O fato dos números não serem consecutivos pode ser facilmente observado a partir da definição de Fibonacci: se o número for expresso pela soma de dois consecutivos, então pode ser expresso pelo próximo número da sequência.

**Pré-computar a sequência:** O maior valor que um unsigned long long pode guardar da sequência é fib(93). Portanto, muito dificilmente será vantajoso utilizar essa técnica. A não ser que a questão trate, por exemplo, de fib(n) mod m, sendo m constante.

**Fórmula de Binet**: Essa fórmula generaliza os termos da sequência. Uma desvantagem é que ao utilizar pontos flutuantes, é possivel se perder precisão durante o calculo e resultar na resposta errada. Por esse motivo, muito dificilmente será utilizada.

$$
f(n) = {({1+\sqrt{5} \over 2 })^n - ({1-\sqrt{5} \over 2 })^n \over \sqrt{5}}
$$

É possivel também chegar ao valor aproximado usando apenas uma parte da equação:

$$
f(n) = {({1+\sqrt{5} \over 2 })^n \over \sqrt{5}}
$$

## Período de Pisano

A sequência de Fibonacci mod M é sempre periódica. Ou seja, para um M no qual o periodo seja 6, como o Pisano de 4, fibonacci de 0 e o de 6 será o mesmo, e o de 1 e o 7 também, e assim por diante, de forma que a equação abaixo é verdadeira:

Função de Pisano = $\pi (k)$  

**OBS:** Essa propriedade é muito útil para calcular $fib(n) \bmod M$ quando n for um número muito grande, pois:

$$
fib(n) \bmod M = fib(n \bmod \pi (M)) \bmod M
$$

*Exemplo:*

Fibonacci: $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 …$

Fibonacci (mod 4): $1, 1, 2, 3, 1, 0, 1, 1, 2, 3, 1, 0 …$

O período de Pisano de 4 é 6, pois, após 6 números, a sequência começa a se repetir.

**Obs:**
Note que o Período de Pisano não serve para otimizar o cálculo, pois não existe fórmula para calculá-lo (deve ser feito de maneira iterativa), tendo complexidade $O(n^2)$.

**Algoritmo:**

```c++
long long pisano(long long m)
{
    long long a = 0, b = 1, c = a + b;
    for (int i = 0; i < m * m; i++)
    {
        c = (a + b) % m;
        a = b;
        b = c;
        if (a == 0 && b == 1)
            return i + 1;
    }
    return m*m;
}
```

## Algoritmos para calcular fib(n)

## Recursivo - $O(2^n)$.

Esse algoritmo é, provavelmente, o mais famoso para encontrar um valor da sequência de Fibonacci. Porém, sua complexidade é muito alta e, dificilmente, será utilizado. 

```c++
int fib(int n)
{
    if(n == 0)
        return 0;

    if(n == 1 || n == 2)
        return 1;

    return fib(n-1) + fib(n-2);
}
```

## Com Laço de Repetição - $O(n)$.

Essa solução é bem mais rápida que a primeira e é o melhor algoritmo para montar um vetor da sequência de Fibonacci. Porém, ainda é lento para se trabalhar com números muito grandes.

```c++
int fib(int n)
{
    int a = 0, b = 1, c;

    if( n == 0)
        return 0;

    for(int i = 2; i <= n; i++)
    {
       c = a + b;
       a = b;
       b = c;
    }
    return b;
}
```

## Exponenciação de Matriz - $O(log(n))$.

Essa solução é muito pouco conhecida e se baseia na seguinte propriedade:
elevar a matriz { {1,1} , {1, 0} } no expoente n resulta na matriz { {fib(n+1) ,fib(n)} , {fib(n), fib(n-1)} }.

```C++
void mult(ll m[2][2], ll m2[2][2], ll mod)
{
    ll a = (m[0][0] * m2[0][0]) % mod + (m[0][1] * m2[1][0]) % mod;
    ll b = (m[0][0] * m2[0][1]) % mod + (m[0][1] * m2[1][1]) % mod;
    ll c = (m[1][0] * m2[0][0]) % mod + (m[1][1] * m2[1][0]) % mod;
    ll d = (m[1][0] * m2[0][1]) % mod + (m[1][1] * m2[1][1]) % mod;

    m[0][0] = a % mod;
    m[0][1] = b % mod;
    m[1][0] = c % mod;
    m[1][1] = d % mod;
}

int getBit_64(ll n, int shiftLeft)
{
    ll mask = (ll)1 << shiftLeft;

    if((n & mask) != 0)
        return 1;

    return 0;
}

int msb_64(ll n)
{
    for(int i = 63; i >= 0; i--)
    {
        if(getBit_64(n, i) == 1)
            return i;
    }

    return -1;
}
ll fibRapido(ll n, ll mod)
{
    if(n == 0)
        return 0;

    int msbN = msb_64(n);

    ll resp[2][2] = {{1,0},{0,1}}; // matriz identidade
    ll fator[2][2] = {{1,1},{1,0}};

    for(int i = 0; i <= msbN; i++)
    {
        if(getBit_64(n, i) == 1)
        {
            mult(resp, fator, mod);
        }

        mult(fator, fator, mod);
    }

    return resp[0][1];
}
```

O algoritmo apresentado retorna a resposta mod m, pois ele serve para trabalhar com números muito grandes, os quais resultam em overflow se não houver operação de módulo envolvida. Ex: fib(1.000.000.000) mod 100. É importante notar que apesar de ele ser muito mais rápido que o algoritmo anterior, ele deve ser utilizado somente quando for imprescindível, posto que demanda muito mais código.


## Algoritmo de Fibonacci Fast Doubling

É a versão simplificada do algoritmo de multiplicação de matriz, evitando contas desnecessárias. 

O método Fast Doubling  é baseado nas seguintes duas formulas:

$$
F(2n) = F(n)[2F(n+1) – F(n)]
$$

$$
F(2n + 1) = F(n)2 + F(n+1)2
$$

Mais informações podem ser vistas [aqui](https://www.geeksforgeeks.org/fast-doubling-method-to-find-the-nth-fibonacci-number/#practiceLinkDiv)

```C++
long long fibonatiMod (long long n,long long mod)
{
    long long msb_position = 63;
    while (!((1 << (msb_position-1) & n)) && msb_position >= 0)
        msb_position--;
 
    long long a=0, b=1; 
 
    for (long long i=msb_position; i>=0;--i)
    {       
        long long d = (a%mod) * ((b%mod)*2 - (a%mod) + mod),
            e = (a%mod) * (a%mod) + (b%mod)*(b%mod);
        a=d%mod;
        b=e%mod;
 
        if (((n >> i) & 1) != 0)
        {
            long long c = (a + b) % mod;
            a = b;
            b = c;
        }
    }
    return a;
}
```



### Exercícios sobre esse tema:

 - [1151 - Fibonacci Fácil](https://www.beecrowd.com.br/judge/pt/problems/view/1151) [Fácil]
 - [1176 - Fibonacci em Vetor](https://www.beecrowd.com.br/judge/pt/problems/view/1176) [Fácil]
 - [1531 - Fibonacci Denovo](https://www.beecrowd.com.br/judge/pt/problems/view/1531) [Dificil]
