from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/todo_db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Task {self.id}>'

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    output = []
    for task in tasks:
        task_data = {'id': task.id, 'content': task.content}
        output.append(task_data)
    return jsonify({'tasks': output})

@app.route('/tasks', methods=['POST'])
def add_task():
    task_content = request.json['content']
    new_task = Task(content=task_content)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
