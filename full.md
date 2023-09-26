# Matemática

# Fibonacci 
Na matemática, a sucessão de Fibonacci (ou sequência de Fibonacci), é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores. 

Definição: $fib(n) = fib(n-1) + fib(n-2)$, para $n \gt 1$. 
Note que $fib(0) = 0$ e $fib(1) = 1$

## Período de Pisano

A sequência de Fibonacci mod M é sempre periódica. Ou seja, para um M no qual o periodo seja 6, como o Pisano de 4, fibonacci de 0 e o de 6 será o mesmo, e o de 1 e o 7 também, e assim por diante, de forma que a equação abaixo é verdadeira:

Função de Pisano = $\pi (k)$  

**OBS:** Essa propriedade é muito útil para calcular $fib(n) \bmod M$ quando n for um número muito grande, pois:

$$
fib(n) \bmod M = fib(n \bmod \pi (M)) \bmod M
$$

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

# Números primos


## Checagem rápida de se um número é primo

Se retornar false então é 100% de certeza que não é primo, mas não garante que é primo se retornar True. Aumentar o $k$ aumenta a certeza. 


```python
def isPrime(n, k=5): # miller-rabin
    from random import randint
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
       if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for _ in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for _ in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True
```



## Fatorização de um número

A fatorização de um número é a decomposição de um números pelos seus primos geradores. Por exemplo o número 24 pode ser decomposto em: $2*2*2*3$ ou $2^3*3$. 

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


## Algoritmo Sieve (Pré-computar primos)

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

# Aritimética modular

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


## Potencia com Módulo

Para potencia com módulo, em C temos o seguinte código:
```c
// Fast pow and mod
long long modpow(long long base, long long exp, long long modulus) {
    base %= modulus;
    T result = 1;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % modulus;
        base = (base * base) % modulus;
        exp >>= 1;
    }
    return result;
}
```

Em python temos a função modpow implementada nativamente na função ```pow```. O primeiro parametro é a base, o segundo o expoente e o terceiro é o módulo.


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
def ncr(n, r, p):
    # initialize numerator and denominator
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p
```
Dicas de otimização:

 - Se o $p$ é constante, é possivel pre-computalo no inicio do programa. 
 - Se o $n$ é constante, é possivel pré-computar.
 

Exemplo do programa em c++:
 ```c++
// fatorial já ta pre computado FAT[]
// invFatorial também INV[]

const long long MOD = XXXXXX    // Funciona apenas para primos entre si, ou seja, se o MOD for primo vai funcionar
invFatoria[0] = 1

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


## Máximo Divisor Comum

Calcula o máximo divisor entre 'a' e 'b'

Ex: mdc(12, 8) = 4
```c++
int mdc(int a, int b) { 
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

**OBS: Utiliza a fórmula do mdc**

```c++
#include <cstdlib> /*para poder utilizar o abs(int)*/
int mmc(int a, int b)
{
   return abs(a * b) / mdc(a,b);
}
```
**OBS: mmc(a, b, c) = mmc(mmc(a, b), c)**


# Em Python (melhor)

```python
from math import gcd, lcm

print(gcd(12,8)) # maior divisor comum
# 4

print(lcm(3,4)) # menor multiplo comum
# 12

# Função feita na mão:
def mdc(a, b):
    while b > 0:
        a = a % b
        a ^= b
        b ^= a
        a ^= b
    return a
```

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


# Algoritmos de Busca

## Busca Binária

```c++
/*faz uma busca binaria em vetor a procura pelo indice do valor que seja maior ou igual a val. */
int busca(int *vet, int val, int tamanho)
{
    int ini = 0, fim = tamanho-1;

    if(val > vet[fim] )
        return tamanho;
    if(val < vet[0] )  //aumentou o desempenho
        return 0;

    int achou = tamanho; /*posicao fora do range = nao achou*/
    while(ini <= fim)
    {
        int meio = (ini + fim )/2;
        int elem = vet[meio];
        if( elem >= val )
        {
            achou = meio;
            fim = meio - 1;
        }
        else /*if( elem < val ) */
            ini = meio + 1;
    }
    return achou;
}
```


# Busca binária em C++


## std::sort

```c++
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    vector<int> vec(7,3,7,4);

    // ordena bem default msm
    sort(vec.begin(),vec.end());

    struct l{
        int a,b;
    };

    vector<struct l> vec2;

    vec2.push_back({1,2});
    vec2.push_back({5,7});
    vec2.push_back({3,1});
    vec2.push_back({9,2});
    vec2.push_back({2,6});  
    // Ordena vetor de struct
    sort(vec2.begin(),vec2.end(),
        // Lambda function in C++ OMG!!!!!
        [](const struct l& s1,const struct l& s2 ){
            if(s1.a==s2.a)return s1.b < s2.b; 
            return s1.a < s2.a;
        });

}

