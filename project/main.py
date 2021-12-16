from flask import Blueprint, render_template
from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from  .models  import connect, reservations, salles, users

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')
    
@main.route('/salle')
def salle():
    conn = connect("Reservation.sqlite")
    rows = salles(conn)
    return render_template('listeSalle.html', rows=rows)

@main.route('/user')
def user():
    conn = connect("Reservation.sqlite")
    rows = users(conn)
    return render_template('listeUser.html', rows=rows)

    
@main.route('/reservation')
def reservation():
    conn = connect("Reservation.sqlite")
    rows = reservations(conn)
    return render_template('listeReservation.html', rows=rows)
   
    
    
