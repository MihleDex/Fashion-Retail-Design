from turtle import title
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html',title="Home")

@app.route('/about')
def about():
    return render_template('about.html',title="About")

@app.route('/women')
def women():
    return render_template('women.html',title="Women")

@app.route('/kids')
def kids():
    return render_template('kids.html',title="Kids")

@app.route('/accessories')
def accessories():
    return render_template('accessories.html',title="Accessories")

@app.route('/men')
def men():
    return render_template('men.html',title="Men")

@app.route('/sales')
def sales():
    return render_template('sales.html',title="Sales")

if __name__ == '__main__':
   app.run(debug=True)