```

## std::lower_bound / std::upper_bound

```c++
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    // Vetor ordenado
    vector<int> vec(1,3,5,7,9);

    // retorna um iterador para o menor elemento que é maior ou igual ao valor passado
    auto it1 = lower_bound(vec.begin(),vec.end(),5);
    // retorna um iterador para o maior elemento que é menor ou igual ao valor passado
    auto it2 = upper_bound(vec.begin(),vec.end(),4);

    struct l{
        int a,b;
    };

    // Vetor ordenado
    vector<struct l> vec2;

    // retorna um iterador para o menor elemento que é maior ou igual ao valor passado
    auto it3 = lower_bound(vec.begin(),vec.end(),5,
        [](const struct l& s1,const int v ){ // LAMBDA FUNCTION IN C++ OMG!!!!
            return s1.a < v;
        });
    // retorna um iterador para o maior elemento que é menor ou igual ao valor passado
    auto it4 = upper_bound(vec.begin(),vec.end(),4,
        [](const struct l& s1,const int v ){ // OTHER LAMBDA FUNCTION IN C++ OMG!!!!
            return s1.a < v;
        });

}
```


## std::distance

```c++
int main(){
    // Vetor ordenado
    vector<int> vec(1,3,5,7,9);

    // retorna um iterador para o menor elemento que é maior ou igual ao valor passado
    auto it1 = lower_bound(vec.begin(),vec.end(),5);
    int idx1 = distance(vec.begin(),it1);

    // retorna um iterador para o maior elemento que é menor ou igual ao valor passado
    auto it2 = upper_bound(vec.begin(),vec.end(),4);
    int idx2 = distance(vec.begin(),it2);

}
```


# Grafos


# Passeios Eulerianos

Um passeio Euleriano em um grafo conexo é um passeio fechado que usa cada aresta do grafo exatamente uma vez. Um grafo conexo é Euleriano se contiver um passeio Euleriano.

## As Pontes de Königsberg

Discutia-se nas ruas da cidade a possibilidade de atravessar todas as pontes sem repetir nenhuma. Havia-se tornado uma lenda popular a possibilidade da façanha quando Euler, em 1736, provou que não existia caminho que possibilitasse tais restrições.

Euler transformou os caminhos em retas e suas intersecções em pontos, criando possivelmente o primeiro grafo da história. Então percebeu que só seria possível atravessar o caminho inteiro passando uma única vez em cada ponte se houvesse exatamente zero ou dois pontos de onde tivessem um número ímpar de caminhos. 

A razão de tal coisa é que de cada ponto deve haver um número par de caminhos, pois será preciso um caminho para "entrar"e outro para "sair". Os dois pontos com caminhos ímpares referem-se ao início e ao final do percurso, pois estes não precisam de um para entrar e um para sair, respectivamente. Se não houver pontos com número ímpar de caminhos, pode-se (e deve-se) iniciar e terminar o trajeto no mesmo ponto, podendo esse ser qualquer ponto do grafo. Isso não é possível quando temos dois pontos com números ímpares de caminhos, sendo obrigatoriamente um o início e outro o fim.

# Fluid Fill

## Versão recursiva

A versão recursiva é a mais fácil de entender o algoritmo, então segue o código:

```python

def floodFill(matrix,x,y,cache: set):
    restrictedValue = matrix[x][y]
    cont = 1
    cache.add((x,y))  # Add this position to set
    
    for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
        # new position
        nX,nY = x+a,y+b
        # check if x and y is valid positions in the matrix
        if not (0 <= nX < len(matrix) and 0<= nY < len(matrix[nX])):
            continue

        # check if new positions is valid to go and if this positions has not been visited
        if matrix[nX][nY] == restrictedValue and key not in cache:
            cont += floodFill(matrix,nX,nY,cache)

    return cont

```

## Versão não recursiva 

```python
def floodFill(matrix,x,y):
    restrictedValue = matrix[x][y]
    buffer = [(x,y)]

    # the directions to go
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    cache = set()
    cache.add((x,y))
    cont = 0
    while len(buffer)>0:
        # remove 1 position to process
        x,y = buffer.pop()
        # increment count
        cont += 1

        for a,b in directions:
            # new position
            key = (x+a,y+b)
            # check if x and y is valid positions in the matrix
            if not (0 <= key[0] < len(matrix) and 0<= key[1] < len(matrix[key[0]])):
                continue

            # check if new positions is valid to go and if this positions has not been visited
            if matrix[key[0]][key[1]] == restrictedValue and key not in cache:
                buffer.append(key)
                cache.add(key)  # Add position to set
    return cont
```

# Algoritmo de Dijkstra

```python
def dijkstra(nodes,src):
    """
        complexity: O(m*log(n))
        m = edges
        n = nodes

        this function return a list of distances from src

        can be faster if you implement heapDictionary (maybe?, in C++ using heapDictionary is faster, but in python i dont think...)
    """
    inf = float('inf')
    queue = []
    dist = [inf] * len(nodes)

    heapq.heappush(queue,(0,src))
    dist[src] = 0

    while queue:
        d,node = heapq.heappop(queue)
        if d > dist[node]:
            continue
        
        for child in nodes[node]:
            weigth = nodes[node][child]
            aux = dist[node] + weigth
            if dist[child] > aux:
                dist[child] = aux
                heapq.heappush(queue,(aux,child))
    return dist
```

## APSP

```python
def dijkstra_apsp(nodes):
    """
        complexity: O(n*m*log(n))
        m = edges
        n = nodes


        this function recive a list of nodes from a graph that can be directed or not
        this function return a matriz of shortest path from every node to other node
    """
    return [dijkstra(nodes,i) for i in range(len(nodes))]

```

# Bellman-Ford

```python

