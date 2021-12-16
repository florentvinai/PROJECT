from flask import Blueprint,  render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from  .models  import connect, reservations, salles, users, get_user, insert_user, add_user, add_user2

#from flask_wtf import CSRFProtect, Form
from wtforms import StringField, SelectField, PasswordField, validators
from wtforms.fields import DateField, TimeField, IntegerField, EmailField


auth = Blueprint('auth', __name__)


# enregistrement de user /authentifiactaion
@auth.route('/signup')
def signup():
    return render_template('signup.html')
# enregistrement de user /authentifiactaion
@auth.route('/signup', methods=['POST'])
def signup_post():

 email = request.form.get('email')
 name = request.form.get('name')
 password = request.form.get('password')

 # connection a la db
 conn = connect("Reservation.sqlite")
# on recupere le user avec les email/password entre par le client
 user = get_user(conn, email, password)

 if user['id'] != 0 : # if a user is found, we want to redirect back to signup page so user can try again
    return redirect(url_for('auth.signup'))

# on recupere toudss les user de la table      
 rows = users(conn)

 for row in rows:
    id = row["id"]

 # on defini un ID pour le user
 id_user= id + 1

 #
 #print(id_user)
 # on contruit le user selon le modele data
 user = {'id' : id_user,'email' : email,'password' : password, 'username' : name, 'fullname' : 'fullname','position' : 'position' }

 #on insere le nouvel user dans la database
 add_user2(conn, user)

 return redirect(url_for('auth.login'))


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():

 email = request.form.get('email')
 password = request.form.get('password')
 remember = True if request.form.get('remember') else False

 # connection a la db
 conn = connect("Reservation.sqlite")
# on recupere le user avec les email/password entre par le client
 user = get_user(conn, email, password)

 print(user['id'])
 print(user)

 if user['id'] == 0 : # if a user is found, we want to redirect back to signup page so user can try again
    return redirect(url_for('auth.signup'))
# if the above check passes, then we know the user has the right credentials

 return render_template('profile.html', row=user)
    
@auth.route('/logout')
def logout():
    return render_template('logout.html')

