import json
import os

def cadastrar():
    data_arr = []
    print('Cadastrar\n\n')
    if os.path.isfile('./data_disciplina.json'):
        with open('data_disciplina.json', 'r', encoding='utf-8') as f:
            my_data = json.load(f)
            data_arr = my_data
            
    
    data_raw = {}
    cad = True
    while cad:
        codigo_da_dscipina = int(input("Codigo da disciplina\n"))
        nome_da_dscipina = input("Nome da disciplina:\n")


        data_raw.update({
            'Codigo da disciplina':codigo_da_dscipina,
            'Nome da disciplina':nome_da_dscipina,
            
            })
        data_arr.append(data_raw)
        with open ('data_disciplina.json', "w") as f:
            json.dump(data_arr, f)
            print('Cadastro efetuado')
        cad = False

def visualizar():
    if os.path.isfile('./data_prof.json') == False:
        print('Nada cadastrado')
    else:
        print('Visualizar\n\n')

        with open('data_disciplina.json', 'r', encoding='utf-8') as f:
            my_data = json.load(f)
            print(my_data)


def editar():
    print('Editar')
    if os.path.isfile('./data_prof.json') == False:
        print('Nada cadastrado')
    else:
        data = []
        if os.path.isfile('./data_disciplina.json'):
            with open('data_disciplina.json', 'r', encoding='utf-8') as f:
                my_data = json.load(f)
                data_arr = my_data
                data = my_data
        print(my_data)
        op = int(input("Digite codigo da discipina: \n\n"))
        
        for i in range(len(my_data)):
            if my_data[i]['Codigo da disciplina'] == op:
                print(my_data[i])
                del my_data[i]
                print(my_data)
                with open ('data_disciplina.json', "w") as f:
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
        if os.path.isfile('./data_disciplina.json'):
            with open('data_disciplina.json', 'r', encoding='utf-8') as f:
                my_data = json.load(f)
                data_arr = my_data
                data = my_data
        print(my_data)
        op = int(input("Digite codigo da disciplina: \n\n"))
        
        for i in range(len(my_data)):
            if my_data[i]['Codigo da disciplina'] == op:
                print(my_data[i])
                del my_data[i]
                print(my_data)
                with open ('data_disciplina.json', "w") as f:
                    json.dump(my_data, f)
                    print('Cadastro Apagado')
                    break