from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import date
from models import Class, Student, Grade, Attendance
from database import Database

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # 실제 운영 환경에서는 보안을 위해 변경해야 합니다

db = Database()

# 학급 관련 라우트
@app.route('/')
def class_list():
    classes = db.get_all_classes()
    return render_template('class_list.html', classes=classes)

@app.route('/classes/add', methods=['GET', 'POST'])
def add_class():
    if request.method == 'POST':
        class_ = Class(
            name=request.form['name'],
            grade=int(request.form['grade']),
            teacher=request.form['teacher'],
            room_number=request.form['room_number']
        )
        db.add_class(class_)
        flash('학급이 추가되었습니다.', 'success')
        return redirect(url_for('class_list'))
    return render_template('class_form.html')

@app.route('/classes/<int:class_id>')
def class_detail(class_id):
    class_ = db.get_class(class_id)
    students = db.get_students_by_class(class_id)
    return render_template('class_detail.html', class_=class_, students=students)

@app.route('/classes/<int:class_id>/edit', methods=['GET', 'POST'])
def edit_class(class_id):
    class_ = db.get_class(class_id)
    if request.method == 'POST':
        class_.name = request.form['name']
        class_.grade = int(request.form['grade'])
        class_.teacher = request.form['teacher']
        class_.room_number = request.form['room_number']
        db.update_class(class_)
        flash('학급 정보가 수정되었습니다.', 'success')
        return redirect(url_for('class_detail', class_id=class_id))
    return render_template('class_form.html', class_=class_)

# 학생 관련 라우트
@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student = Student(
            name=request.form['name'],
            student_id=request.form['student_id'],
            birth_date=date.fromisoformat(request.form['birth_date']),
            class_id=int(request.form['class_id']),
            phone=request.form['phone'],
            address=request.form['address']
        )
        db.add_student(student)
        flash('학생이 추가되었습니다.', 'success')
        return redirect(url_for('class_detail', class_id=student.class_id))
    
    classes = db.get_all_classes()
    return render_template('student_form.html', classes=classes)

@app.route('/students/<int:student_id>')
def student_detail(student_id):
    student = db.get_student(student_id)
    class_ = db.get_class(student.class_id)
    grades = db.get_student_grades(student_id)
    attendances = db.get_student_attendance(student_id)
    return render_template('student_detail.html', 
                         student=student, 
                         class_=class_,
                         grades=grades,
                         attendances=attendances)

