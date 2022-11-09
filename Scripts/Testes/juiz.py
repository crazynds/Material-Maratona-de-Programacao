'''
    Programa para testar entradas e saídas de problemas da maratona SBC 2022.

    O programa é feito para rodar com o seguinte esquema de diretórios:

    .
    ├── F
    │   ├── input
    │   │   └── VARIOS_ARQUIVOS_DE_ENTRADA_AQUI
    │   └── output
    │       └── VARIOS_ARQUIVOS_DE_SAIDA_AQUI
    ├── juiz.py
    └── PROGRAMA_A_SER_TESTADO

    ao baixar os arquivos de entrada e saída, é necessário apenas copiar o juiz.py e o binário
    para uma pasta anterior ao problema, e tudo vai funcionar.

    sempre execute o programa com python3 juiz.py (nunca python3 alguma_pasta/juiz.py, etc)

    Programa feito para rodar em ambiente linux, mas também funciona em WSL.

    Autoria: Natã Schmitt
    30/10/2022
'''


from datetime import datetime as dt
import subprocess
import os


PROGRAM = './PROGRAMA_A_SER_TESTADO' # nome do binário, pode ser usado python também

PROBLEM_LETTER = 'F' # letra da questão



class cor:
    B = '\033[94m'
    G = '\033[92m'
    R = '\033[91m'
    END = '\033[0m'

for pth,_,files in os.walk(f'./{PROBLEM_LETTER}/input'):
    files = sorted(files)
    for f in sorted(files, key=len):

        s = dt.now()
        subprocess.check_output(f'cat {pth}/{f} | {PROGRAM} > out', shell=True,text=True)
        e = dt.now()

        try:
            res = subprocess.check_output(f'diff out ./{PROBLEM_LETTER}/output/{f}', shell=True,text=True)
        except Exception as e:
            res = e.output


        if len(res) == 0:
            print(f'{cor.G}TEST CASE #{f[2:]} OK! took {(e-s).total_seconds():.4f}s\n{cor.END}')
        else:
            print(f'{cor.R}TEST CASE #{f[2:]} `cat {pth}/{f} | {PROGRAM} > out` ERROR!!!!{cor.END}')
            print(res)
            exit(1)
