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
    
    Colaboradores: 
     - Luiz Henrique B. Lago

'''
import yaml
import subprocess
from random import randint,uniform
from datetime import datetime
from matplotlib import pyplot as plt


config = yaml.safe_load(open("config.yml"))

RUN_CONFIG = config['config']; 

EXECUTIONS_PER_N = RUN_CONFIG['repeat'] # execuções para cada N, é gerado uma média para cada N

FILENAMES = config['filenames'] # nomes dos executáveis pra rodar, caso for python, adicione python3 antes do .py

START_N = RUN_CONFIG['start']
MAX_N = RUN_CONFIG['end']
STEP_N = RUN_CONFIG['step']

INPUT_CONFIG = config['input']

VARIABLES = INPUT_CONFIG['variables']

for var in VARIABLES:
    type = VARIABLES[var]['type']
    start = VARIABLES[var]['start']
    end = VARIABLES[var]['end']
    match type:
        case 'intrand':
            VARIABLES[var] = lambda: randint(start,end)
        case 'floatrand':
            VARIABLES[var] = lambda: round(uniform(start,end),6)

nl = '\n'

results = [[] for _ in range(len(FILENAMES))]

fig, ax = plt.subplots(1,1)

N_FROM_TO = range(START_N,MAX_N,STEP_N)

def bench(f):
    times = []
    k = 0
    print(f'Started benchmark of {f.ljust(30)} n: {str(i).center(15)}')
    
    dt = datetime.now()

    for _ in range(EXECUTIONS_PER_N):
        subprocess.run([f,'input'])

    dt = datetime.now() - dt
    mediaTime = dt.total_seconds()/EXECUTIONS_PER_N
    print(f'Ended benchmark of {f.ljust(30)} runtime:\t{mediaTime:.4f}')
    times.append((i, mediaTime))
    return times

def createFormatedInput():
    format = INPUT_CONFIG['format']
    for var in VARIABLES:
        search = '{'+var+'}'
        pos = format.find(search)
        while pos!=-1:
            val = VARIABLES[var]()
            format = format.replace(search,str(val),1)
            pos = format.find(search)
    return format


with open('input', 'w+') as f:
    pass

try:
    with open('input', 'a') as F:
        for i in N_FROM_TO:
            ns = f'{nl.join([createFormatedInput() for _ in range(N_FROM_TO.step if i > N_FROM_TO.step else i)])}\n'
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
