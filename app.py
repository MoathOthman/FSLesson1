from flask import Flask, abort, render_template, request, redirect, url_for,jsonify
import sys
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/moath'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model): 
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'


db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body= {}
    try:
        description = request.get_json()['description'];
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body = {
            'description': todo.description
        }
    except:
        db.session.rollback()
        error=True
        print(sys.exc_info())
        abort()
    finally:
        db.session.close()
    if not error:
        return jsonify(body)
@app.route('/')
def index():
    return render_template('index.html', data= Todo.query.all())