from turtle import title
from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fcc8cd976388abead7c7a207762cb7c5'

@app.route('/')
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

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('index'))
    return render_template('register.html',title="Register",form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("hey")
        if form.email.data == 'admin@site.com' and form.password.data == 'password':
            flash('Login Success!','success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful!','danger')
    return render_template('login.html',title="Login",form=form)

if __name__ == '__main__':
   app.run(debug=True)