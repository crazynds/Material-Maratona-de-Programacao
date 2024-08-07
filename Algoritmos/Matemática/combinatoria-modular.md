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