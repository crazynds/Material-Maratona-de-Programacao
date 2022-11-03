# Números primos



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