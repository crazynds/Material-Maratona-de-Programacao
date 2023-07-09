# Branchless Programing

A ideia consiste em evitar ao máximo o uso de *branchs* (jumps condicionais) no código de programação. A grande vantagem por traz disso vem por conta que ao fazer um *branch* condicional, o processador por ter uma arquitetura de pipeline, tenta fazer uma predição de qual caminho seguir (**taken** or **not tanken**), dessa forma quando a instrução de *branch* for totalmente executada na pipeline, o processador vai descobrir se a desição tomada estava correta, caso não esteja toda a pipeline é limpada, e todos os ciclos até a tomada de decisão do *branch* serão desperdiçados.

Atualmente os processadores modernos possuem mecanismos para *aprimorar* a predição das instruções de *branchs*, porém a predição não consegue ser precisa para todos os tipos de algoritmos. Geralmente esses casos estão relacionados a proporção de **taken** e **not tanken** de um determinado trecho de código (quanto maior for a diferença das proporções, mais dificil para o processador para realizar a predição).

No geral, programação *branchless* pode dar um ganho legal no desenvolvimento, porém é praticamente inutil, e serve mais para 'otimização extrema', na hora de participar de competições, ninguém vai pensar em técnicas *branchless* de otimização. 

O compilador também busca automaticamente fazer adaptações no código para torna-lo *branchless* sempre que ele achar melhor, oque torna a práticar de escrever código nesse formato mais inutil ainda.

> Writing branchless code can speed up the process. But we’re talking about fractions of a second here. If you’re doing anything in a loop and repeating it over and again, this might be intriguing. It is not important in “regular” day-to-day scripting. However, in intensive computational programmings, such as gaming or machine learning, it soon becomes a crucial factor. Especially if you have limited CPU and memory resources.



## Códigos Exemplos

```c++

// Note que as funções abaixo são muito piores que suas versões não branchless, é bem interessante dar uma estudada do porque
int min(int a,int b){
    return a*(a<b)+b*(b<=a)
}
int max(int a,int b){
    return a*(a>b)+b*(b>=a)
}
```


## Referências


- https://www.youtube.com/watch?v=bVJ-mWWL7cE&ab_channel=Creel
- https://dev.to/jobinrjohnson/branchless-programming-does-it-really-matter-20j4
- https://en.algorithmica.org/hpc/pipelining/branchless/
- https://mesumali26-ma.medium.com/branchless-programming-with-python-124a85bd7481