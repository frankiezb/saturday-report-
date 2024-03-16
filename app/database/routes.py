from flask import (
    Flask,
    render_template,
    request
)
import requests

BACKEND_URL = "http://127.0.0.1:5000/task"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/tasks")
def task_list():
    response = requests.get(BACKEND_URL)
    if response.status_code == 200:
        tasks_list = response.json().get("tasks")
        return render_template("list.html", tasks_list=tasks_list)
    else:
        return (
            render_template("error.html", err=response.status_code),
            response.status_code
        )

if __name__ == "__main__":
    app.run(port=5001, debug=True)
