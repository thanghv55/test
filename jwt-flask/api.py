from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hoangthangts'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)


@app.route('/users', methods=['GET'])
def get_all_users():
    return ''


@app.route('/user/<user_id>', methods=['GET'])
def get_one_users():
    return ''


@app.route('/user', methods=['POST'])
def creat_user():
    data = request.json
    hash_password = generate_password_hash(data['password'])
    new_user = User(public_id=uuid.uuid4(), name=data['name'], password=hash_password, admin=True)
    db.session.add(new_user)
    db.session.commit()
    return jsonify('Create new user sucessful!')


@app.route('/hello/<name>', methods=['GET'])
def hello_world(name):
    return jsonify("hello " + name)


if __name__ == '__main__':
    app.run(debug=True)
