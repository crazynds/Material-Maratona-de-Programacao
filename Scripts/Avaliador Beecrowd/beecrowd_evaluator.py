'''
    Este programa verifica se cada aluno solucionou determinados problemas no site BeeCrowd.

    Ele acessa o perfil de cada aluno contido no dicionario ids e verifica se os problemas
    contidos em p_list e bonusp_list foram resolvidos.

    p_list e bonusp_list => listas com os números dos problemas a serem verificados
    ids => dicionário onde as chaves são os ids para o perfil de cada aluno no BeeCrowd
        e os valores são dicionários com informações dos alunos.

    Autor: Eduardo Machado de Lima
    
    Contribuidores: 
     - Luiz Henrique B Lago
     
'''

import yaml
import re
import multiprocessing
from tqdm.contrib.concurrent import thread_map
from requests import get
import pandas as pd



config = yaml.safe_load(open("config.yml",encoding='utf8'))
headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

EX_LISTS = config['lists']

p_list = EX_LISTS['problems']
bonusp_list = EX_LISTS['bonus']

num_cores = multiprocessing.cpu_count()


users = config['users']
problems = {}

def updateProblemsUser(user):
    name = user['name']
    id = user['id']
    p = 1
    np = 1
    lines = []
    numberReg = re.compile('<a href="/judge/pt/problems/view/([0-9]+)"')
    while p <= np:
        url = f"https://www.beecrowd.com.br/judge/pt/profile/{id}?page={p}"
        flag = False
        for line in get(url, headers=headers).content.decode().split('\n'):
            if line == '</tbody>':    
                flag = False
            elif line == '<tbody>':
                flag = True
            elif flag:
                lines.append(line)

            if len(line.split(' ')) == 3 and line.split(' ')[1] == 'of':
                np = int(line.split(' ')[2][:-6])
        p += 1
    dic = {}
    for i in range(len(lines)):
        if lines[i] == '<tr class="impar">' or lines[i] == '<tr class="par">':
            if lines[i+1] == '<td colspan="7"></td>':
                break            
            number = int(numberReg.search(lines[i+2]).group(1))            
            dic[number] = { 
                'name' : lines[i+4][55:].split('<')[0],
                'pos' : int(lines[i+6][57:].split('&ordm')[0].replace('>', '')),
                'lang' : lines[i+9][18:].split('<')[0],
                'time' : float(lines[i+11].split(' <')[0]),
                'date' : lines[i+13].split(' <')[0],
                'code' : number 
            }

    user['solved'] = dic
    return user


def updateProblemStats(problem):
    key = problem['code']
    levelReg = re.compile("Nível ([0-9]+) \/ 10")
    typeReg = re.compile("\/judge\/pt\/problems\/index\/([0-9]+)")
    url = f"https://www.beecrowd.com.br/judge/pt/questions/index/{problem['code']}"
    types= ['Iniciante', 'Ad-Hoc', 'Strings', 'Estrutura e Bibliotecas', 'Matemática', 'Paradigmas', 'Grafos', 'Geometria Computacional', 'SQL']
    for line in get(url, headers=headers).content.decode().split('\n'):
        level = levelReg.search(line)
        if level:
            problem['level'] = level.group(1)
        type = typeReg.search(line)
        if type:
            problem['type'] = type.group(1)
            problem['type'] = types[int(problem['type'])-1]
    return problem


def generateExcelOutput(users):
    header = ["Dev","Data","Nome","Tipo","Nivel"]
    rows = []
    for user in users:
        for code in user['solved']:
            problemData = problems[code]
            try:
                rows.append([
                    user['name'],
                    user['solved'][code]['date'].strip(),
                    problemData['name'] +f' ({code})',
                    problemData['type'],
                    problemData['level'],
                ])
            except KeyError as e:
                print('Problema com dados não encontrados')
                print(problemData['name']+ " - "+ str(code))
                print(str(e))
    df = pd.DataFrame(rows,columns=header)
    df['Data'] = pd.to_datetime(df['Data'],format="%d/%m/%Y %H:%M:%S")
    df = df.sort_values(by = ['Data'])
    df = df.reset_index(drop=True)
    df.to_csv('relatorio.csv')


print('Carregando dados de usuários')
users = thread_map(updateProblemsUser,users,max_workers=num_cores)

for user in users:
    for number in user['solved']:
        if number not in problems:
            problems[number] = {
                'name': user['solved'][number]['name'],
                'code': number
            }


print('Carregando dados dos problemas')
problems = thread_map(updateProblemStats,[problems[key] for key in problems],max_workers=num_cores)
problems = dict((x['code'],x) for x in problems)

for user in users:
    name = user['name']
    print(f'{name}')
    dic = user['solved']
    
    print('Realizados:', len(dic))
    for n in p_list:
        if n not in dic.keys():
            print(n, "faltando")
    for n in bonusp_list:
        if n in dic.keys():
            print('Bônus:', n, dic[n]['name'])
    print()

generateExcelOutput(users)