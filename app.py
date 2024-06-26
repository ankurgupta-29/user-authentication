from flask import Flask, render_template, redirect, request, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ankurgupta29'
app.config['MYSQL_HOST'] = 'database-1.cdemiowkayx7.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'mysql1234'
app.config['MYSQL_DB'] = 'mysqldb'

mysql = MySQL(app)
login_manager=LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app) 


class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    cur=mysql.connection.cursor()
    cur.execute("SELECT id, email FROM user WHERE id=%s", (user_id,))
    user_data=cur.fetchone()
    cur.close()
    if user_data:
        user=User()
        user.id = user_data[0]
        user.email = user_data[1]
        return user
    return None



@app.route('/')
def homepage():
    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        email = request.form['email']
        name = request.form['name']
        lname = request.form['lname']
        password = request.form['password']
        cpassword = request.form['cpassword']
        if password != cpassword:
            flash('Passwords do not match', 'error')
            return redirect('/signup')
        cur = mysql.connection.cursor()
        cur.execute("SELECT email, password FROM user WHERE email=%s", (email,))
        user = cur.fetchone()
        if user:
            flash('Email already exists', 'error')
            cur.close()
            return redirect('/signup')
        cur.execute("INSERT INTO user (email, name, lname, password) VALUES (%s, %s, %s, %s)",
                    (email, name, lname, password))
        mysql.connection.commit()
        cur.close()
        flash('Signup successful', 'success')
        return redirect('/login')
    else:
        return render_template('signup.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, email, password FROM user WHERE email=%s", (email,))
        user_data = cur.fetchone()
        cur.close()
        if user_data and user_data[2] == password:
            user = User()
            user.id = user_data[0]
            login_user(user)
            flash('Login successful', 'success')
            
            if current_user.is_authenticated:
                return redirect('/notes')
            else:
                flash('User not authenticated', 'error')
                return redirect('/login')
        else:
            flash('Email or password do not match', 'error')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/notes', methods=['POST', 'GET'])
@login_required
def notes():
    if request.method == 'POST':
        title = request.form.get('title')
        note = request.form.get('note')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO notes (user_id, title, note) VALUES (%s, %s, %s)",
                    (current_user.id, title, note))
        mysql.connection.commit()
        cur.close()
        flash('Note added successfully', 'success')
        return redirect('/notes')
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM notes WHERE user_id=%s", (current_user.id,))
        notes_data = cur.fetchall()
        cur.close()
        return render_template('notes.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 5000 ,debug=True)