def bellmanford(edges: list,vertices,src):
    """
        complexity: O(m*n)
        m = edges
        n = nodes

        this function recives a directed list of edges that can contain negative weights
        this function return a list of distances from src
        different than dijkstra, the bellman ford can compute correct distances over negative edges
        work in directed graphs, there is no sense a non directed graph with negative edges (think about)

    """
    # In theory, sort the edges array can make the code fast because of the sequential reading of the array, but in reality this is over engineering
    # edges.sort()
    inf = float('inf')
    current = [inf]*vertices
    current[src] = 0

    ## Optional, only for backtrace
    trace = [i for i in range(vertices)]

    for _ in range(1,vertices): # run n-1 times
        change = False # premature optimization
        for s,d,w in edges:
            if current[s]!=inf and current[s] + w < current[d]:
                change = True
                current[d] = current[s] + w
                ## Optional, only for backtrace
                trace[d] = s

        if not change: # if any change in array ocurr, then already got the final result
            break
    else: # Run one more to check infinit loops
        # the path between 2 vertices has at max n-1 edges without negative loops, 
        # if the path has more than n-1 edges, so it has a negative loop in the graph 
        for s,d,w in edges:
            if last[s] + w < last[d]:
                ## 2nd return value is optional, only for backtrace
                return [float('-inf')]*vertices,trace

    ## 2nd return value is optional, only for backtrace
    return last,trace

```

# APSP

```python
def bellmanford_apsp(edges: list,vertices):
    """
        complexity: O(m*n^2)
        m = edges
        n = nodes

        this function recives a directed list of edges that can contain negative weights
        this function return a list of distances from every pair of nodes
        this is a variation of the original bellmanford algorithm that execute N * belmanford for every vertice

    """
    # In theory, sort the edges array can make the code fast because of the sequential reading of the array, but in reality this is over engineering
    # edges.sort()
    inf = float('inf')
    current = [[inf]*vertices  for _ in range(vertices)]
    for i in range(vertices):
        current[i][i] = 0

    ## Optional, only for backtrace
    trace = [[i for i in range(vertices)] for _ in range(vertices)]

    for _ in range(1,vertices): # run n-1 times
        change = False # premature optimization
        for s,d,w in edges:

            # this for loop can be boosted if implemented using SIMD instructions
            for i in range(vertices):
                if current[s][i]!=inf and current[s][i] + w < current[d][i]:
                    change = True
                    current[d][i] = current[s][i] + w
                    ## Optional, only for backtrace
                    trace[d][i] = s

        if not change: # if any change in array ocurr, then already got the final result
            break
    else: # Run one more to check infinit loops
        # the path between 2 vertices has at max n-1 edges without negative loops, 
        # if the path has more than n-1 edges, so it has a negative loop in the graph 
        for s,d,w in edges:
            for i in range(vertices):
                if current[s][i] + w < current[d][i]:
                    ## 2nd return value is optional, only for backtrace
                    return [float('-inf')]*n,trace

    # You need to rotate the array, so the src is the first index, and the dst is the second,
    # You can skip this if you wish, but the index are reversed, like: result[dst][src] = ShortestPath(src,dst)
    result = list(zip(*current))

    ## 2nd return value is optional, only for backtrace
    return result,trace

```

# Johnson Algorithm

```python
def johnson(edges: list, vertices):
    """
        complexity: O(n + m*n + m + n*m log n + n^2) = O(n*m log n)
        m = edges
        n = nodes

        this function recives a directed list of edges that can contain negative weights
        this function return a list of distances from every pair of nodes

    """
    # Add a new Vertice and add an edge from this vertice to every other vertice with weight zero
    newVertice = vertices
    edges.extend([(newVertice,i,0) for i in range(vertices)])

    # Compute a P_v for every vertice
    vW,_ = bellmanford(edges,vertices+1,newVertice)

    # Remove the edges previously added
    del edges[-vertices:]

    if vW[0] == float('-inf'):
        return [[float('-inf')]*vertices for _ in range(vertices)]

    # Apply the function to every edge
    newEdges = [(s,d,w+vW[s]-vW[d]) for s,d,w in edges]

    # Convert the new edges to a grahp
    nodes = convertEdgesArrayToDirectedSimpleGraph(newEdges,vertices)

    # Compute dijkstra to get the APSP
    bestPaths = [dijkstra(nodes,i) for i in range(vertices)]

    # Correct the values of the paths
    for i in range(vertices):
        for j in range(vertices):
            bestPaths[i][j] = bestPaths[i][j] - vW[i] + vW[j]

    return bestPaths
```

# Prim's Algorithm

```python
def primAlgorithm(graph,initialNode = 0):
    '''
        complexity: O(m*log(n))
        m = edges
        n = nodes

        this function return a list of edges of MST

        can be faster if you replace s(set) to a array of True or False
            - code needs to be adapted to this change;
    '''
    s = set()
    s.add(initialNode)
    tree = []

    arr = []
    a = initialNode
    for b in graph[a]:
        heapq.heappush(arr,(graph[a][b],a,b))

    while len(s)!=len(graph) and len(arr)>0:
        (cost,a,b) = heapq.heappop(arr)
        if b in s:
            continue
        
        tree.append((a,b,cost))
        s.add(b)
        
        a = b
        for b in graph[a]:
            if b not in s:
                heapq.heappush(arr,(graph[a][b],a,b))

        pass
    return tree 
```

# Kruskal's MST

```python
def kruskalsMST(edges: list,nodes: int):
    '''
        complexity: O(m*alpha(n)) + (sort operation)
        m = edges
        n = nodes

        this function return a list of edges of MST

        can be faster if yout implementation of SetUnion are better
    '''
    union = DisjointSetUnion(nodes)
    nEdges = []
    edges.sort(key=lambda e: e[2])
    for (a,b,cost) in edges:
        # Check if 'a' and 'b' already are in the same cluster
        if union.find(a) != union.find(b):
            union.union(a,b)
            nEdges.append((a,b,cost))
    return nEdges
