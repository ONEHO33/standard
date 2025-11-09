"""
@author gye hyun james kim <pnuskgh@gmail.com>
@copyright 2017~2025, BlueStone Inc.
@license BlueStone License 1.0
"""

from flask import Flask, render_template, request
from mainFastAPI import getLogger, init_env

app = Flask(__name__)

init_env()
logger = getLogger("app/mainFlask")


@app.route("/")
def hello_world():
    # return "Hello World"
    # --- Jinja2 템플릿
    return render_template("flaskTemplate.html", name="James")


@app.route("/result", methods=["POST"])
def result():
    names = request.form.getlist("name[]")
    student_numbers = request.form.getlist("StudentNumber[]")

    return render_template("app_result.html", students=zip(names, student_numbers))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)
