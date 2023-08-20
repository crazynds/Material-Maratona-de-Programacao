# Combinatória modular

Fermat’s little theorem and modular inverse 
Fermat’s little theorem states that if $p$ is a prime number, then for any integer a, the number $a^p – a$ is an integer multiple of p. In the notation of modular arithmetic, this is expressed as: 
$$
a^p = a (\mathrm{mod}\ p) 
$$
For example, if $a = 2$ and $p = 7$, $2^7 = 128$, and $128 – 2 = 7 × 18$ is an integer multiple of 7.

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