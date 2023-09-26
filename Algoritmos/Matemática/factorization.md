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
