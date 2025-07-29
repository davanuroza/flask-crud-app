from flask import Flask, jsonify, request
from todo_manager import ToDoManager

app = Flask(__name__)
todo_manager = ToDoManager()

@app.route('/')
def home():
    return "API To-Do List dengan Flask + SQLite + OOP!"

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = todo_manager.get_all()
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    task = data.get('task')
    if not task:
        return jsonify({'message': 'Task tidak boleh kosong'}), 400
    todo_manager.add(task)
    return jsonify({'message': 'Tugas ditambahkan!', 'task': task})

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    new_task = data.get('task')
    if not new_task:
        return jsonify({'message': 'Task baru tidak boleh kosong'}), 400
    todo_manager.update(todo_id, new_task)
    return jsonify({'message': 'Tugas diperbarui!', 'id': todo_id, 'task': new_task})

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo_manager.delete(todo_id)
    return jsonify({'message': 'Tugas dihapus.', 'id': todo_id})

if __name__ == '__main__':
    app.run(debug=True)
