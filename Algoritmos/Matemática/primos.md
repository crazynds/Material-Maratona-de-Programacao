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
        if checkComposite(n,a,d,s)
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
def isPrime(n, k=5): # miller-rabin deterministico para 64 bits
    if n < 2: return False
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]: # 12 primeiros primos
        if n==a:
            return True
        if checkComposite(n,a,d,s)
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