```

# Espaçamento entre clusters

```python
from collections import deque

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.groups = set(self.parent)
 
    def find(self, x):
       if self.parent[x] != x:
           self.parent[x] = self.find(self.parent[x])
       return self.parent[x] 

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.size[root_y] > self.size[root_x]:
            root_x, root_y = root_y, root_x
        elif self.size[root_y] == self.size[root_x]:
            self.size[root_x] += 1

        # delete root_y group
        self.groups.remove(root_y)
        self.parent[root_y] = root_x
    
    def num_groups(self):
        return len(self.groups)

def maxSpacingClustering(kClusters: int,nodes: int,edges: list):
    edges.sort(reverse=True,key=lambda e: e[2])
    union = DisjointSetUnion(nodes)
    # Une os vertices até que sobre apenas k clusters
    while len(edges)>0:
        # Note que a aresta é removida do array, sabe dizer porque?
        (a,b,_) = edges.pop()
        union.union(a,b)
        # Condição de parada
        if union.num_groups()<=kClusters:
            break
    # Procura a menor distancia entre 2 clusters
    minCost = float('inf')
    for (a,b,minCost) in reversed(edges):
        if union.find(a)!=union.find(b):
            break
    return minCost
```

Complexidade de tempo: O(M * alpha(n)) + sorting time (M * log M)

# Perfect matching Graph

```python

def perfectMatchGraph(graph):
    '''
        Check if in one graph every vertice can be matched with other vertice.
            without any vertice stays alone.

        If a vertice is matched with other, it can't be matched with any other vertice.
    '''
    nodes = len(graph)
    vert = [len(graph[a]) for a in range(nodes)]
    hp = [(len(graph[a]),a) for a in range(nodes)]
    heapq.heapify(hp)
    
    revGraph = getReverseGraph(graph)
    
    while len(hp)>0:
        g,a = heapq.heappop(hp)
        if vert[a] != g or vert[a]<0:
            continue
        if g==0:
            return False
        
        for b in graph[a]:
            if vert[b]>0:
                vert[b] = -1
                vert[a] = -1
                for c in revGraph[a]:
                    if vert[c] != -1:
                        vert[c] -= 1
                        heapq.heappush(hp,(vert[c],c))
                for c in revGraph[b]:
                    if vert[c] != -1:
                        vert[c] -= 1
                        heapq.heappush(hp,(vert[c],c))
                break
    return max(vert)<0

```

# Funções conversoras

```python
def convertEdgesArrayToNonDirectedSimpleGraph(edges,vertices):
    simplegraph = [{} for _ in range(vertices)]

    for (a,b,cost) in edges:
        simplegraph[a][b] = cost
        simplegraph[b][a] = cost
    return simplegraph

def convertEdgesArrayToDirectedSimpleGraph(edges,vertices):
    simplegraph = [{} for _ in range(vertices)]

    for (a,b,cost) in edges:
        simplegraph[a][b] = cost
    return simplegraph

def convertSimpleGraphToEdgesArray(simplegraph):
    edges = []

    for a in range(len(simplegraph)):
        for b in simplegraph[a]:
            if a<b:
                edges.append((a,b,simplegraph[a][b]))
    return edges

def convertEdgesArrayToTreeGraph(edges,vertices):
    FATHER = 0
    CHILD = 1
    treeGraph = [[None,[]] for _ in range(vertices)]
    simpleGraph = convertEdgesArrayToNonDirectedSimpleGraph(edges,vertices)
    def iterOverGraph(currentNode,father):
        treeGraph[currentNode][FATHER] = father
        for node in simpleGraph[currentNode]:
            if node!=father:
                treeGraph[currentNode][CHILD].append(iterOverGraph(node,currentNode))
        return currentNode
    root = iterOverGraph(0,None)
    return (treeGraph,root)

def getReverseGraph(graph):
    reverse = [{} for _ in range(len(graph))]
    for a in range(len(graph)):
        for b in graph[a]:
            reverse[b][a] = graph[a][b]
    return reverse

```	

# Algoritmos de Geometria Computacional

## Classe Point (Usando em alguns algoritmos)

```c++
class Point {
public:
   float x, y, z;

   Point() {
      x = y = z = 0;
   }

   Point(float x1, float y1, float z1) {
      x = x1;
      y = y1;
      z = z1;
   }

   Point operator - (Point a) {
      return Point(x - a.x, y - a.y, z - a.z);
   }

   Point operator + (Point a) {
      return Point (x + a.x, y + a.y, z + a.z);
   }

   Point operator / (float a) {
      return Point (x / a, y / a, z / a);
   }

   Point operator * (float a) {
      return Point (x * a, y * a, z * a);
   }
};
```


## Polígono

Sendo PI = π

```c++
/*Fórmula para achar o raio do polígono a partir da área 
'a' de um polígono com 'n' lados*/
raio = sqrt((2*a)/((double)n*sin((2*PI)/(double)n)));

/*lembrando que a área de um polígono pode ser calculada por:*/
area = ((l*raio)/2.0) * n;
/*tendo ‘l’ o comprimento do lado, 'raio' sendo o raio do círculo o qual o polígono é circunscrito (apótema) e
‘n’ o número de lados do polígono:*/

