import json
import os

def cadastrar():
    data_arr = []
    print('Cadastrar\n\n')
    if os.path.isfile('./data_turmas.json'):
        with open('data_turmas.json', 'r', encoding='utf-8') as f:
            my_data = json.load(f)
            data_arr = my_data
            
    
    data_raw = {}
    cad = True
    while cad:
        codigo_da_dscipina = int(input("Codigo da turma\n"))
        codigo_do_professor = int(input("Codigo do professor:\n"))
        codigo_da_dscipina = int(input("Codigo da disciplina:\n"))

        data_raw.update({
            'Codigo da turma':codigo_da_dscipina,
            'Codigo do professor':codigo_do_professor,
            'Codigo da disciplina':codigo_da_dscipina
            })
        data_arr.append(data_raw)
        with open ('data_turmas.json', "w") as f:
            json.dump(data_arr, f)
            print('Cadastro efetuado')
        cad = False

def visualizar():
    if os.path.isfile('./data_prof.json') == False:
        print('Nada cadastrado')
    else:
        print('Visualizar\n\n')

        with open('data_turmas.json', 'r', encoding='utf-8') as f:
            my_data = json.load(f)
            print(my_data)


def editar():
    if os.path.isfile('./data_prof.json') == False:
        print('Nada cadastrado')
    else:
        print('Editar')
        data = []
        if os.path.isfile('./data_turmas.json'):
            with open('data_turmas.json', 'r', encoding='utf-8') as f:
                my_data = json.load(f)
                data_arr = my_data
                data = my_data
        print(my_data)
        op = int(input("Digite codigo da Turma: \n\n"))
        
        for i in range(len(my_data)):
            if my_data[i]['Codigo da turma'] == op:
                print(my_data[i])
                del my_data[i]
                print(my_data)
                with open ('data_turmas.json', "w") as f:
                    json.dump(my_data, f)
                print('Atualizar cadastro:\n')
                cadastrar()
                break

def apagar():
    print('Apagar Cadastro')
    if os.path.isfile('./data_prof.json') == False:
        print('Nada cadastrado')
    else:
        data = []
        if os.path.isfile('./data_turmas.json'):
            with open('data_turmas.json', 'r', encoding='utf-8') as f:
                my_data = json.load(f)
                data_arr = my_data
                data = my_data
        print(my_data)
        op = int(input("Digite codigo da turma: \n\n"))
        
        for i in range(len(my_data)):
            if my_data[i]['Codigo da turma'] == op:
                print(my_data[i])
                del my_data[i]
                print(my_data)
                with open ('data_turma.json', "w") as f:
                    json.dump(my_data, f)
                    print('Cadastro Apagado')
                    break