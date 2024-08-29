# Números primos


## Checagem rápida de se um número é primo

Se retornar false então é 100% de certeza que não é primo, mas não garante que é primo se retornar True. Aumentar o $k$ aumenta a certeza. 


```python
def checkComposite(n,a,d,s):
    x = pow(a, d, n)
    if x == 1 or x == n-1: return False
    for _ in range(1, s):
        x = (x * x) % n
        if x == n-1: 
            return False
    return True

def isPrime(n, k=5): # miller-rabin
    from random import randint
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
       if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for _ in range(k):
        a = randint(2, n-1)
        if checkComposite(n,a,d,s):
            return False
        
    return True
```

```C++
#define ll unsigned long long

ll powmod(ll base, ll e, ll mod);

ll mulpow(ll base, ll e, ll mod);// Multiplicação com módulo
// Só é importante se a*b pode dar overflow, senão usar (a*b)%mod

bool check_composite(ll n, ll a, ll d, int s) {
    ll x = powmod(a, d, n);
    if (x == 1 || x == n - 1)
        return false;
    for (int r = 1; r < s; r++) {
        x = mulpow(x,x,n);
        if (x == n - 1)
            return false;
    }
    return true;
};
bool isPrime(ll n) { // miller rabin returns true if n is prime, else returns false.
    if (n < 2)
        return false;

    int r = 0;
    ll d = n - 1;
    while ((d & 1) == 0) {
        d >>= 1;
        r++;
    }

    for (int a : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}) {
        if (n == a)
            return true;
        if (check_composite(n, a, d, r))
            return false;
    }
    return true;
}
```

