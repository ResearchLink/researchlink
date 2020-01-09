# encoding=utf-8

from flask import request, Blueprint, render_template, redirect, url_for, jsonify, current_app as app
from flask_login import login_required, current_user
from flaskweb.app import db
from auth.views import check_user_login
from .models import SurveyInfo
from .forms import SurveyForm
import os

basedir = os.path.dirname(__file__)
bp = Blueprint('main', __name__,
               static_url_path="/static",
               static_folder=os.path.join(basedir, "../static"),
               template_folder=os.path.join(basedir, "../templates"))


@bp.route('/', methods=['GET', 'POST'])
def index():
    # post
    form = SurveyForm()
    if form.validate_on_submit():
        email = form.email.data
        # sent to database
        app.logger.info(email)
        survey = SurveyInfo(email=form.email.data,
                            interests=form.interests.data, year=form.year.data)
        db.session.add(survey)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('debug.html', form=form)

# @bp.route('/user')
# @login_required
# def user():
#     return 'hello world %s' % current_user.username


# @bp.route("/api/login", methods=["POST"])
# def login():
#     # rewrite login api
#     data = request.get_json()
#     username = data.get("username")
#     password = data.get("password")
#     if check_user_login(username, password):
#         return redirect(url_for("index"))
#     else:
#         return "login error", 400


# @login_required
# @bp.route('/upload', methods=["POST"])
# def upload():
#     fs = request.files['file']
#     upload_dir = app.config["UPLOAD_DIR"]
#     if not os.path.exists(upload_dir):
#         os.makedirs(upload_dir)
#     filepath = os.path.join(upload_dir, fs.filename)
#     app.logger.info("saving %s to %s" % (fs, filepath))
#     fs.save(filepath)
#     return jsonify({"result": "ok"})
