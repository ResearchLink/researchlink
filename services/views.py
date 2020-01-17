# encoding=utf-8

from flask import request, flash, Blueprint, render_template, redirect, url_for, jsonify, current_app as app
from flask_login import login_required, current_user
from flaskweb.app import db
from auth.views import check_user_login
from .models import SurveyInfo, Post, Application
from .forms import SurveyForm
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/wzq/document'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc'}

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
    return render_template('index.html', form=form)

# -------------- pricing ----------------------
@bp.route('/pricing', methods=['GET'])
def pricing():
    """
    This route shows the pricing page
    """
    return render_template('pricing.html')

# -------------- post ----------------------


@bp.route('/explore',  methods=['GET'])
# @login_required
def explore():
    """
    This route shows all posts
    """
    page = request.args.get('page', 1, type=int)
    # posts = Post.query.order_by(Post.timestamp.desc()).paginate(
    #     page, app.config['POSTS_PER_PAGE'], False)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, 6, False)
    next_url = url_for('main.explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('explore.html', title=('Explore'),
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)

# -------------- post ----------------------
@bp.route('/position_detail/<post_id>',  methods=['GET', 'POST'])
# @login_required
def position_detail(post_id):
    """
    This route shows position detail
    """
    # get post by post_id
    post = Post.query.filter_by(id=post_id).first_or_404()
    return render_template('post.html', post=post)



# -------------- login ----------------------


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

# -------------- upload ----------------------

# @login_required
@bp.route('/api/upload', methods=["POST"])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
    file = request.files['file']
    post_id = request.form.to_dict()['post_id']
    
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        resume_addr = os.path.join(UPLOAD_FOLDER, filename)
        file.save(resume_addr)
        app.logger.info('Resume saved to ' + resume_addr)
    
    # save each application to the db
    application = Application(post_id=post_id ,
                    resume_addr=resume_addr)
    db.session.add(application)
    db.session.commit()
    return jsonify({"code": 0, "fileName": "/api/download/" + filename})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
