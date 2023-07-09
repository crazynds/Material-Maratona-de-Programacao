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