/*Fórmula da apótema do polígono usando o raio encontrado na fórmula acima*/
apotema = cos(PI/(double)n) * raio;

/*Área de um círculo inscrito em um polígono baseado na apótema encontrada na fórmula acima*/
area1 = PI*apotema*apotema;

/*Área de um círculo circunscrito num polígono com o raio encontrado acima*/
area2 = PI*raio*raio;

/* Calcula a area de um poligono irregular */

struct Point {
	float x, y;
};

//numP = número de pontos
float area_do_poligono(Point v[], int numP)
{
	float area = (v[numP - 1].y + v[0].y) * (v[numP - 1].x - v[0].x);

	for (int i = 0; i < numP - 1; i++)
    	{
		area += (v[i].y + v[i + 1].y) * (v[i].x - v[i + 1].x);
	}

	if (area < 0)
		area *= -1;

	return area / 2;
}

```


## Centro de um círculo a partir de 3 pontos (pontos cocirculares)
Resulta no circCentro que é o centro do círculo.

```c++
typedef struct Point {
   	double x,y;
}Point;

Point A,B,C;
Point circCentro;

double D = 2.0 * (A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y));
if (D==0.0) { /*Não existe círculo pois são colineares*/ }
circCentro.x = ((A.y*A.y + A.x*A.x) * (B.y - C.y) + (B.y*B.y + B.x*B.x) * (C.y - A.y) + (C.y*C.y + C.x*C.x) * (A.y - B.y))/D;
circCentro.y = ((A.y*A.y + A.x*A.x) * (C.x - B.x) + (B.y*B.y + B.x*B.x) * (A.x - C.x) + (C.y*C.y + C.x*C.x) * (B.x - A.x))/D;
```

## Área de Triângulo
Fórmula denominada Heron of Alexandria

Calcular a área A de um triângulo cujas arestas são de tamanho a, b e c.
Se Tivermos os vértices A B C do triângulo basta que 'a' 'b' e 'c' sejam os resultados dos cálculos das distâncias entre AB BC CA.

```c++
float areaOfTriangle(float a, float b, float c)
{
    float s = (a + b + c) * 0.5f;
    return sqrt(s*(s-a)*(s-b)*(s-c));
}

/* Fórmula básica de área de quadrado.
*/
float areaOfTriangle(float b, float h)
{
    return 0.5f * b * h;
}
```

## Distância entre dois Pontos
Fórmula para o cálculo de distância entre dois pontos.

```c++
float dist3D(Point a, Point b) {
    return sqrt(pow(b.x - a.x, 2)  +  pow(b.y - a.y, 2) + pow(b.z - a.z, 2));
}

