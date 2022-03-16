from flask import Flask, jsonify, request
from json import dump, load, JSONDecodeError
import os

from app.funcs.funcs import add_to_database, check_wrong_fields

app = Flask(__name__)
DATABASE_FILEPATH=os.getenv('DATABASE_FILEPATH')

@app.get('/user')
def get_database():
    try:
        with open(DATABASE_FILEPATH, 'r') as f:
            return jsonify(load(f)), 200
    except (FileNotFoundError, JSONDecodeError) as e:
        with open(DATABASE_FILEPATH, 'w') as f:
            dump([], f)
        with open(DATABASE_FILEPATH, 'r') as f:
            return jsonify(load(f)), 200            


@app.post('/user')
def akakak():
    data = request.get_json()

    if not check_wrong_fields(data):
        try:   
            with open(DATABASE_FILEPATH, 'r') as read_file:
                json_list = (load(read_file))
        except (FileNotFoundError, JSONDecodeError) as e:
            with open(DATABASE_FILEPATH, 'w') as f:
                dump([], f)
            with open(DATABASE_FILEPATH, 'r') as read_file:
                json_list = (load(read_file))
            
        if not add_to_database(json_list, data):
            return {'error': 'User already exists.'}, 409
    else:
        return {"wrong_fields": check_wrong_fields(data)}, 400


    with open(DATABASE_FILEPATH, 'w') as f:
        dump(json_list, f, indent=2)
        return {
            'data': data
        }, 201
        