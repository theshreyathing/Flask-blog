from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app =  Flask(__name__, template_folder='template')

app.config['SECRET_KEY'] = '1e8d826441423a20ed244252708dc3f4'  #Adding secret key to sheild from certain attacks

posts = [
    {
        'author': 'Person 1',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 7, 2023'
    },
    {
        
        'author': 'Person 2',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 8, 2023'
    
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About' )

@app.route("/register", methods =['GET', 'POST']) 
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','Success')
        return redirect(url_for('home'))
    return render_template('register.html',title= 'Register', form =form)

@app.route("/login")   #route name
def login(): #route function
    form = LoginForm()
    return render_template('login.html',title= 'Login', form =form)

if __name__ == '__main__':
    app.run(debug=True)