float dist2D(Point a, Point b) {
    return sqrt(pow(b.x - a.x, 2)  +  pow(b.y - a.y, 2));
}
```

## Produto Vetorial

O produto vetorial entre os vetores $a$ e $b$ resulta em um vetor ortogonal (perpendicular) a ambos.
A norma do vetor resultante é: $|a| * |b| * sin(\alpha)$, sendo $\alpha$ o ângulo entre os vetores.

Se esse resultado for $0$, significa que os vetores são parelelos.

Esse resultado consiste na área do paralelogramo formado pelos vetores (ao dividir por 2, obtém-se a área do triângulo formado pelos vetores)

```c++
Point cross(Point a, Point b) {
    Point result;
    result.x = a.y * b.z - a.z * b.y;
    result.y = a.z * b.x - a.x * b.z;
    result.z = a.x * b.y - a.y * b.x;

    return result;
}
```

## Produto Escalar

O produto escalar entre os vetores $a$ e $b$ resulta em: $|a| * |b| * cos(\alpha)$, sendo $\alpha$ o ângulo entre os vetores.

Se o resultado for $0$, significa que os vetores são perpendiculares.

```c++
float dot(Point a, Point b) {
    return (a.x * b.x) + (a.y * b.y) + (a.z * b.z);
}
```

## Norma

A norma nada mais é que o tamanho do vetor. Para obtê-la, basta realizar a raiz quadrada da soma dos quadrados dos componentes.

```c++
float norma(Point a) {
    return sqrt(dot(a, a));
}
```

## Círculo

__THIS CIRCLE HAS BEEN SLICED INTO THE MAXIMUM NUMBER OF SECTIONS 
USING 10 SLICES. HOW MANY SECTIONS ARE THERE? HINT: COUNTING SECTIONS 
IS TOUGH!. TRY USING THE FORMULA PREVIOUSLY DEVELOPED.__


- Maximum number of sections of a Circle when sliced by a knife = [n(n+1)/2] +1.  
where "n" is the number of slices.

- A circle has an angle of 2 * PI and an Area of: PI * RAIO^2

- Area of Sector = (ANG/2) * RAIO^2              (when ANG is in radians)
- Area of Sector = ((ANG * PI/180)/2) * RAIO^2   (when ANG is in degrees)

- Arc Length = ANG * RAIO   (when ANG is in radians)
- Arc Length = ANG * PI/180 * RAIO   (when ANG is in degrees)

- Area of Segment  = (ANG - sin(ANG))/2 * RAIO^2   (when ANG is in radians)
- Area of Segment  = (ANG * PI/180 - sin(ANG))/2 * RAIO^2   (when ANG is in degrees)

## Intersecção entre retas (linhas ou segmentos), retornando o ponto da intersecção
p1 e p2 correspondem ao ponto inicial e final dado de uma linha1 

p3 e p4 correspondem ao ponto inicial e final dado de uma linha2

```c++
Point* intersection(Point p1, Point p2, Point p3, Point p4) {
    float x1 = p1.x, x2 = p2.x, x3 = p3.x, x4 = p4.x;
    float y1 = p1.y, y2 = p2.y, y3 = p3.y, y4 = p4.y;

    float d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);

    // Se d é zero, não há intersecção.
    if (d == 0)
    {
        return NULL;
    }

    // Pega o x e y do ponto de intersecção.
    float pre = (x1*y2 - y1*x2), post = (x3*y4 - y3*x4);
    float x = ( pre * (x3 - x4) - (x1 - x2) * post ) / d;
    float y = ( pre * (y3 - y4) - (y1 - y2) * post ) / d;
    /******************************************************************/
    // Checa se as coordenadas do ponto então entre os dois segmentos
    //OBS: Se for linhas, esse código deve ser comentado, pois essa
    //parte do código é apenas quando se lida com SEGMENTOS de reta.
    if ( x < min(x1, x2) || x > max(x1, x2) ||
        x < min(x3, x4) || x > max(x3, x4) ) return NULL;
    if ( y < min(y1, y2) || y > max(y1, y2) ||
        y < min(y3, y4) || y > max(y3, y4) ) return NULL;
    /******************************************************************/
    // Retorna o ponto da intersecção
    Point* ret = new Point();
    ret->x = x;
    ret->y = y;
    return ret;
}
```


## Intersecção entre segmentos de reta (retornando booleano)
p1 e p2 correspondem ao ponto inicial e final dado de uma linha1 

p3 e p4 correspondem ao ponto inicial e final dado de uma linha2

```c++
bool intersection(Point p1, Point p2, Point p3, Point p4) {
    float x1 = p1.x, x2 = p2.x, x3 = p3.x, x4 = p4.x;
    float y1 = p1.y, y2 = p2.y, y3 = p3.y, y4 = p4.y;

    float d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
    if (d == 0) return false;

    float pre = (x1*y2 - y1*x2), post = (x3*y4 - y3*x4);
    float x = ( pre * (x3 - x4) - (x1 - x2) * post ) / d;
    float y = ( pre * (y3 - y4) - (y1 - y2) * post ) / d;
    /******************************************************************/
    // Checa se as coordenadas do ponto então entre os dois segmentos
    //OBS: Se for linhas, esse código deve ser comentado, pois essa
    //parte do código é apenas quando se lida com SEGMENTOS de reta.
    if ( x < min(x1, x2) || x > max(x1, x2) ||
        x < min(x3, x4) || x > max(x3, x4) ) return false;
    if ( y < min(y1, y2) || y > max(y1, y2) ||
        y < min(y3, y4) || y > max(y3, y4) ) return false;
    /******************************************************************/
    return true;
}
```


## Linhas coincidentes
p1 e p2 correspondem ao ponto inicial e final dado de uma linha1 

p3 e p4 correspondem ao ponto inicial e final dado de uma linha2

```c++
bool linesCoincident(Point p1, Point p2, Point p3, Point p4)
{
    float nominator_ua = ((p4.x - p3.x)*(p1.y - p3.y)) - ((p4.y - p3.y)*(p1.x - p3.x));
    float denominator_ua = ((p4.y - p3.y)*(p2.x - p1.x)) - ((p4.x - p3.x)*(p2.y - p1.y));
    float nominator_ub = ((p2.x - p1.x)*(p1.y - p3.y)) - ((p2.y - p1.y)*(p1.x - p3.x));
    float denominator_ub = ((p4.y - p3.y)*(p2.x - p1.x)) - ((p4.x - p3.x)*(p2.y - p1.y));
    // - Se os nominadores e denominadores para ua e ub forem 0  linhas são coincidentes.
    // - se apenas os denominadores forem iguais a zero  as retas são paralelas (essa parte 
    // não está no código. Se precisa, adicionar depois).
    if(nominator_ua == 0.f && denominator_ua == 0.f
        && nominator_ub == 0.f && denominator_ub == 0.f)
    {
        return true;
    }
    return false;
}
```

## Testar linhas coincidentes, paralelas e intersecção entre elas
sendo x1 e y1 e x2 e y2 o ponto inicial e final de uma reta

sendo x3 e y3 e x4 e y4 o ponto inicial e final de outra reta

```c++
int x1, y1;
int x2, y2;
int x3, y3;
int x4, y4;
double m1=1.0*((x1-x2)*(y3-y4))-((y1-y2)*(x3-x4));
double m2=1.0*((x3-x4)*(y3-y1))-((y3-y4)*(x3-x1));
double m3=1.0*(-((x3-x1)*(y1-y2))+((y3-y1)*(x1-x2)));
/*Caso as linhas sejam coincidentes*/
if(m1==0 && m2==0 && m3==0)
{
    printf("Linhas coincidentes.\n");
}
/*Caso as linhas sejam paralelas*/
else if(m1==0)
{
    printf("Linhas paralelas\n");
}
/*Se não ocorrer nenhum desses casos
 *então há um ponto x y de intersecção
 *entre as duas linhas.
 */
