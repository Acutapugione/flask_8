from flask import render_template, request, url_for, redirect
from app import app, db
from .models import Students, Lessons

# self-migration
# with app.app_context() as s:
#     db.drop_all()
#     db.create_all()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/students/')
def students():
    students = Students.query.limit(25).all()

    return render_template('list.html', items = students)

@app.route('/students/create/', methods = ('GET', 'POST'))
def student_create():
    if request.method == 'POST':
        #filling params
        name = request.form['name']
        lesson_id = request.form['lesson_id']
                
        #create instance
        stud = Students(
            name = name,
            lesson_id = lesson_id
        )
        
        #add to session db
        db.session.add(stud)
        
        #db commiting ( apply changes )
        db.session.commit()

        return redirect(url_for('students'))

    return render_template('create_student.html')


@app.route('/lessons/')
def lessons():
    lessons = Lessons.query.limit(25).all()

    return render_template('list.html', items = lessons, handlers = ( lesson_edit, ))

@app.route('/students/<int:id>/')
def student_info(id):
    student = Students.query.get_or_404(id)
    
    return student.name


@app.route('/lessons/<int:id>/edit', methods = ('GET', 'POST'))
def lesson_edit(id):
    lesson = Lessons.query.get_or_404(id)
    # students = Students.query.limit(25).all()
    
    if request.method == 'POST':
        name = request.form['name']
        teacher = request.form['teacher']

        lesson.name = name
        lesson.teacher = teacher
    
        db.session.add(lesson)

        db.session.commit()
        return redirect(url_for('lessons'))
        
    return render_template('edit_lesson.html', lesson = lesson, count = len(lesson.students))

@app.route('/lessons/create/', methods = ('GET', 'POST'))
def lesson_create():
    if request.method == 'POST':
        name = request.form['name']
        teacher = request.form['teacher']

        lesson = Lessons(
            name = name,
            teacher = teacher,
        )
        
        db.session.add(lesson)

        db.session.commit()
        return redirect(url_for('lessons'))
        
    return render_template('create_lesson.html')
