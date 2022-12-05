#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """when request route "/" displays “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """generic comment"""
    return "HBNB"


@app.route("/c/<txt>", strict_slashes=False)
def c_(txt):
    """generic comment"""
    txt = txt.replace("_", " ")
    return "C {}".format(txt)


@app.route("/python", strict_slashes=False)
@app.route("/python/<txt>", strict_slashes=False)
def python_(txt="is cool"):
    """generic comment"""
    txt = txt.replace("_", " ")
    return "Python {}".format(txt)


@app.route("/number/<int:my_num>", strict_slashes=False)
def number(my_num):
    """generic comment"""
    return "{} is a number".format(my_num)


@app.route("/number_template/<int:my_num>", strict_slashes=False)
def my_number(my_num):
    """generic comment"""
    return render_template('5-number.html', num=my_num)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """generic comment"""
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)