else
{
    double intr1=m2/m1;
    double intr2=m3/m1;
    double x=x1+intr2*(x2-x1);
    double y=y1+intr1*(y2-y1);
    printf("Ponto de inteseccao: %.2lf %.2lf\n",x,y);
}
```



## **(NÃO TESTADO)** Distância entre segmentos de reta
```c++
/* SMALL_NUM = ?
* a1 e a2 é uma reta
* b1 e b2 é a outra reta
*/
#define SMALL_NUM 0.01f
float distanceSegmentToSegment(Point a1, Point a2, Point b1, Point b2) {
    Point u,v,w;
    u = a2 - a1;
    v = b2 - b1;
    w = a1 - b1;

    float a = dot(u,u);
    float b = dot(u,v);
    float c = dot(v,v);
    float d = dot(u,w);
    float e = dot(v,w);

    float D = a * c - b * b;

    float sc, sN, sD = D;
    float tc, tN, tD = D;

    if(D < SMALL_NUM)	{
        sN = 0;
        sD = 1;
        tN = e;
        tD = c;
    } else {
        sN = (b * e - c * d);
        tN = (a * e - b * d);

        if(sN < 0) {
            sN = 0;
            tN = e;
            tD = c;
        } else if (sN > sD) {
            sN = sD;
            tN = e + b;
            tD = c;
        }
    }

    if (tN < 0)	{
        tN = 0;
        if (-d < 0) {
            sN = 0;
        } else if (-d > a) {
            sN = sD;
        } else {
            sN = -d;
            sD = a;
        }
    } else if (tN > tD) {
        tN = tD;
        if ((-d + b) < 0.0) {
            sN = 0;
        } else if ((-d + b) > a) {
            sN = sD;
        } else {
            sN = (-d + b);
            sD = a;
        }
    }

    sc = (abs(sN) < SMALL_NUM ? 0 : sN/sD );
    tc = (abs(tN) < SMALL_NUM ? 0 : tN/tD );

    return norma(w + u * sc - v * tc);
}
```

## Distância Ponto a Linha
```c++
float distPointToLine(Point c, Point p1, Point p2) {
   Point pV;
   pV = p2 - p1;

   Point pW;
   pW = c - p1;

   float c1 = dot(pW, pV);
   float c2 = dot(pV, pV);
   float b = c1 / c2;

   Point proj;
   proj = p1 + pV * b;

   return dist(c, proj);
}
```

## **(NÃO TESTADO)** Distância Ponto a Segmento de Reta
```c++
float distPointToSegment(Point c, Point p1, Point p2) {
   Point pV;
   pV = p2 - p1;

   Point pW;
   pW = c - p1;

   float c1 = dot(pW, pV);
   if(c1 <= 0)
      return dist(c, p1);

   float c2 = dot(pV, pV);
   if(c2 <= c1)
      return dist(c, p2);

   float b = c1 / c2;

   Point proj;
   proj = p1 +  pV * b;

   return dist(c, proj);
}
```

## **(NÃO TESTADO)** Projeção de um Ponto em um Plano

projeçao do ponto thePoint no plano ABC

```c++
Point projectionInPlane(Point thePoint, Point a, Point b, Point c) {
    Point normal, p1p2, p1p3, p1p0;
    p1p2 = b - a;
    p1p3 = c - a;
    p1p0 = thePoint - a;
    normal = cross(p1p2, p1p3);

    float sb, sn, sd;

    sn = -dot(normal, p1p0);
    sd =  dot(normal, normal);

    sb = sn / sd;

    return thePoint + normal * sb;
}

float distPointToPlane(Point thePoint, Point a,Point b, Point c) {   
	return dist(thePoint, projectionInPlane(thePoint, a, b, c));
}
```

## **(NÃO TESTADO)** Ponto dentro de Polígonos
Testa se ponto está dentro de um poligono pelo numero de vezes q ele passa por arestas verticalmente, funciona somente em 2D

V[] = vertex points of a polygon V[n+1] with V[n]=V[0]

Return:  0 = outside, 1 = inside
```c++
int crossingNumbers(Point P, vector<Point> V) { // 2D
   int cn = 0;
   float vt;
   float next;

   for(int i = 0; i < V.size(); i++) {
      next = i + 1;

      if(next == V.size()) next = 0;
         
      if(((V[i].y <= P.y) && (V[next].y > P.y)) || 
         ((V[i].y > P.y) && (V[next].y <= P.y))) {
         vt = (float)(P.y - V[i].y) / (V[next].y - V[i].y);

         if (P.x < V[i].x + vt * (V[next].x - V[i].x))
            ++cn;
      }
   }
   return (cn % 2);
}
```

## (NÃO TESTADO) Sweep Line 

```c++
#include <bits/stdc++.h>
using namespace std;
 
// A point in 2D plane
struct Point
{
    int x, y;
};
 
// A line segment with left as Point
// with smaller x value and right with
// larger x value.
struct Segment
{
    Point left, right;
};
 
 
// An event for sweep line algorithm
// An event has a point, the position
// of point (whether left or right) and
// index of point in the original input
// array of segments.
struct Event {
    int x, y;
    bool isLeft;
    int index;
    Event(int x, int y, bool l, int i) : x(x), y(y), isLeft(l), index(i) {}
 
    // This is for maintaining the order in set.
    bool operator<(const Event& e) const {
            if(y==e.y)return x<e.x;
            return y < e.y;
    }
};
 
 
// Given three collinear points p, q, r, the function checks if
// point q lies on line segment 'pr'
bool onSegment(Point p, Point q, Point r)
{
    if (q.x <= max(p.x, r.x) && q.x >= min(p.x, r.x) &&
        q.y <= max(p.y, r.y) && q.y >= min(p.y, r.y))
       return true;
 
    return false;
}
 
