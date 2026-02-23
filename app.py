print("STARTING APP...")

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return render_template("index.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        students.append({
            "name": name,
            "age": age,
            "course": course
        })

        return redirect("/")

    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete_student(id):
    if id < len(students):
        students.pop(id)
    return redirect("/")

if __name__ == "__main__":
    print("RUNNING SERVER...")
    app.run(debug=True)