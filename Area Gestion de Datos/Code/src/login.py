from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_login import login_user
from flask_login import login_required


login = Flask(__name__)

login = Flask(__name__)
login_manager = LoginManager()
login_manager.init_login(login)

@login.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = get_user(request.form['username'])
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('index'))
        flash('Credenciales inválidas')
    return render_template('login.html')
    pass

@login.route('/logout')
def logout():

    pass

# @login.route('/')
# def home():
#     passhash = generate_password_hash('123456'),
#     print(passhash),
#     return passhash
    
# if __name__ == "__main__":
#     login.run()    