// To find orientation of ordered triplet (p, q, r).
// The function returns following values
// 0 --> p, q and r are collinear
// 1 --> Clockwise
// 2 --> Counterclockwise
int orientation(Point p, Point q, Point r)
{
    // See https://www.geeksforgeeks.org/orientation-3-ordered-points/
    // for details of below formula.
    int val = (q.y - p.y) * (r.x - q.x) -
              (q.x - p.x) * (r.y - q.y);
 
    if (val == 0) return 0;  // collinear
 
    return (val > 0)? 1: 2; // clock or counterclock wise
}
 
// The main function that returns true if line segment 'p1q1'
// and 'p2q2' intersect.
bool doIntersect(Segment s1, Segment s2)
{
    Point p1 = s1.left, q1 = s1.right, p2 = s2.left, q2 = s2.right;
 
    // Find the four orientations needed for general and
    // special cases
    int o1 = orientation(p1, q1, p2);
    int o2 = orientation(p1, q1, q2);
    int o3 = orientation(p2, q2, p1);
    int o4 = orientation(p2, q2, q1);
 
    // General case
    if (o1 != o2 && o3 != o4)
        return true;
 
    // Special Cases
    // p1, q1 and p2 are collinear and p2 lies on segment p1q1
    if (o1 == 0 && onSegment(p1, p2, q1)) return true;
 
    // p1, q1 and q2 are collinear and q2 lies on segment p1q1
    if (o2 == 0 && onSegment(p1, q2, q1)) return true;
 
    // p2, q2 and p1 are collinear and p1 lies on segment p2q2
    if (o3 == 0 && onSegment(p2, p1, q2)) return true;
 
     // p2, q2 and q1 are collinear and q1 lies on segment p2q2
    if (o4 == 0 && onSegment(p2, q1, q2)) return true;
 
    return false; // Doesn't fall in any of the above cases
}
 
 
// Find predecessor of iterator in s.
 set<Event>::iterator pred(set<Event> &s, set<Event>::iterator it) {
    return it == s.begin() ? s.end() : --it;
}
 
// Find successor of iterator in s.
set<Event>::iterator succ(set<Event> &s, set<Event>::iterator it) {
    return ++it;
}
 
// Returns true if any two lines intersect.
int isIntersect(Segment arr[], int n)
{
    unordered_map<string,int> mp;  // to note the pair for which intersection is checked already
    // Pushing all points to a vector of events
    vector<Event> e;
    for (int i = 0; i < n; ++i) {
        e.push_back(Event(arr[i].left.x, arr[i].left.y, true, i));
        e.push_back(Event(arr[i].right.x, arr[i].right.y, false, i));
    }
 
    // Sorting all events according to x coordinate.
    sort(e.begin(), e.end(), [](Event &e1, Event &e2) {return e1.x < e2.x;});
 
    // For storing active segments.
    set<Event> s;
     int ans=0;
    // Traversing through sorted points
    for (int i=0; i<2*n; i++)
    {
        Event curr = e[i];
        int index = curr.index;
 
        // If current point is left of its segment
        if (curr.isLeft)
        {
            // Get above and below points
            auto next = s.lower_bound(curr);
            auto prev = pred(s, next);
            // Check if current point intersects with
            // any of its adjacent
            bool flag=false;
            if (next != s.end() && doIntersect(arr[next->index], arr[index])){
                string s=to_string(next->index+1)+" "+to_string(index+1);
                if(mp.count(s)==0){mp[s]++;ans++;} //if not already checked we can increase count in map
            }
            if (prev != s.end() && doIntersect(arr[prev->index], arr[index])){
                    string s=to_string(prev->index+1)+" "+to_string(index+1);
                if(mp.count(s)==0){mp[s]++;ans++;} //if not already checked we can increase count in map
            }
            // if same line segment is there then decrease answer as it got increased twice
            if(prev != s.end() && next != s.end() && next->index==prev->index)ans--;
 
 
            // Insert current point (or event)
            s.insert(curr);
        }
 
        // If current point is right of its segment
        else
        {
            // Find the iterator
            auto it=s.find(Event(arr[index].left.x, arr[index].left.y, true, index));
            // Find above and below points
            auto next = succ(s, it);
            auto prev = pred(s, it);
 
            // If above and below point intersect
            if (next != s.end() && prev != s.end())
               {  string s=to_string(next->index+1)+" "+to_string(prev->index+1);
                    string s1=to_string(prev->index+1)+" "+to_string(next->index+1);
                   if (mp.count(s)==0&&mp.count(s1)==0&&doIntersect(arr[prev->index], arr[next->index]))
                    ans++;
                    mp[s]++;
                  }
 
            // Remove current segment
            s.erase(it);
 
        }
    }
    //print pair of lines having intersection
 
    for(auto &pr:mp){
        cout<<"Line: "<<pr.first<<"\n";
    }
    return ans;
}
 
// Driver code
int main() {
    Segment arr[] = { {{1, 5}, {4, 5}}, {{2, 5}, {10, 1}},{{3, 2}, {10, 3}},{{6, 4}, {9, 4}},{{7, 1}, {8, 1}}};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout<<"Number of intersection points: "<<isIntersect(arr, n);
    return 0;
}
```
