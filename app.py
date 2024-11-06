from flask import Flask, request, jsonify
from google.cloud import firestore

app = Flask(__name__)
db = firestore.Client()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = [task.to_dict() for task in db.collection('tasks').stream()]
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task_data = request.json
    db.collection('tasks').add(task_data)
    return jsonify({'status': 'Task added successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
