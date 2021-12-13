
import sqlite3
import os

from . import data
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


def dictionary_factory(cursor, row):
  dictionary = {}
  for index in range(len(cursor.description)):
    column_name = cursor.description[index][0]
    dictionary[column_name] = row[index]
  return dictionary


def connect(database):
  connection = sqlite3.connect(database)
  connection.set_trace_callback(print)
  connection.execute('PRAGMA foreign_keys = 1')
  connection.row_factory = dictionary_factory
  return connection



def read_build_script():
  path = os.path.join(os.path.dirname(__file__), 'Build_tables.sql')
  file = open(path)
  script = file.read()
  file.close()
  return script


def create_database(connection):
  script = read_build_script()
  connection.executescript(script)
  connection.commit()


def insert_salle(connection, salle):
  #sql = 'INSERT INTO salles(id, salleName, telephone, projector, tableau, capacity) VALUES (:id, :salleName, :telephone, :projector, :tableau, :capacity);'
  sql = 'INSERT INTO salles VALUES (:id, :salleName, :telephone, :projector, :tableau, :capacity);'
  connection.execute(sql, salle)
  connection.commit()

def insert_user(connection, users):

  password_hash = generate_password_hash(users['password'])
  #sql = 'INSERT INTO users(id, email, password_hash, username, fullname, position ) VALUES (:id, :email, :password_hash, :username, :fullname, :position);'
  sql = 'INSERT INTO users VALUES (:id, :email, :username, :fullname, :position, :password_hash);'
  connection.execute(sql, {'id' : users['id'],'email' : users['email'],'username' : users['username'], 'fullname' : users['fullname'],'position' : users['position'],'password_hash' : password_hash,  })
  #connection.execute(sql, users)
  connection.commit()

def add_user2(connection, users):

  password_hash = generate_password_hash(users['password'])
  
  sql = 'INSERT INTO users VALUES (:id, :email, :username, :fullname, :position,  :password_hash,);'
  connection.execute(sql, {'id' : users['id'],'email' : users['email'], 'username' : users['username'], 'fullname' : users['fullname'],'position' : users['position'], 'password_hash' : password_hash,})
  
  #connection.execute(sql, users)
  connection.commit()

def insert_reservations(connection, reservation):
  #sql = 'INSERT INTO reservations(id, title, salleId, userId, dateDebut, durationH, descriptionM) VALUES (:id, :title, :roomId, :userId, :date, :duration, :descriptionM);'
  sql = 'INSERT INTO reservations VALUES (:id, :title, :salleId, :userId, :dateDebut, :durationH, :descriptionM);'
  connection.execute(sql, reservation)
  connection.commit()


def salles(connection):
  sql = 'SELECT * FROM salles ORDER BY id;'
  cursor = connection.execute(sql)
  return cursor.fetchall()

def users(connection):
  sql = 'SELECT * FROM users ORDER BY id;'
  cursor = connection.execute(sql)
  return cursor.fetchall()


def reservations(connection):
  sql = 'SELECT * FROM reservations ORDER BY id;'
  cursor = connection.execute(sql)
  return cursor.fetchall()


def fill_database(connection):
  for salle in data.salles():
    insert_salle(connection, salle)
  for user in data.users():
    insert_user(connection, user)
  for reservation in data.reservations():
    insert_reservations(connection, reservation)


def salle(connection, team_id):
  sql = 'SELECT * FROM teams WHERE id = :id;'
  cursor = connection.execute(sql, {'id' : team_id})
  result = cursor.fetchone()
  if result is None:
    raise Exception('salle inconnue')
  return result


def reservation(connection, book_id):
  sql = 'SELECT * FROM reservations WHERE id = :id;'
  cursor = connection.execute(sql, {'id' : book_id})
  result = cursor.fetchone()
  if result is None:
    raise Exception('Match inconnu')
  return result



def add_user(connection, email, password):
  hash = generate_password_hash(password)
  sql = '''
    INSERT INTO users(email, password_hash) VALUES (:email, :hash);
  '''
  connection.execute(sql, {'email' : email, 'hash' : hash})
  connection.commit()


def get_user(connection, email, password):
  sql = '''
    SELECT * FROM users WHERE email = :email;
  '''
  cursor = connection.execute(sql, {'email' : email})
  result = cursor.fetchone()
  print(result)

  if result is None:
    #raise Exception('Utilisateur inconnu None')
    return {'id' : 0, 'email' : 'NONE'}
  hash = result['password_hash']
  #if not check_password_hash(hash, password):
    #raise Exception('Utilisateur inconnu hash')
  return {'id' : result['id'], 'email' : result['email'], 'fullname' : result['fullname']}


def change_password(connection, email, old_password, new_password):
  user = get_user(connection, email, old_password)
  sql ='''
    UPDATE users SET password_hash = :hash WHERE id = :id;
  '''
  hash = generate_password_hash(new_password)
  connection.execute(sql, {'id' : user['id'], 'hash' : hash})
  connection.commit()

