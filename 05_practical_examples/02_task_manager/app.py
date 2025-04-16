from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
from models import User, Task, Comment
from database import Database
import hashlib

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # 실제 운영 환경에서는 안전한 키 사용
db = Database()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = db.get_user(session['user_id'])
    tasks = db.get_user_tasks(user.id)
    return render_template('index.html', user=user, tasks=tasks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hash_password(request.form['password'])
        user = db.get_user_by_username(username)
        if user and user.password == password:
            session['user_id'] = user.id
            flash('로그인 성공!', 'success')
            return redirect(url_for('index'))
        flash('아이디 또는 비밀번호가 올바르지 않습니다.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = hash_password(request.form['password'])
        if db.get_user_by_username(username):
            flash('이미 존재하는 사용자 이름입니다.', 'danger')
            return redirect(url_for('register'))
        user = User(
            id=None,
            username=username,
            email=email,
            password=password
        )
        db.add_user(user)
        flash('회원가입이 완료되었습니다. 로그인해주세요.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('로그아웃되었습니다.', 'success')
    return redirect(url_for('login'))

@app.route('/tasks/new', methods=['GET', 'POST'])
def new_task():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        task = Task(
            id=None,
            title=request.form['title'],
            description=request.form['description'],
            status='todo',
            priority=request.form['priority'],
            due_date=datetime.fromisoformat(request.form['due_date']),
            user_id=session['user_id']
        )
        db.add_task(task)
        flash('작업이 추가되었습니다.', 'success')
        return redirect(url_for('index'))
    return render_template('task_form.html')

@app.route('/tasks/<task_id>')
def task_detail(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    task = db.get_task(task_id)
    if not task or task.user_id != session['user_id']:
        flash('작업을 찾을 수 없습니다.', 'danger')
        return redirect(url_for('index'))
    comments = db.get_task_comments(task_id)
    return render_template('task_detail.html', task=task, comments=comments)

@app.route('/tasks/<task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    task = db.get_task(task_id)
    if not task or task.user_id != session['user_id']:
        flash('작업을 찾을 수 없습니다.', 'danger')
        return redirect(url_for('index'))
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.status = request.form['status']
        task.priority = request.form['priority']
        task.due_date = datetime.fromisoformat(request.form['due_date'])
        db.update_task(task)
        flash('작업이 수정되었습니다.', 'success')
        return redirect(url_for('task_detail', task_id=task_id))
    return render_template('task_form.html', task=task)

@app.route('/tasks/<task_id>/delete', methods=['POST'])
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    task = db.get_task(task_id)
    if not task or task.user_id != session['user_id']:
        flash('작업을 찾을 수 없습니다.', 'danger')
        return redirect(url_for('index'))
    db.delete_task(task_id)
    flash('작업이 삭제되었습니다.', 'success')
    return redirect(url_for('index'))

@app.route('/tasks/<task_id>/comments', methods=['POST'])
def add_comment(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    task = db.get_task(task_id)
    if not task or task.user_id != session['user_id']:
        flash('작업을 찾을 수 없습니다.', 'danger')
        return redirect(url_for('index'))
    comment = Comment(
        id=None,
        content=request.form['content'],
        task_id=task_id,
        user_id=session['user_id']
    )
    db.add_comment(comment)
    flash('댓글이 추가되었습니다.', 'success')
    return redirect(url_for('task_detail', task_id=task_id))

@app.route('/tasks/<task_id>/comments/<comment_id>/delete', methods=['POST'])
def delete_comment(task_id, comment_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    comment = db.get_task_comments(task_id)
    if not comment or comment.user_id != session['user_id']:
        flash('댓글을 찾을 수 없습니다.', 'danger')
        return redirect(url_for('index'))
    db.delete_comment(comment_id)
    flash('댓글이 삭제되었습니다.', 'success')
    return redirect(url_for('task_detail', task_id=task_id))

if __name__ == '__main__':
    app.run(debug=True) 