@app.route('/students/<int:student_id>/edit', methods=['GET', 'POST'])
def edit_student(student_id):
    student = db.get_student(student_id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.student_id = request.form['student_id']
        student.birth_date = date.fromisoformat(request.form['birth_date'])
        student.class_id = int(request.form['class_id'])
        student.phone = request.form['phone']
        student.address = request.form['address']
        db.update_student(student)
        flash('학생 정보가 수정되었습니다.', 'success')
        return redirect(url_for('student_detail', student_id=student_id))
    
    classes = db.get_all_classes()
    return render_template('student_form.html', student=student, classes=classes)

# 성적 관련 라우트
@app.route('/grades/add', methods=['GET', 'POST'])
def add_grade():
    student_id = request.args.get('student_id')
    if not student_id:
        flash('학생 정보가 필요합니다.', 'error')
        return redirect(url_for('class_list'))
    
    student = db.get_student(int(student_id))
    if request.method == 'POST':
        grade = Grade(
            student_id=student.id,
            subject=request.form['subject'],
            score=float(request.form['score']),
            semester=int(request.form['semester']),
            exam_date=date.fromisoformat(request.form['exam_date'])
        )
        db.add_grade(grade)
        flash('성적이 추가되었습니다.', 'success')
        return redirect(url_for('student_detail', student_id=student_id))
    
    return render_template('grade_form.html', student=student)

@app.route('/grades/<int:grade_id>/edit', methods=['GET', 'POST'])
def edit_grade(grade_id):
    grade = db.get_grade(grade_id)
    student = db.get_student(grade.student_id)
    
    if request.method == 'POST':
        grade.subject = request.form['subject']
        grade.score = float(request.form['score'])
        grade.semester = int(request.form['semester'])
        grade.exam_date = date.fromisoformat(request.form['exam_date'])
        db.update_grade(grade)
        flash('성적이 수정되었습니다.', 'success')
        return redirect(url_for('student_detail', student_id=student.id))
    
    return render_template('grade_form.html', grade=grade, student=student)

@app.route('/classes/<int:class_id>/grades')
def class_grades(class_id):
    class_ = db.get_class(class_id)
    semester = request.args.get('semester', type=int)
    subject = request.args.get('subject')
    
    grades = db.get_class_grades(class_id, semester, subject)
    subjects = db.get_class_subjects(class_id)
    
    # 성적 통계 계산
    scores = [grade.score for grade in grades]
    avg_score = sum(scores) / len(scores) if scores else 0
    max_score = max(scores) if scores else 0
    min_score = min(scores) if scores else 0
    std_dev = (sum((x - avg_score) ** 2 for x in scores) / len(scores)) ** 0.5 if scores else 0
    
    return render_template('class_grades.html',
                         class_=class_,
                         grades=grades,
                         subjects=subjects,
                         avg_score=avg_score,
                         max_score=max_score,
                         min_score=min_score,
                         std_dev=std_dev)

# 출석 관련 라우트
@app.route('/attendance/add', methods=['GET', 'POST'])
def add_attendance():
    student_id = request.args.get('student_id')
    class_id = request.args.get('class_id')
    date_str = request.args.get('date')
    
    if not student_id and not class_id:
        flash('학생 또는 학급 정보가 필요합니다.', 'error')
        return redirect(url_for('class_list'))
    
    if request.method == 'POST':
        if student_id:  # 개별 출석 추가
            attendance = Attendance(
                student_id=int(student_id),
                date=date.fromisoformat(request.form['date']),
                status=request.form['status'],
                reason=request.form.get('reason')
            )
            db.add_attendance(attendance)
            flash('출석 정보가 추가되었습니다.', 'success')
            return redirect(url_for('student_detail', student_id=student_id))
        else:  # 일괄 출석 추가
            students = db.get_students_by_class(int(class_id))
            for student in students:
                attendance = Attendance(
                    student_id=student.id,
                    date=date.fromisoformat(request.form['date']),
                    status=request.form['status'],
                    reason=request.form.get('reason')
                )
                db.add_attendance(attendance)
            flash('일괄 출석 정보가 추가되었습니다.', 'success')
            return redirect(url_for('class_attendance', class_id=class_id, date=date_str))
    
    if student_id:
        student = db.get_student(int(student_id))
        return render_template('attendance_form.html', student=student)
    else:
        class_ = db.get_class(int(class_id))
        return render_template('attendance_form.html', class_=class_)

@app.route('/attendance/<int:attendance_id>/edit', methods=['GET', 'POST'])
def edit_attendance(attendance_id):
    attendance = db.get_attendance(attendance_id)
    student = db.get_student(attendance.student_id)
    
    if request.method == 'POST':
        attendance.date = date.fromisoformat(request.form['date'])
        attendance.status = request.form['status']
        attendance.reason = request.form.get('reason')
        db.update_attendance(attendance)
        flash('출석 정보가 수정되었습니다.', 'success')
        return redirect(url_for('student_detail', student_id=student.id))
    
    return render_template('attendance_form.html', attendance=attendance, student=student)

@app.route('/classes/<int:class_id>/attendance')
def class_attendance(class_id):
    class_ = db.get_class(class_id)
    date_str = request.args.get('date', date.today().isoformat())
    attendances = db.get_class_attendance(class_id, date.fromisoformat(date_str))
    
    # 출석 통계 계산
    attendance_stats = {
        '출석': sum(1 for a in attendances if a.status == '출석'),
        '지각': sum(1 for a in attendances if a.status == '지각'),
        '조퇴': sum(1 for a in attendances if a.status == '조퇴'),
        '결석': sum(1 for a in attendances if a.status == '결석')
    }
    
    return render_template('class_attendance.html',
                         class_=class_,
                         attendances=attendances,
                         attendance_stats=attendance_stats)

if __name__ == '__main__':
    app.run(debug=True) 