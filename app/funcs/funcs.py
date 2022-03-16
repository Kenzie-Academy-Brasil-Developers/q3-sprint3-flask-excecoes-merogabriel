import json
from flask import jsonify

def add_to_database(json_list: list, payload: dict):
    nome = capitalize_name(payload['nome'])
    email = payload['email'].lower()

    if len(json_list) == False:
        id = 1
    else:
        id = json_list[-1]['id'] + 1

    payload['id'], payload['nome'], payload['email'] = id, nome, email
    
    if check_email(json_list, email):
        json_list.append(payload)
        return payload

    return False

def capitalize_name(nome: str):
    nomes = []
    for nome in nome.split():
        nomes.append(nome.capitalize())

    nomes = " ".join(nomes)

    return nomes

def check_email(json_list: list, email: str):
    for existing_email in json_list:
        if existing_email['email'] == email:
            return False

    return True

def check_wrong_fields(payload: dict):
    type_nome = type(payload['nome'])
    type_email = type(payload['email'])

    wrong_fields = []

    if type_nome != str:
        wrong_fields.append({})
        wrong_fields[-1]['nome'] = check_data_type(type_nome)
           
        
    if type_email != str:
        wrong_fields.append({})
        wrong_fields[-1]['email'] = check_data_type(type_email)

    return wrong_fields

def check_data_type(data):
    if data == int:
        return 'integer'
    elif data == bool:
        return 'bool'
    elif data == float:
        return 'float'
    elif data == dict:
        return 'dictionary'
    elif data == tuple:
        return 'tuple'
    elif data == list:
        return 'list'