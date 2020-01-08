# encoding=utf-8
from flask import request, Blueprint, render_template, redirect, url_for, jsonify, current_app as app
from flask_login import login_required, current_user
from flaskweb.app import db
from auth.views import check_user_login
from .models import Todo, TodoItem
import os

basedir = os.path.dirname(__file__)
modname = "debug"
bp = Blueprint(modname, modname, url_prefix="/debug",
               static_url_path="/static",
               static_folder=os.path.join(basedir, "../static"),
               template_folder=os.path.join(basedir, "../templates"))


@bp.route('/')
def index():
    return render_template('debug.html')


@bp.route('/user')
@login_required
def user():
    return 'hello world %s' % current_user.username


@bp.route("/api/login", methods=["POST"])
def login():
    # rewrite login api
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if check_user_login(username, password):
        return redirect(url_for(modname + ".index"))
    else:
        return "login error", 400


@login_required
@bp.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "GET":
        todos = Todo.query.all()
        todos = [i.to_dict() for i in todos]
        return jsonify(todos)
    else:
        todo = Todo.create(request.form['name'], current_user, request.form['tag'])
        db.session.add(todo)
        db.session.commit()
        return jsonify(todo.to_dict())


@login_required
@bp.route("/todo/<int:tid>", methods=["GET", "POST"])
def todo_item(tid):
    if request.method == "GET":
        todo = TodoItem.query.filter_by(tid=tid).all()
        res = [t.to_dict() for t in todo]
        return jsonify(res)
    else:
        task = request.form['task'].strip()
        todo = TodoItem.create(tid, task, current_user)
        db.session.add(todo)
        db.session.commit()
        return jsonify(todo.to_dict())


@login_required
@bp.route('/upload', methods=["POST"])
def upload():
    fs = request.files['file']
    upload_dir = app.config["UPLOAD_DIR"]
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    filepath = os.path.join(upload_dir, fs.filename)
    app.logger.info("saving %s to %s" % (fs, filepath))
    fs.save(filepath)
    return jsonify({"result": "ok"})
