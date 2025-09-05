from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modèle Task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=True)
    priority = db.Column(db.String(20), default="Medium")  # Low, Medium, High
    completed = db.Column(db.Boolean, default=False)

# Crée la base au premier lancement
with app.app_context():
    db.create_all()

# Routes
@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    category = request.form.get("category")
    priority = request.form.get("priority")
    if title:
        new_task = Task(title=title, category=category, priority=priority)
        db.session.add(new_task)
        db.session.commit()
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect("/")

@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = not task.completed
        db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
