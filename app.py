from flask import Flask, redirect, render_template

app = Flask(__name__)

app.route('/')
def index():
    return render_template('home.html')

@app.route('/error_500')
def error_500():
    x = 1 / 0
    return "This won't be reached"

if __name__ == '__main__':
    app.run(debug=True)