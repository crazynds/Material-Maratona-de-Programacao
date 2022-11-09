'''
    Este programa verifica se cada aluno solucionou determinados problemas no site BeeCrowd.

    Ele acessa o perfil de cada aluno contido no dicionario ids e verifica se os problemas
    contidos em p_list e bonusp_list foram resolvidos.

    p_list e bonusp_list => listas com os números dos problemas a serem verificados
    ids => dicionário onde as chaves são os ids para o perfil de cada aluno no BeeCrowd
        e os valores são dicionários com informações dos alunos.

    Autor: Eduardo Machado de Lima
    04/11/2022 
'''

from requests import get

p_list = [1001, 1005, 1010, 1018, 1021, 1037, 1047, 1216, 2091, 1124, 1232, 1087, 1129, 1140, 1912]
bonusp_list = [1086, 1032]

ids = {'732820' : {'name' : 'Eduardo Lima'},
       '417367' : {'name' : 'Fernando Pozzer'},
       '464560' : {'name' : 'Bento Borges Schirmer'},
       '722880' : {'name' : 'Luiz Henrique Lago'},
       '722844' : {'name' : 'Natã Ismael Schmitt'},
       '723759' : {'name' : 'Jonathan Nogueira'},
       '722914' : {'name' : 'Felipe Becker'},
       '724137' : {'name' : 'Luis Henrique Chesani'},
       '722836' : {'name' : 'Enzo Hahn Veroneze'},
       '722923' : {'name' : 'Matheus de Almeida'}}

headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
for idt in ids.keys():
    print('\n{}'.format(ids[idt]['name']))
    p = 1
    np = 1
    lines = []
    while p <= np:
        url = "https://www.beecrowd.com.br/judge/pt/profile/{}?page={}".format(idt,p)
        flag = False
        for line in get(url, headers=headers).content.decode().split('\n'):
            if line == '</tbody>':    
                flag = not flag
            if flag:
                lines.append(line)
            if line == '<tbody>':
                flag = not flag
            if len(line.split(' ')) == 3 and line.split(' ')[1] == 'of':
                np = int(line.split(' ')[2][:-6])
        p += 1
    
    dic = {}
    for i in range(len(lines)):
        if lines[i] == '<tr class="impar">' or lines[i] == '<tr class="par">':
            if lines[i+1] == '<td colspan="7"></td>':
                break
            dic[int(lines[i+2][55:59].replace('>', ''))] = {'name' : lines[i+4][55:].split('<')[0],
                                                            'pos' : int(lines[i+6][57:].split('&ordm')[0].replace('>', '')),
                                                            'lang' : lines[i+9][18:].split('<')[0],
                                                            'time' : float(lines[i+11].split(' <')[0]),
                                                            'date' : lines[i+13].split(' <')[0]}
    print('Realizados:', len(dic))
    for n in p_list:
        if n not in dic.keys():
            print(n, "faltando")
    for n in bonusp_list:
        if n in dic.keys():
            print('Bônus:', n, dic[n]['name'])
    ids[idt]['solved'] = dic