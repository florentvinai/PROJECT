def salles():
    return [
        {'id': 1, 'salleName': 'SALLEToulouse', 'telephone': True, 'projector': True,'tableau': True,'capacity': 5},
        {'id': 2, 'salleName': 'SALLENice', 'telephone': True, 'projector': False,'tableau': True,'capacity': 15},
        {'id': 3, 'salleName': 'SALLENice1', 'telephone': True, 'projector': False,'tableau': True,'capacity': 15},
        {'id': 4, 'salleName': 'SALLEPARIS', 'telephone': False, 'projector': True,'tableau': True,'capacity': 2}]

def reservations():
    return [
        {'id': 1, 'title': "meetingMarketing", 'salleId': 1, 'userId': 2, 'dateDebut': '2020-08-03 00:00:00', 'durationH': 3, 'descriptionM': 'ceci est une courte description1 du meeting'}, 
        {'id': 2, 'title': "meetingMarketing1", 'salleId': 2, 'userId': 3, 'dateDebut': '2020-01-03 00:00:00', 'durationH': 1, 'descriptionM': 'ceci est une courte description2 du meeting'},
        {'id': 3, 'title': "meetingMarketing2", 'salleId': 3, 'userId': 1, 'dateDebut': '2020-01-03 00:00:00', 'durationH': 1, 'descriptionM': 'ceci est une courte description2 du meeting'},
        {'id': 4, 'title': "meetingMarketing3", 'salleId': 1, 'userId': 2, 'dateDebut': '2020-09-03 00:00:00', 'durationH': 2, 'descriptionM': 'ceci est une courte description3 du meeting'}
    ]

def users():
    return [
        {'id': 1, 'email': 'admin@admin.fr', 'password': 'admin','username': 'admin','fullname': 'admin','position': 'admin'},
        {'id': 2, 'email': 'jcv@toto.fr', 'password': 'toto','username': 'toto','fullname': 'admin','position': 'admin'},
        {'id': 3, 'email': 'jcv@titi.fr', 'password': 'titi','username': 'titi','fullname': 'admin','position': 'admin'}
    ]