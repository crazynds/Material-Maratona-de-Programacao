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


Código em python:

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
 