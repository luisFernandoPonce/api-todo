from flask import Flask, jsonify, request
import json
app = Flask(__name__)
#logica de la aplicacion
todos= [
{ "label": "My first task", "done": False },
{ "label": "My second task", "done": False }
]


# los endpoints
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_todo=json.loads(request.data)
    #print("peticion recibida con el body", request_body)
    todos.append(request_todo)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if (position > len(todos)):
        return 'Posición no existe', 400
        if (position<0):
            return 'la posición no puede ser menor a cero', 400
            todos.remove(position)
            return jsonify(todos)


if  __name__=='__main__':
    app.run(host='0.0.0.0', port=3245,debug=True)