import json
import os
def cadastrar():
    data_arr = []
    print('Cadastrar\n\n')
    if os.path.isfile('./data_prof.json'):
        with open('data_prof.json', 'r', encoding='utf-8') as f:
            my_data = json.load(f)
            data_arr = my_data
            
    
    data_raw = {}
    cad = True
    while cad:
        codigo_do_professor = int(input("Codigo do professor\n"))
        nome_do_professor = input("Nome do professor\n")
        CPF_do_professor = input("CPF do professor\n")

        data_raw.update({
            'Codigo do professor':codigo_do_professor,
            'Nome do professor':nome_do_professor,
            'CPF do professor':CPF_do_professor
            })
        data_arr.append(data_raw)
        with open ('data_prof.json', "w") as f:
            json.dump(data_arr, f)
            print('Cadastro efetuado')
        cad = False

def visualizar():
    print('Visualizar\n\n')
    if os.path.isfile('./data_prof.json') == False:
        print('Nada cadastrado')
    else:
        with open('data_prof.json', 'r', encoding='utf-8') as f:
            my_data = json.load(f)
            print(my_data)


def editar():
    print('Editar')
    if os.path.isfile('./data_prof.json') == False:
        print('Nada cadastrado')
    else:
        data = []
        if os.path.isfile('./data_prof.json'):
            with open('data_prof.json', 'r', encoding='utf-8') as f:
                my_data = json.load(f)
                data_arr = my_data
                data = my_data
        print(my_data)
        op = int(input("Digite codigo do professor: \n\n"))
        
        for i in range(len(my_data)):
            if my_data[i]['Codigo do professor'] == op:
                print(my_data[i])
                del my_data[i]
                print(my_data)
                with open ('data_prof.json', "w") as f:
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
        if os.path.isfile('./data_prof.json'):
            with open('data_prof.json', 'r', encoding='utf-8') as f:
                my_data = json.load(f)
                data_arr = my_data
                data = my_data
        print(my_data)
        op = int(input("Digite codigo do professor: \n\n"))
        
        for i in range(len(my_data)):
            if my_data[i]['Codigo do professor'] == op:
                print(my_data[i])
                del my_data[i]
                print(my_data)
                with open ('data_prof.json', "w") as f:
                    json.dump(my_data, f)
                    print('Cadastro Apagado')
                    break