from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import hashlib
from models import User, Post, Comment
from database import Database

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 실제 운영 환경에서는 안전한 키로 변경해야 합니다.

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = Database('blog.db')

@login_manager.user_loader
def load_user(user_id):
    return db.get_user(int(user_id))

def hash_password(password):
    return generate_password_hash(password)

def verify_password(password, hashed_password):
    return check_password_hash(hashed_password, password)

@app.route('/')
def index():
    posts = db.get_user_posts(current_user.id) if current_user.is_authenticated else []
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.get_user_by_username(username)
        
        if user and verify_password(password, user.password):
            login_user(user)
            flash('로그인 성공!', 'success')
            return redirect(url_for('index'))
        else:
            flash('아이디 또는 비밀번호가 올바르지 않습니다.', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if db.get_user_by_username(username):
            flash('이미 존재하는 사용자 이름입니다.', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = hash_password(password)
        user = User(None, username, email, hashed_password)
        db.add_user(user)
        
        flash('회원가입이 완료되었습니다. 로그인해주세요.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('로그아웃되었습니다.', 'success')
    return redirect(url_for('index'))

@app.route('/posts/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(None, title, content, current_user.id)
        db.add_post(post)
        flash('게시글이 작성되었습니다.', 'success')
        return redirect(url_for('index'))
    
    return render_template('post_form.html')

@app.route('/posts/<int:post_id>')
def view_post(post_id):
    post = db.get_post(post_id)
    if not post:
        flash('게시글을 찾을 수 없습니다.', 'danger')
        return redirect(url_for('index'))
    
    comments = db.get_post_comments(post_id)
    return render_template('post.html', post=post, comments=comments)

@app.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = db.get_post(post_id)
    if not post or post.user_id != current_user.id:
        flash('권한이 없습니다.', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        if db.update_post(post):
            flash('게시글이 수정되었습니다.', 'success')
            return redirect(url_for('view_post', post_id=post_id))
        else:
            flash('게시글 수정에 실패했습니다.', 'danger')
    
    return render_template('post_form.html', post=post)

@app.route('/posts/<int:post_id>/delete')
@login_required
def delete_post(post_id):
    post = db.get_post(post_id)
    if not post or post.user_id != current_user.id:
        flash('권한이 없습니다.', 'danger')
        return redirect(url_for('index'))
    
    if db.delete_post(post_id):
        flash('게시글이 삭제되었습니다.', 'success')
    else:
        flash('게시글 삭제에 실패했습니다.', 'danger')
    
    return redirect(url_for('index'))

@app.route('/posts/<int:post_id>/comments', methods=['POST'])
@login_required
def add_comment(post_id):
    content = request.form['content']
    comment = Comment(None, content, post_id, current_user.id)
    db.add_comment(comment)
    flash('댓글이 작성되었습니다.', 'success')
    return redirect(url_for('view_post', post_id=post_id))

@app.route('/posts/<int:post_id>/comments/<int:comment_id>/delete')
@login_required
def delete_comment(post_id, comment_id):
    comment = db.get_post_comments(post_id)
    if not comment or comment.user_id != current_user.id:
        flash('권한이 없습니다.', 'danger')
        return redirect(url_for('view_post', post_id=post_id))
    
    if db.delete_comment(comment_id):
        flash('댓글이 삭제되었습니다.', 'success')
    else:
        flash('댓글 삭제에 실패했습니다.', 'danger')
    
    return redirect(url_for('view_post', post_id=post_id))

if __name__ == '__main__':
    app.run(debug=True) 