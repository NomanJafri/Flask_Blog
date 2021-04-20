from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='bb955930a281a6e6e12a82c41f31770d'

posts = [
    {
        "author": "Noman Jafri",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2021"
    },
    {
        "author": "Hina Noman",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2021"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@flaskblog.com' and form.password.data == '123': #Dummy Data to see everything uptil now is working
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template("login.html", title="Login", form=form)

if __name__=="__main__":
    app.run(port=80, debug=True)