'''
    Programa para fazer um gráfico de tempo de execução de diferentes programas para entradas numéricas n e k
    delimitadas por \n. Para outros tipos de entrada, é necessário adaptação. Utilizado em linux.

    Exemplo de entrada:
    1 3         -> casos de teste
    20 9        -> ..
    35 1        -> ..
    4 30        -> ..
    10000 12    -> ..

    Entrada termina com EOF.

    Autor: Natã Schmitt

    22/10/2022
'''

import subprocess
from random import randint
from datetime import datetime
from matplotlib import pyplot as plt


EXECUTIONS_PER_N = 1 # execuções para cada N, é gerado uma média para cada N

FILENAMES = ['./exemplo_programa_cpp', 'python3 exemplo_python.py'] # nomes dos executáveis pra rodar, caso for python, adicione python3 antes do .py

N_FROM_TO = range(1,5_000_000,100_000) # N inicial, N final, passo de N

RAND_FUNC_N = lambda: randint(1,30) # [mínimo, máximo) para cada n
RAND_FUNC_K = lambda: randint(1,30) # [mínimo, máximo) para cada k



nl = '\n'

results = [[] for _ in range(len(FILENAMES))]

fig, ax = plt.subplots(1,1)



def bench(f):
    times = []
    k = 0
    for _ in range(EXECUTIONS_PER_N):
        
        dt = datetime.now()
        subprocess.check_output(f'cat input | {f} 1>/dev/null', shell=True,text=True)
        dt = datetime.now() - dt
        k+= dt.total_seconds()
        print(f'processing program {f.ljust(30)} n: {str(i).center(15)} runtime:\t{dt.total_seconds():.4f}')

    times.append((i, k/EXECUTIONS_PER_N))
    return times

with open('input', 'w+') as f:
    pass

try:
    with open('input', 'a') as F:
        for i in N_FROM_TO:
            ns = f'{nl.join([f"{RAND_FUNC_N()} {RAND_FUNC_K()}" for _ in range(N_FROM_TO.step if i > N_FROM_TO.step else i)])}\n'
            F.write(ns)

            for ind, program in enumerate(FILENAMES):
                results[ind].extend(bench(program))

except KeyboardInterrupt:
    pass


for ind, program in enumerate(FILENAMES):
    ax.plot([a[0] for a in results[ind]], [a[1] for a in results[ind]], label=program)


ax.set_xlabel('Tamanho da entrada')
ax.set_ylabel('Tempo de execução')

plt.tight_layout()
plt.legend()

plt.show() 
