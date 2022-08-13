from flask import Flask, jsonify, request, json
app = Flask(__name__)


todos = [{ "label": "Sample Todo 0", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    todosjson = jsonify(todos)
    return todosjson

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json #transforma de JSON a Python
    todos.append(request_body)
    print("Incoming request with the following body", todos)
    return jsonify(todos) 
    #Jsonify transforma a Json desde Python

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)