De acordo com [esse site](https://cp-algorithms.com/algebra/primality_tests.html#deterministic-version) é possivel ter uma versão do MillerRabin deterministica se for checado todas as bases até $2*ln(n)^2$.

É provado também que para qualquer número inteiro de 64 bits é necessário checar apenas as 12 primeiros primos.

```python
def checkComposite(n,a,d,s):
    x = pow(a, d, n)
    if x == 1 or x == n-1: return False
    for _ in range(1, s):
        x = (x * x) % n
        if x == n-1: 
            return False
    return True
def isPrime(n): # miller-rabin deterministico para 64 bits
    if n < 2: return False
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]: # 12 primeiros primos
        if n==a:
            return True
        if checkComposite(n,a,d,s):
            return False
        
    return True
```



## Algoritmo Sieve (Pré-computar primos)
Sieve: Algoritmo para verificar se um número é primo.

O algoritmo computa todos os números primos antes (função sieve()) para que depois a  verificação seja através da função prime(int p), onde p é o número que se deseja testar.

```c++
#define SIEVE_SIZE 1000
#include <bitset>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

int N;
int C;
vector<int> primes;
bitset<SIEVE_SIZE+2> bs;

void sieve()
{
    int i, j, max = SIEVE_SIZE + 1;
    bs.reset();
    bs.flip();
    bs.set(0, false);
    bs.set(1, true);
    for( i=2; i <= max; i++ )
    {
        if( bs.test(i) == true ) // i é primo, e todos os múltiplos de i nao
        {
            primes.push_back( i );
            for( j = i*i; j <= max; j += i )
            {
                bs.set(j, false);
            }
        }
    }
}

bool isPrime(int p)
{
    if( p < SIEVE_SIZE )
       return bs.test(p);
    for(int i=0; i< primes.size()-1; i++)
    {
        if( p % primes[i] == 0 )
           return false;
    }
    return true;
}
```

## Sieve em Python (comparação)

```python
import math
from itertools import compress
import timeit

def sieve(n):
    "Primes less than n"
    # sieve(30) --> 2 3 5 7 11 13 17 19 23 29
    data = bytearray((0, 1)) * (n // 2)
    data[:3] = 0, 0, 0
    limit = math.isqrt(n) + 1
    for p in compress(range(limit), data):
        data[p*p : n : p+p] = bytes(len(range(p*p, n, p+p)))
    data[2] = 1
    i = -1
    try:
        while True:
            yield (i := data.index(1, i+1))
    except ValueError:
        pass

def SieveOfEratosthenes(num):
    prime = [True for _ in range(num+1)]
    # boolean array
    p = 2
    while (p * p <= num):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            yield p

print(timeit.timeit(lambda: list(sieve(1_000_000)), number=1))
# 0.013812200020765886
print(timeit.timeit(lambda: list(SieveOfEratosthenes(1_000_000)), number=1))
# 0.0916068000078667v

```

## Prime Factor
Retorna o menor fator primo de um valor n.

Ex: 6 = 2 * 3. No caso o menor valor é o 2 então este será retornado.
Se n for primo, o próprio n será retornado.

```c++
int primeFactor (int n)
{
	// Don't bother to use abs () <stdlib.h>
	if (n < 0)
		n = -n;
	// For n < 2; it is just n
	if (n < 2)
		return n;

	// otherwise, for an even number it is 2
	if (n % 2 == 0)
		return 2;

	// for other odd numbers, search for a divisor
	// until SQRT (n) [conceptual] n / div >= div is
	// equivalent to SQRT (n) >= div
	for (int div = 3; n / div >= div; div += 2)
	{
		// if div is a divisor, just return it.
		if (n % div == 0)
			return div;
	}

	// There is no divisor (n is prime), return it.
	return n;
}
```

# Fatorização

A fatorização de um número é a decomposição de um números pelos seus primos geradores. Por exemplo o número 24 pode ser decomposto em: $2*2*2*3$ ou $2^3*3$. 

Antes de usar o algoritmo de fatorização, checar se o número é primo usando algum teste de primalidade.


## Wheel factorization

A função abaixo faz a fatorização de um número pelos seus primos. Ela pode ser otimizada se já houver uma lista de primos pré computados. Para primos muito grandes essa função pode levar um tempo para fatorizar.


```python
def factorization(number):
    solution = []
    while number&1==0:
        number//=2
        solution.append(2)
    i = 3
    while math.sqrt(number) > i:
        while number % i == 0:
            number //= i 
            solution.append(i)
        i += 2
    if number!=1:
        solution.append(number)
    return solution
```


## Se tiver um sieve pré-computado (até sqrt(n)) é melhor usar essa versão:
```python
import math
import timeit

def factor(n, primes):
    "Prime factors of n."
    # factor(99) --> 3 3 11
    for prime in primes:
        while True:
            quotient, remainder = divmod(n, prime)
            if remainder:
                break
            yield prime
            n = quotient
            if n == 1:
                return
    if n > 1:
        yield n

n = 1_000_000
primes = sieve(math.isqrt(n) + 1) # isqrt é a int(sqrt(n)) ou raiz inteira

```

## Brent's algorithm

Esse algoritmo é bem complexo, leia mais [aqui](https://cp-algorithms.com/algebra/factorization.html#brents-algorithm).


```C++

long long gcd(long long a, long long b); // Maior divisor comum

long long mulpow(long long a, long long b, long long mod); // Multiplicação com módulo
// Só é importante se a*b pode dar overflow, senão usar (a*b)%mod

bool isPrime(long long i); // Fast primality check

long long f(long long x, long long c, long long mod) {
    return (mulpow(x, x, mod) + c) % mod;
}

long long brent(long long n) {
    long long x = x0;
    long long g = 1;
    long long q = 1;
    long long xs, y;
    long long x0=2;
    long long c=1;

    int m = 128;
    int l = 1;
    while (g == 1) {
        y = x;
        for (int i = 1; i < l; i++)
            x = f(x, c, n);
        int k = 0;
        while (k < l && g == 1) {
            xs = x;
            for (int i = 0; i < m && i < l - k; i++) {
                x = f(x, c, n);
                q = mulpow(q, abs(y - x), n);
            }
            g = gcd(q, n);
            k += m;
        }
        l *= 2;
    }
    if (g == n) {
        do {
            xs = f(xs, c, n);
            g = gcd(abs(xs - y), n);
        } while (g == 1);
    }
    return g;
}

vector<long long> fast_factorization(long long num){
    vector<long long> vec;
    while(num>1){
        if(isPrime(num)){
            vec.push_back(num);
            break;
        }
        long long val = brent(num);
        while(num%val==0){
            num/=val;
            vec.push_back(val);
        }
    }
    return vec;
}
```


## Quebrando o RSA

Uma maneira de encontrar os 2 primos multiplos que formam uma chave é usando o algoritmo abaixo. Ainda é lento para quando os números são muito grandes, porém consegue ser viavel para chaves de até 256 bits.

```python
def find2FactorsOfNumber(n):
    a = math.isqrt(n) + 1
    # diff between two consecutives squares
    diff = (a+1)**2 - a**2
    a2 = a**2
    # If N is prime this will loop forever
    while True:
        # this line can be omitted if you use 
        # the diff between two consecutives squares
        #a2 = a**2
        b2 = a2 - n

        # this is the slowest part of the code
        # if you can check if b2 is a perfect square
        # faster this code can be optimized.
        if math.isqrt(b2)**2 == b2:
            b = math.isqrt(b2)
            print(a,b)
            print(a2-b2 == n,(a+b)*(a-b) == n)
            break

        a2 += diff
        # update diff
        diff += 2

        a += 1
    # Return p and q that p*q == n
    return (int(a-b),int(a+b))
```

Se passado um número para a função ela irá retornar 2 números inteiros tal que se multiplicados resulta no número passado. Se não houver 2 números tal que gere um resultado válido, vai ficar em loop infinito.

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

## Multiplicação com módulo

Para linguagens como C/C++ que um inteiro pode overflow, existem casos que queremos multiplicar 2 números e o resultado pode não caber em um inteiro de 64 bits. O algoritmo abaixo faz a multiplicação em O(log n) com módulo evitando o overflow.

```C
#define ll long long int

ll mulpow(ll a, ll b, ll mod) {
    ll res = 0;
    while (b > 0) {
        if (b & 1)
            res = (res + a) % mod;
        a = (a + a) % mod;
        b >>= 1;
    }
    return res;
}
```

## Potencia com Módulo

Para potencia com módulo, em C temos o seguinte código:
```c
#define ll long long int

// Fast pow and mod
ll powmod(ll base, ll exp, ll modulus) {
    base %= modulus;
    ll result = 1;
    while (exp > 0) {
        if (exp & 1) result = mulpow(result, base, modulus);
        base = mulpow(base ,base , modulus);
        exp >>= 1;
    }
    return result;
}
```
Caso a $base^2$ não de overflow, é possivel substituir a função mulpow apenas por $(result.base)\mathrm{mod}\ modulus$ e $(base.base)\mathrm{mod}\ modulus$ nos dois casos em que ela é usada.

Em python temos a função powmod implementada nativamente na função ```pow```. O primeiro parametro é a base, o segundo o expoente e o terceiro é o módulo.

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

# Combinatória modular

Fermat’s little theorem and modular inverse 
Fermat’s little theorem states that if $p$ is a prime number, then for any integer a, the number $a^p – a$ is an integer multiple of p. In the notation of modular arithmetic, this is expressed as: 
$$
a^p = a (\mathrm{mod}\ p) 
$$
For example, if $a = 2$ and $p = 7$ so $2^7 = 128$ and $128 – 2 = 7 × 18$ is an integer multiple of 7.

If a is not divisible by p, Fermat’s little theorem is equivalent to the statement $a^{p–1} – 1$ is an integer multiple of p, i.e 
$$
a^{p-1} = 1 (\mathrm{mod}\ p)
$$
If we multiply both sides by $a^{-1}$, we get. 

$$
a^{p-2} = a^{-1} (\mathrm{mod}\ p)
$$


Código em python: (Precisa testar, não acredito que esteja dando a resposta certa)

```python
def comb_mod(n, p, MOD):
    # initialize numerator and denominator
    num = den = 1
    for i in range(p):
        num = (num * (n - i)) % MOD
        den = (den * (i + 1)) % MOD
    return (num * pow(den, MOD - 2, MOD)) % MOD 
```
Dicas de otimização:

 - Se o $MOD$ é constante, é possivel pre-computar o fatorial no inicio do programa. 
 - Se o $n$ é constante, é possivel pré-computar tudo e acessar como um array.
 

```python
MOD = 10**9 + 7
# Precomputamos o fatorial
factorials = [1] * (10**6 + 1)
for i in range(2, 10**6 + 1):
    factorials[i] = (factorials[i - 1] * i) % MOD

# Poderiamos pre computar o inverso do fatorial
# Mas vamos usar o pow(den, MOD - 2, MOD) para calcular o invFatorial
def combination_mod(n, k, MOD):
    if k > n:
        return 0
    num = factorials[n]
    den = (factorials[k] * factorials[n- k]) % MOD
    return (num * pow(den, MOD - 2, MOD)) % MOD   
```

### Não faz sentido esse código em c++!
Exemplo do programa em c++ (Provavelmente errado!):
 ```c++
// fatorial já ta pre computado FAT[]

const long long MOD = XXXXXX    // Funciona apenas para primos entre si, ou seja, se o MOD for primo vai funcionar

// Computar inv fatorial
invFatorial[0] = 1

for(int x=1;x<LIMIT;x++){
    invFatorial[x] = pow(i,MOD-2);
}

long long comb_mob(long long n, long long p)
{
    // O resto da divisão de (n p) = (n!/(p!(n-p)!)) modulo q poder ser calculado da senguinte forma:
    // FAT[n]*INV[n-p]*INV[p]%MOD
    long long resp = fatorial[n]*invFatorial[n-p];
    resp %= MOD;
    resp *= invFatorial[p];
    resp %= MOD;
    return resp;
}
```

## Algoritmos TESTADOS

Para calcular uma combinatória mod `mod` é preciso pré-computar os fatoriais mod `mod` de $1$ até o maior $n$.

$n$ é o total de elementos e `maxn` é o maior valor possível para $n$.

### Pré-computar fatoriais

```cpp
ll fatMod[maxn + 1];

void precomputeFatMod()
{
    fatMod[0] = 1;
    for (int i = 1; i <= maxn; i++)
    {
        fatMod[i] = fatMod[i - 1] * i % mod;
    }
}
```

### Inverso Modular

```cpp
ll inv(ll a)
{
    return a <= 1 ? a : mod - (long long)(mod / a) * inv(mod % a) % mod;
}
```

### Pré-computar o inverso Modular?

Para pré-computar o inverso modular, pode-se usar programação dinânmica partindo da solução recursiva acima. Porém, acredito que não seja
recomendado, pois, o vetor teria que ter tamanho `mod`, ou seja, teria que guardar todos os valores entre 1 e `mod - 1`. Geralmente,
`mod = 10^9 + 7`, que é muito grande.

### Combinatória Módulo `mod`

```cpp
int combMod(int n, int k)
{
    return fatMod[n] * inv(fatMod[k]) % mod * inv(fatMod[n - k]) % mod;
}
```

# Encontrando a potência de um divisor de fatorial (Fórmula de Legendre)

Algoritmo para encontrar o maior $x$ tal que $k ^ x$ divide $n!$.

**Complexidade:** $O(log n)$

## Caso $k$ seja primo

```cpp
int fact_pow (int n, int k)
{
    int res = 0;
    while (n)
    {
        n /= k;
        res += n;
    }

    return res;
}
```

## Caso $k$ não seja primo ($k$ composto)

No algoritmo abaixo, `factors` é um vetor que guarda os fatores primos que formam $k$. Ele guarda um par, pois o primeiro
é o fator em si, e o segundo, a potência a ele associada.

Para exemplificar: $60 = 2^2 * 3 * 5$

Logo, para representar 60, seria necessário montar um vetor com os seguintes valores:
 - {2, 2}
 - {3, 1}
 - {5, 1}

**OBS:** os primos não precisam estar em ordem.

```cpp
int fact_pow(int n, vector<pair<int, int>> factors)
{
    int resp = 1000000;
    int aux;
    for(auto p : factors)
    {
        aux = fact_pow(n, p.first);
        aux /= p.second;

        if(resp > aux)
        {
            resp = aux;
        }
    }

    return resp;
}
```


## Máximo Divisor Comum / Greatest Common Divisor

Calcula o máximo divisor entre 'a' e 'b'

Ex: gcd(12, 8) = 4
```c++
long long gcd(long long a, long long b) { 
   while (b > 0) { 
      a = a % b; 
      a ^= b;    b ^= a;    a ^= b;  
   }  
   return a; 
} 
```
## Mínimo Múltiplo Comum

Procura o menor valor que seja múltiplo de 'a' e 'b'

Ex: mmc(3, 4) = 12

**OBS: Utiliza a fórmula do gdc**

```c++
#include <cstdlib> /*para poder utilizar o abs(int)*/
int mmc(int a, int b)
{
   return abs(a * b) / gdc(a,b);
}
```
**OBS: mmc(a, b, c) = mmc(mmc(a, b), c)**


## Em Python (melhor)

```python
from math import gcd, lcm

print(gcd(12,8)) # maior divisor comum
# 4

print(lcm(3,4)) # menor multiplo comum
# 12

```

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


# Log 2 O(1)

### C++

```c++
// C++20
#include <bit>
int log2_floor(unsigned long i) {
    return std::bit_width(i) - 1;
}

// pre C++20
int log2_floor(unsigned long long i) {
    return i ? __builtin_clzll(1) - __builtin_clzll(i) : -1;
}
```

# Números de Catalan

Números de Catalan são usados para resolver alguns problemas de combinatória.

O enésimo número de Catalan ($C_{n}$) é resultado dos seguintes problemas:
 - Número total de sequências de parênteses corretas (abrindo $n$ e fechando $n$). Ex: ()(());
 - Número de formas para colocar parênteses em $n+1$ fatores.

**OBS:** Existem MUITAS outras aplicações, mas envolvem assuntos mais complexos.

```cpp
int catalan[maxn];

void precomputeCatalan()
{
    catalan[0] = catalan[1] = 1;
    for (int i = 2; i <= maxn; i++)
    {
        catalan[i] = 0;
        for (int j = 0; j < i; j++)
        {
            catalan[i] += (catalan[j] * catalan[i-j-1]) % mod;
            catalan[i] = catalan[i] % mod;
        }
    }
}
```

Para acessar $C_{n}$, utilizar `catalan[n]`.

# Área de Polígono (Fórmula de Surveyor) 

Dados os pontos no plano cartesiano que formam um polígono, pode-se calcular a sua área.

## Explicação

Para calcular a área, deve-se somar os determinantes dos vetores formados por pontos adjacentes e dividir por 2. Para facilitar
o cálculo, pode-se considerar um polígono de $n$ lados como uma matriz de $n+1$ linhas e 2 colunas ($x$ e $y$). $n+1$ linhas são
necessárias, pois deve-se colocar uma cópia do primeiro ponto no fim da matriz. Deve-se calcular o determinante de todos os pares
de pontos adjacentes, somá-los e dividir por dois. É necessário utilizar o valor absoluto, pois, dependendo da ordem dos pontos (sentido
horário ou anti-horário), o resultado pode ser negativo.

**OBS:**
 - O polígono não precisa estar centralizado na origem (nem conter a origem);
 - O polígono não precisa ser convexo;
 - Os pontos precisam estar "em ordem", ou seja, no vetor, os pontos vizinhos são adjacentes.
 - Para o cálculo, é necessário duplicar o primeiro ponto no fim do vetor (a função abaixo já faz isso).

## O Algoritmo

`points` contém todos os pontos ($x$, $y$) que formam o polígono "em ordem".

```cpp
double orderedPointsArea(vector<pair<double, double>> points)
{
    points.push_back(points.front());

    double p = 0, n = 0;

    for(int i = 0; i < points.size() - 1; i++)
    {
        p += points[i].first * points[i + 1].second;
        n += points[i].second * points[i + 1].first;
    }

    return abs(p - n) / 2;
}
```

## E se os pontos não estiverem ordenados?

**Provavelmente**, deve-se aplicar a ordenação dos pontos que é feita no `Algoritmo de Graham`.



# Graham Scan
*Jaime Antonio Daniel Filho e Juliano de Mello Pasa*

## O que é um envoltório convexo?
O "convex hull", como também é conhecido, é definido como o menor polígono convexo que engloba todos os pontos de um certo conjunto. Convexo significa que nenhuma das diagonais do polígono cruza o lado de fora.

![poligono_convexo_concavo](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/ae0ae734-6ea0-4666-acc4-0134cf519d5a)

Uma das maneiras de visualizar o envoltório convexo é utilizando um elástico de borracha. Para isso, suponha que os pontos são pregos em uma superfície plana. Imagine agora, o que aconteceria se você esticasse um elástico em torno dos pregos e depois o soltasse, permitindo que ele se contraia. O elástico englobaria todos os pregos e encostaria apenas nos mais externos, ou seja, nos que fazem parte do envóltorio convexo.

![analogia_do_elastico](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/2ee1f15e-086e-41e6-9e4d-d5476f6ecebb)

## O algoritmo

O Exame de Graham é um dos algoritmos utilizados para encontrar o envóltorio convexo de um conjunto de pontos. O algoritmo computa o subconjunto de pontos pertencentes ao envóltorio junto à ordem em que aparecem.

O primeiro passo é encontrar um ponto que certamente pertence ao envóltorio convexo. O ponto com menor coordenada y, por exemplo, é um deles. Caso mais de um ponto existir nessa mesma coordenada y, escolhemos o com a maior coordenada x. Tal ponto é chamado de P.

![algoritmo_parte_1](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/bc455bd2-65b7-4c3a-8c32-be0f4e25b991)

Depois, os pontos precisam ser ordenados pelo ângulo que ele forma com o ponto inicial P em relação ao eixo x. Se dois pontos possuírem o mesmo ângulo, ordenamos da maior para menor distância em relação a P.

![algoritmo_parte_2](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/99816ad2-f911-4f0d-b380-4239194ae5d3)

O algoritmo prossegue percorrendo todos os pontos no vetor ordenado e verificando se ele faz parte ou não do envóltorio convexo. Isso é determinado testando se o ponto atual realiza uma curva no sentido horário ou no sentido anti-horário em relação aos dois pontos anteriores. Caso a curva for no sentido horário, o ponto não pertence ao envóltorio e está dentro do polígono.

![algoritmo_parte_3](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/9c9ec097-8273-41c0-b029-367b50066ec1)

Os pontos pertencentes ao envóltorio são armazenados em uma pilha. Desse modo, a medida que percorremos o vetor, adicionamos um ponto e, enquanto for necessário girar no sentido horário partindo dos dois últimos pontos, removemos o topo da pilha.

O verdadeiro ângulo entre os pontos não precisa ser calculado para determinar o sentido da curva. Isso pode ser obtido por meio do cálculo do produto vetorial entre os dois vetores. O resultado é um vetor perpendicular com o sentido dado pela regra da mão direita.

![regra_da_mao_direita](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/5f35460c-80dd-4069-a3b3-6c7d32e91100)

Como os pontos pertencem ao plano xOy, o vetor perpendicular será constituído somente da componente z. Assim, dados três pontos $P_1=(x_1, y_1)$ $P_1=(x_2, y_2)$ e $P_3=(x_3, y_3)$, a componente z de $\vec{P_1P_2}\times\vec{P_1P_3}$ é calculada pela expressão $(x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1)$. Se o resultado for igual a 0, os pontos são colineares. Se for positivo, os três pontos formam uma curva no sentido anti-horário. Se for negativo, estão no sentido horário.

![algoritmo_parte_4](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/dfb81982-cdd6-4b61-9639-451a268d23b7)

Exemplo de excução do algoritmo com posição dos pontos na pilha. O ponto $P$ é o ponto atual do vetor sendo analisado. Os pontos $-1$ e $-2$ correspondem ao ponto no topo da pilha e o ponto logo abaixo (notação de índices em Python). Os pontos em $X$ vermelho são os pontos excluídos do polígono. As linhas verdes são arestas que farão parte do polígono convexo. As linhas azuis são as arestas que estão sendo analisadas, enquanto as linhas vermelhas são linhas que podem ser removidas. As linhas vermelhas serão removidas caso os pontos analisados não forme uma curva no sentido anti-horário.

![executionGif](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/06bf62cc-9cf2-402c-ae7a-a9869c3e43e6)

## Implementação C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Point
{
    int x;
    int y;
};

// Calcula a distância euclidiana entre dois pontos.
int distance_squared(const Point &a, const Point &b)
{
    int dx = a.x - b.x;i
    int dy = a.y - b.y;

    return dx * dx + dy * dy;
}

// Calculate o produto vetorial entre AB e AC:
// AB x AC = 0 -> colinear
// AB x AC > 0 -> anti-horário
// AB x AC < 0 -> horário
int cross_product(const Point &a, const Point &b, const Point &c)
{
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

// ALgoritmo de Graham Scan para encontrar o menor envoltório convexo.
std::vector<Point> graham_scan(std::vector<Point> &points)
{
    // Se existirem 3 pontos, o menor envoltório convexo é formado por eles.
    if (points.size() <= 3)
    {
        return points;
    }

    // Vetor que armazena os pontos que formam o envoltório convexo.
    std::vector<Point> hull;

    // Inicia P0 com o primeiro ponto do vetor.
    Point p0 = points[0];

    // Encontra o ponto mais baixo e mais à direita.
    for (size_t i = 1; i < points.size(); i++)
    {
        if (points[i].y < p0.y || (points[i].y == p0.y && points[i].x > p0.x))
        {
            p0 = points[i];
        }
    }

    // Ordena os pontos de acordo com o ângulo que eles formam com P0.
    // Isto é, de modo que eles sempre estejam no sentido anti-horário
    // em relação a P0.
    std::sort(points.begin(), points.end(), [&](Point &a, Point &b) {
        int product = cross_product(p0, a, b);

        if (product != 0)
        {
            // Se o produto for positivo, o ponto mais à direita é o A, pois
            // giramos no sentido anti-horário partindo de A para chegarmos em B.
            return product > 0;
        }

        int distance_b = distance_squared(p0, b);
        int distance_a = distance_squared(p0, a);

        // Se os pontos forem colineares, o mais distante de P0 vem primeiro.
        return distance_a < distance_b;
    });

    // Percorre e verifica o restante do vetor de pontos.
    for (size_t i = 0; i < points.size(); i++)
    {
        // Enquanto ponto atual e os dois últimos pontos no envoltório
        // formarem um ângulo horário, remova o ponto do topo do envoltório.
        while (hull.size() >= 2 && cross_product(hull[hull.size() - 2], hull[hull.size() - 1], points[i]) <= 0)
        {
            hull.pop_back();
        }

        // Adiciona o ponto ao envoltório convexo.
        hull.push_back(points[i]);
    }

    return hull;
}

int main()
{
    std::vector<Point> points = {
    };

    std::vector<Point> hull = graham_scan(points);

    for (const Point &point : hull)
    {
        std::cout << "(" << point.x << ", " << point.y << ")" << std::endl;
    }

    return 0;
}
```

## Outra forma de calcular orientação

Na implementação em Python, a orientação foi calculada de uma forma diferente. Em vez de utilizar o produto vetorial entre os dois vetores formados pelos 3 pontos, foi calculada a diferença entre suas subidas. As operações são idênticas, mas as componentes multiplicadas são diferentes. Em decorrência disso, para pontos no sentido anti-horário, o valor será negativo, enquanto para pontos no senti horário o valor será positivo.

![desmos-graph (0)](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/ca2fd619-5cf5-426e-8798-dc4c99368588)

## Implementação Python
```python
from functools import cmp_to_key


# Calcula a orientacao de 3 pontos com base na diferença entre suas subidas.
# Essa funcao eh usada no ordenamento e no scan.
# A orientacao eh dada da seguinte forma:
#
#   valor < 0: os pontos estao no sentido anti-horario
#   valor = 0: os pontos sao colineares
#   valor > 0: os pontos estao no sentido horario
def CalculateOrientation(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p3[1] - p2[1]) * (p2[0] - p1[0])


# Calcula o quadrado da distancia entre dois pontos.
# Essa funcao eh usada no ordenamento.
def CalculateSquaredDistance(p1, p2):
    return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2


# Funcao de comparacao que sera utilizada pelo sorted() do python.
# Funcoes de comparacao devem retornar valores inteiros da seguinte forma:
# 
#   valor < 0: p1 vem antes de p2  
#   valor = 0: p1 eh igual p2
#   valor > 0: p1 vem depois de p2
#
# No caso do scan de Graham, pontos com orientacao anti-horaria devem ser os primeiros da lista,
# entao basta retornar o valor da orientacao, pois a orientacao anti-horaria tem valor negativo.
# Caso a orientacao seja igual a zero, o ponto mais proximo do ponto inicial deve vir primeiro.
def CompareOrientation(p1, p2):
    orientation = CalculateOrientation(startingPoint, p1, p2)

    if orientation: 
        return orientation
    if CalculateSquaredDistance(startingPoint, p1) <= CalculateSquaredDistance(startingPoint, p2):
        return -1
    return 1


if __name__ == "__main__":
    n = int(input())
    points = []

    assert n > 2, "Nao e possivel montar um poligono com menos de 3 pontos"

    for i in range(n):
        points.append(tuple(map(int, input().split(" "))))

    # Esse ponto deve ser global pois ele eh utilizado na funcao de comparacao do sorted().
    # A funcao de comparacao recebe apenas dois valores (os valores que estao sendo comparados), 
    # e por isso nao eh possivel passar o startingPoint como terceiro parametro.
    global startingPoint
    startingPoint = points[0]

    # Laco para encontrar o ponto com o menor Y.
    # Se dois pontos tiverem o mesmo Y, eh selecionado o mais a esquerda
    # Complexidade: O(n)
    for r in points:
        if r[1] < startingPoint[1]:
            startingPoint = r
        elif r[1] == startingPoint[1] and r[0] < startingPoint[0]:
            startingPoint = r

    # Ordenacao dos pontos com base no angulo com o startingPoint
    # key=cmp_to_key() eh utilizado para alterar a funcao de comparacao
    # entre dois valores da estrutura
    # Complexidade: O(nLogN)
    points = sorted(points, key=cmp_to_key(CompareOrientation))

    # O ponto inicial sempre fara parte do fecho convexo
    filteredPoints = [startingPoint]

    # Nessa etapa do algoritmo, sao removidos os pontos colineares
    # e mantidos somente o ponto mais distante.
    # Caso um ponto nao seja colinear com o proximo ponto, entao ele 
    # eh o ponto mais distante do startingPoint com aquele angulo
    # Complexidade: O(n)
    for i in range(1, len(points) - 1):
        if CalculateOrientation(startingPoint, points[i], points[i+1]):
            filteredPoints.append(points[i])
    filteredPoints.append(points[-1])

    assert len(filteredPoints) > 2, "Nao ha mais de 2 pontos nao colineares entre si"

    # A etapa final do algoritmo eh o scan em si.
    # Os pontos que fazem parte do fecho sao guardados em uma pilha.

    # A pilha eh iniciada com os 3 primeiros pontos filtrados.
    resultStack = [startingPoint, filteredPoints[1], filteredPoints[2]]

    # Para cada ponto p restante, eh verificada sua orientacao com o ultimo
    # e o penultimo ponto da pilha. Se esses 3 pontos forem colineares ou de
    # orientacao horaria, significa que o ultimo ponto da pilha nao faz parte
    # do fecho, e entao ele eh removido. Agora, o ponto p sera comparado com os
    # novos ultimo e penultimo pontos.
    # Caso o ponto p tenha uma orientacao anti-horária, ele eh adicionado ao topo da pilha
    # Complexidade: O(n)
    for p in filteredPoints[3:]:
        while len(resultStack) > 1 and CalculateOrientation(resultStack[-2], resultStack[-1], p) >= 0:
            resultStack.pop()
        resultStack.append(p)

    print(resultStack)
```


## Grande Tratado da Bytelândia
A Grande Guerra da Bytelândia chegou ao fim. Os reinos restantes agora estão discutindo o Tratado
de Divisão, que dividirá todas as terras do mundo entre eles. Este tratado se refere não apenas ao
mundo conhecido, mas também a quaisquer territórios ainda não descobertos ou habitados, incluindo
terra ou mar. Podemos assumir que o mundo é um plano infinito.

Cada reino no continente da Bytelândia tem uma única capital, e o Tratado de Divisão será baseado
em suas localiza¸cões: ele declara que cada pedaço de terra pertence ao reino cuja capital é a mais
próxima em um voo de pássaro (ou em linha reta). Em outras palavras: onde quer que você esteja no
mundo, se $C$ é a capital mais próxima de você, você estará no território do reino de C. Se houver um
empate entre as distâncias de duas ou mais capitais, esse lugar estará na fronteira entre seus reinos.

Sob este tratado, alguns reinos podem ficar cercados por outros, enquanto outros reinos podem
ficar com território ilimitado. Por isso, alguns monarcas estão contestando o tratado. Para informar
essa discussão, eles exigem sua ajuda. Dadas as coordenadas das localizações de cada capital no
continente da Bytelândia, você deve descobrir quais reinos teriam territórios infinitos sob o Tratado
de Divisão.

### Entrada
A primeira linha da entrada contém um único inteiro $N (2 ≤ N ≤ 10^5)$, o número de reinos.
Cada reino é identificado por um número inteiro único entre 1 e N. Cada uma das N linhas seguintes
contém dois inteiros $X$ e $Y$ $(0 ≤ X, Y ≤ 10^4)$, as coordenadas 2D da localização da capital de um
reino. As capitais são dadas em ordem crescente de identificador do reino, não há duas capitais com
a mesma localização, e você pode assumir que toda capital tem tamanho insignificante.

### Saída
Imprima uma única linha com uma lista de inteiros separados por espaço em ordem crescente:
os identificadores dos reinos que teriam territórios infinitos sob o Tratado de Divisão descrito. É
garantido que sempre haverá pelo menos um reino assim.

<hr>

O problema fornece uma série de reinos, representados por pontos, e quer descobrir quais deles possuem terrenos infinitos. Utilizando o Diagrama de Voronoy, uma forma de decomposição que divide o espaço em áreas mais próximas a determinado pontos, podemos fácilmente visualizar o problema.

![voronoy](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/16589959-2bc6-4a85-b324-f90f1ef7e2ad)

Com o desenho dos pontos, é possível perceber que os reinos com terrenos infinitos são aqueles que fazem parte do envóltorio convexo. Entretanto, torna-se necessário realizar algumas adaptações no algoritmo de Graham Scan, pois, diferentemente do problema original, precisamos considerar também os pontos que estão na borda do envoltório, mas não são vértices do menor polígono.

O primeiro passo, então, é modificar o nosso algoritmo para que ele não remova pontos colineares, isto é, os pontos em que o produto vetorial seja igual a 0. 

### C++
```cpp
        // Modificamos a regra para remover os pontos apenas no sentido horário, ou seja, apenas
        // os que o produto vetorial for negativo (< 0).
        while (hull.size() >= 2 && cross_product(hull[hull.size() - 2], hull[hull.size() - 1], points[i]) < 0)
        {
            hull.pop_back();
        }
```

### Python
```python
        # O trecho que remove os pontos colineares deve ser removido da implementação
        for i in range(1, len(points) - 1):
            if CalculateOrientation(startingPoint, points[i], points[i+1]):
                filteredPoints.append(points[i])
        filteredPoints.append(points[-1])

        # O trecho do scan deve ser modificado, para remover somente os pontos no sentido horário, ou seja,
        # apenas os que a diferença entre a subida seja positiva (> 0).
        while len(resultStack) > 1 and CalculateOrientation(resultStack[-2], resultStack[-1], p) > 0:
            resultStack.pop()
```

Isso, porém, gera um pequeno problema. Quando os pontos possuírem o mesmo ângulo com o ponto inicial P, o algoritmo verificará os pontos do mais próximo para o mais distante pelas nossas regras de ordenação. Entretanto, caso esse pontos sejam os últimos, a curva realizada quando partirmos para o ponto seguinte será no sentido horário e o ponto anterior será removido.

![colineares](https://github.com/jaimeadf/Material-da-Maratona/assets/40345645/ece6be0a-7a55-4b28-a9be-93d42370a3d6)

*O algoritmo verifica inicialmente o ponto F e, quando parte para o ponto E, uma curva horária é formada e o F removido. Os polígono resultante será ABCDE.*

A solução para esse caso é reverter a ordem dos pontos colineares com maior ângulo para que eles sejam verificados da maior para a menor distância.
```cpp
    std::sort(...);

    size_t colinear_index = points.size() - 2;

    // Encontra os últimos pontos colineares em relação a P0.
    while (colinear_index > 0 && cross_product(p0, points.back(), points[colinear_index]) == 0)
    {
        colinear_index--;
    }

    // Inverte os pontos colineares para serem ordenados da maior para a menor distância.
    std::reverse(points.begin() + colinear_index + 1, points.end());
```

Outra solução para tratar os últimos pontos colineares é verificar se há mais pontos colineares entre o ponto inicial e o último ponto do polígono convexo. Caso haja mais pontos colineares ($CalculateOrientation == 0$), eles serão adicionados em um vetor. Esse vetor só será adicionado à pilha final caso existam outros pontos no polígono que não são colineares entre o último ponto e o ponto inicial. Essa extensão dos pontos resultantes deve seguir essa regra para evitar que os pontos sejam reinseridos caso o polígono inicialmente calculado seja composto somente de pontos colineares (os primeiros pontos calculados).
```python
    lastCollinear = []

    for i in range(len(reinos) - 2):
        if not CalculateOrientation(resultStack[-1], reinos[-2-i], start):
            lastCollinear.append(reinos[-2-i])
        else:
            resultStack.extend(lastCollinear)
            break
```

Por fim, adicionamos a leitura das entradas e imprimimos os pontos ordenados por um campo identificador.

## C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Point
{
    int id;

    int x;
    int y;
};

int distance_squared(const Point &a, const Point &b)
{
    int dx = a.x - b.x;
    int dy = a.y - b.y;

    return dx * dx + dy * dy;
}

int cross_product(const Point &a, const Point &b, const Point &c)
{
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

std::vector<Point> graham_scan(std::vector<Point> &points)
{
    if (points.size() <= 3)
    {
        return points;
    }

    std::vector<Point> hull;

    Point p0 = points[0];

    for (size_t i = 1; i < points.size(); i++)
    {
        if (points[i].y < p0.y || (points[i].y == p0.y && points[i].x > p0.x))
        {
            p0 = points[i];
        }
    }

    std::sort(points.begin(), points.end(), [&](Point &a, Point &b) {
        int product = cross_product(p0, a, b);

        if (product != 0)
        {
            return product > 0;
        }

        int distance_b = distance_squared(p0, b);
        int distance_a = distance_squared(p0, a);

        return distance_a < distance_b;
    });

    size_t colinear_index = points.size() - 2;
    while (colinear_index > 0 && cross_product(p0, points.back(), points[colinear_index]) == 0)
    {
        colinear_index--;
    }

    std::reverse(points.begin() + colinear_index + 1, points.end());

    for (size_t i = 0; i < points.size(); i++)
    {
        while (hull.size() >= 2 && cross_product(hull[hull.size() - 2], hull[hull.size() - 1], points[i]) < 0)
        {
            hull.pop_back();
        }

        hull.push_back(points[i]);
    }

    return hull;
}

int main()
{
    std::ios_base::sync_with_stdio(false);

    size_t length;
    std::cin >> length;

    std::vector<Point> kingdoms(length);    
    
    for (size_t i = 0; i < length; i++)
    {
        kingdoms[i].id = i + 1;
        std::cin >> kingdoms[i].x >> kingdoms[i].y;
    }

    std::vector<Point> hull = graham_scan(kingdoms);

    std::sort(hull.begin(), hull.end(), [&](Point &a, Point &b) {
        return a.id < b.id;
    });

    for (const Point &point : hull)
    {
        std::cout << point.id << " ";
    }

    return 0;
}
```

## Python
```python
from functools import cmp_to_key


def CalculateOrientation(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p3[1] - p2[1]) * (p2[0] - p1[0])

def CalculateSquaredDistance(p1, p2):
    return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2

def CompareOrientation(p1, p2):
    orientation = CalculateOrientation(start, p1, p2)

    if orientation: 
        return orientation
    if CalculateSquaredDistance(start, p1) <= CalculateSquaredDistance(start, p2):
        return -1
    return 1


n = int(input())
reinos = []

for i in range(n):
    info = input().split(" ")
    info.append(i+1)
    reinos.append(tuple(map(int, info)))

if n < 4:
    output = ""
    for r in reinos:
        output += str(f"{r[2]} ")

    print(output[:-1])
    quit()

start = reinos[0]

for r in reinos:
    if r[1] < start[1]:
        start = r
    elif r[1] == start[1] and r[0] < start[0]:
        start = r

reinos = sorted(reinos, key=cmp_to_key(CompareOrientation))
resultStack = [start, reinos[1], reinos[2]]

for p in reinos[3:]:
    while len(resultStack) > 1 and CalculateOrientation(resultStack[-2], resultStack[-1], p) > 0:
        resultStack.pop()
    resultStack.append(p)

lastCollinear = []

for i in range(len(reinos) - 2):
    if not CalculateOrientation(resultStack[-1], reinos[-2-i], start):
        lastCollinear.append(reinos[-2-i])
    else:
        resultStack.extend(lastCollinear)
        break

resultStack.sort(key=lambda x: x[2])
output = ""
for r in resultStack:
    output += str(f"{r[2]} ")

print(output[:-1])
```


# Material sobre interseccoes

## Codigo para checar se um ponto esta em um poligono convexo ##

Nao entendi, mas coloquei aqui.

```cpp
struct pt {
    long long x, y;
    pt() {}
    pt(long long _x, long long _y) : x(_x), y(_y) {}
    pt operator+(const pt &p) const { return pt(x + p.x, y + p.y); }
    pt operator-(const pt &p) const { return pt(x - p.x, y - p.y); }
    long long cross(const pt &p) const { return x * p.y - y * p.x; }
    long long dot(const pt &p) const { return x * p.x + y * p.y; }
    long long cross(const pt &a, const pt &b) const { return (a - *this).cross(b - *this); }
    long long dot(const pt &a, const pt &b) const { return (a - *this).dot(b - *this); }
    long long sqrLen() const { return this->dot(*this); }
};

bool lexComp(const pt &l, const pt &r) {
    return l.x < r.x || (l.x == r.x && l.y < r.y);
}

int sgn(long long val) { return val > 0 ? 1 : (val == 0 ? 0 : -1); }

vector<pt> seq;
pt translation;
int n;

bool pointInTriangle(pt a, pt b, pt c, pt point) {
    long long s1 = abs(a.cross(b, c));
    long long s2 = abs(point.cross(a, b)) + abs(point.cross(b, c)) + abs(point.cross(c, a));
    return s1 == s2;
}

void prepare(vector<pt> &points) {
    n = points.size();
    int pos = 0;
    for (int i = 1; i < n; i++) {
        if (lexComp(points[i], points[pos]))
            pos = i;
    }
    rotate(points.begin(), points.begin() + pos, points.end());

    n--;
    seq.resize(n);
    for (int i = 0; i < n; i++)
        seq[i] = points[i + 1] - points[0];
    translation = points[0];
}

bool pointInConvexPolygon(pt point) {
    point = point - translation;
    if (seq[0].cross(point) != 0 &&
            sgn(seq[0].cross(point)) != sgn(seq[0].cross(seq[n - 1])))
        return false;
    if (seq[n - 1].cross(point) != 0 &&
            sgn(seq[n - 1].cross(point)) != sgn(seq[n - 1].cross(seq[0])))
        return false;

    if (seq[0].cross(point) == 0)
        return seq[0].sqrLen() >= point.sqrLen();

    int l = 0, r = n - 1;
    while (r - l > 1) {
        int mid = (l + r) / 2;
        int pos = mid;
        if (seq[pos].cross(point) >= 0)
            l = mid;
        else
            r = mid;
    }
    int pos = l;
    return pointInTriangle(seq[pos], seq[pos + 1], pt(0, 0), point);
}
```

## Sweep Line 2d

Ele verifica somente quando as linhas comecam ou terminam. Verifica se dois segmentos de reta se interceptam, e caso sim, retorna eles.

```cpp
const double EPS = 1E-9;

struct pt {
    double x, y;
};

struct seg {
    pt p, q;
    int id;

    double get_y(double x) const {
        if (abs(p.x - q.x) < EPS)
            return p.y;
        return p.y + (q.y - p.y) * (x - p.x) / (q.x - p.x);
    }
};

bool intersect1d(double l1, double r1, double l2, double r2) {
    if (l1 > r1)
        swap(l1, r1);
    if (l2 > r2)
        swap(l2, r2);
    return max(l1, l2) <= min(r1, r2) + EPS;
}

int vec(const pt& a, const pt& b, const pt& c) {
    double s = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
    return abs(s) < EPS ? 0 : s > 0 ? +1 : -1;
}

bool intersect(const seg& a, const seg& b)
{
    return intersect1d(a.p.x, a.q.x, b.p.x, b.q.x) &&
           intersect1d(a.p.y, a.q.y, b.p.y, b.q.y) &&
           vec(a.p, a.q, b.p) * vec(a.p, a.q, b.q) <= 0 &&
           vec(b.p, b.q, a.p) * vec(b.p, b.q, a.q) <= 0;
}

bool operator<(const seg& a, const seg& b)
{
    double x = max(min(a.p.x, a.q.x), min(b.p.x, b.q.x));
    return a.get_y(x) < b.get_y(x) - EPS;
}

struct event {
    double x;
    int tp, id;

    event() {}
    event(double x, int tp, int id) : x(x), tp(tp), id(id) {}

    bool operator<(const event& e) const {
        if (abs(x - e.x) > EPS)
            return x < e.x;
        return tp > e.tp;
    }
};

set<seg> s;
vector<set<seg>::iterator> where;

set<seg>::iterator prev(set<seg>::iterator it) {
    return it == s.begin() ? s.end() : --it;
}

set<seg>::iterator next(set<seg>::iterator it) {
    return ++it;
}

pair<int, int> solve(const vector<seg>& a) {
    int n = (int)a.size();
    vector<event> e;
    for (int i = 0; i < n; ++i) {
        e.push_back(event(min(a[i].p.x, a[i].q.x), +1, i));
        e.push_back(event(max(a[i].p.x, a[i].q.x), -1, i));
    }
    sort(e.begin(), e.end());

    s.clear();
    where.resize(a.size());
    for (size_t i = 0; i < e.size(); ++i) {
        int id = e[i].id;
        if (e[i].tp == +1) {
            set<seg>::iterator nxt = s.lower_bound(a[id]), prv = prev(nxt);
            if (nxt != s.end() && intersect(*nxt, a[id]))
                return make_pair(nxt->id, id);
            if (prv != s.end() && intersect(*prv, a[id]))
                return make_pair(prv->id, id);
            where[id] = s.insert(nxt, a[id]);
        } else {
            set<seg>::iterator nxt = next(where[id]), prv = prev(where[id]);
            if (nxt != s.end() && prv != s.end() && intersect(*nxt, *prv))
                return make_pair(prv->id, nxt->id);
            s.erase(where[id]);
        }
    }

    return make_pair(-1, -1);
}
```

# Volume Poliedros

 - Esfera: $(4/3) * pi * r^{3}$
 - Pirâmide: $areaBase * altura / 3$

# Area de Formas

## Triangulos (Fórmula de Herão)

Formula geral usando semi perimetro e seja tamanho dos lados do triangulo $a$, $b$ e $c$.

$$
    p = \frac{a+b+c}{2}
$$


$$
    A = \sqrt{p*(a-p)*(b-p) * (c-p)}
$$

## Área de Polígonos Regulares (de $n$ lados e lado $l$)

**Definição:** Um polígono regular é **CONVEXO** e possui todos os lados e ângulos **IGUAIS**.  

$a$ é o apótema (tamanho do segmento que liga o centro ao ponto médio de um dos lados fazendo um ângulo de 90 graus)

$p$ é o perímetro ($n * l$)

$$
    A = \frac{p * a}{2}
$$

## Lista de apótemas

 - triângulo: $a = \frac{l * \sqrt{2}}{6}$
 - quadrado: $a = \frac{l}{2}$
 - hexágono: $a = \frac{l * \sqrt{3}}{2}$


# Formulas genericas de pontos #

Material com estruturas e funcoes prontas para trabalhar com pontos 2D e 3D. As implementacoes sao para pontos em 3D, pois sao maiores do que as 2D. 

## Definicao da estrutura ##

```cpp
struct point3d {
    ftype x, y, z;
    point3d() {}
    point3d(ftype x, ftype y, ftype z): x(x), y(y), z(z) {}
    point3d& operator+=(const point3d &t) {
        x += t.x;
        y += t.y;
        z += t.z;
        return *this;
    }
    point3d& operator-=(const point3d &t) {
        x -= t.x;
        y -= t.y;
        z -= t.z;
        return *this;
    }
    point3d& operator*=(ftype t) {
        x *= t;
        y *= t;
        z *= t;
        return *this;
    }
    point3d& operator/=(ftype t) {
        x /= t;
        y /= t;
        z /= t;
        return *this;
    }
    point3d operator+(const point3d &t) const {
        return point3d(*this) += t;
    }
    point3d operator-(const point3d &t) const {
        return point3d(*this) -= t;
    }
    point3d operator*(ftype t) const {
        return point3d(*this) *= t;
    }
    point3d operator/(ftype t) const {
        return point3d(*this) /= t;
    }
};
point3d operator*(ftype a, point3d b) {
    return b * a;
}
```

## Funcoes genericas ##

```cpp
ftype dot(point3d a, point3d b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
}
ftype norm(point3d a) {
    return dot(a, a);
}
double abs(point3d a) {
    return sqrt(norm(a));
}
double proj(point3d a, point3d b) {
    return dot(a, b) / abs(b);
}
double angle(point3d a, point3d b) {
    return acos(dot(a, b) / abs(a) / abs(b));
}
point3d cross(point3d a, point3d b) {
    return point3d(a.y * b.z - a.z * b.y,
                   a.z * b.x - a.x * b.z,
                   a.x * b.y - a.y * b.x);
}
ftype triple(point3d a, point3d b, point3d c) { // Calcula area de poligono determinado pelos vetores a, b e c.
    return dot(a, cross(b, c));
}
```

