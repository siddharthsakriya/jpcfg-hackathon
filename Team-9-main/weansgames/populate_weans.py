import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'weansgames.settings')

import django
django.setup()
from tournaments.models import Player, Genre, Game, Event, GameResult, Kid, Volunteer, Staff, PlayerGamePreferences
from django.contrib.auth.models import User
from tournaments.forms import UserForm

def populate():
    players = [{'name': 'John', 'surname': 'Smith'},
               {'name': 'Jane', 'surname': 'Doe'},
               {'name': 'Bob', 'surname': 'Smith'},
               {'name': 'Alice', 'surname': 'Doe'},
               {'name': 'Jack', 'surname': 'Smith'},
               {'name': 'Jill', 'surname': 'Doe'},
               {'name': 'Bill', 'surname': 'Smith'},
               {'name': 'John', 'surname': 'Doe'},] 
    
    genres = ['Action', 'Adventure', 'RPG', 'Simulation', 'Strategy', 'Sports', 'Puzzle', 'Idle', 'Casual', 'Arcade']

    games = [{'name': 'Minecraft', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Adventure'},
                {'name': 'Fortnite', 'quantity': 10, 'description': 'A game about building forts and going on adventures.', 'genre': 'Action'},
                {'name': 'League of Legends', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Strategy'},
                {'name': 'Overwatch', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Action'},
                {'name': 'World of Warcraft', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'RPG'},
                {'name': 'Dota 2', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Strategy'},
                {'name': 'Counter Strike: Global Offensive', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Action'},
                {'name': 'Grand Theft Auto V', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Action'},
                {'name': 'The Witcher 3: Wild Hunt', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'RPG'},
                {'name': 'The Elder Scrolls V: Skyrim', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'RPG'},
                {'name': 'The Legend of Zelda: Breath of the Wild', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Adventure'},
                {'name': 'Red Dead Redemption 2', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Action'},
                {'name': 'Fallout 4', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'RPG'},
                {'name': 'God of War', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Action'},
                {'name': 'Uncharted 4: A Thief\'s End', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Action'},
                {'name': 'Horizon Zero Dawn', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Action'},
                {'name': 'Bloodborne', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Action'},
                {'name': 'The Last of Us Remastered', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Action'},
                {'name': 'Super Mario Odyssey', 'quantity': 10, 'description': 'A game about placing blocks and going on adventures.', 'genre': 'Adventure'},]
    
    events = [{'name': 'Weans Games 2020', 'startDate': '2020-03-01 00:00:00', 'endDate': '2020-03-01 00:00:00', 'game': 'Minecraft'},
                {'name': 'Weans Games 2021', 'startDate': '2020-03-01 00:00:00', 'endDate': '2020-03-01 00:00:00', 'game': 'Fortnite'},
                {'name': 'Weans Games 2022', 'startDate': '2020-03-01 00:00:00', 'endDate': '2020-03-01 00:00:00', 'game': 'League of Legends'},
                {'name': 'Weans Games 2023', 'startDate': '2020-03-01 00:00:00', 'endDate': '2020-03-01 00:00:00', 'game': 'Overwatch'},
                {'name': 'Weans Games 2024', 'startDate': '2020-03-01 00:00:00', 'endDate': '2020-03-01 00:00:00', 'game': 'World of Warcraft'},
                {'name': 'Weans Games 2025', 'startDate': '2020-03-01 00:00:00', 'endDate': '2020-03-01 00:00:00', 'game': 'Dota 2'},
                {'name': 'Weans Games 2026', 'startDate': '2020-03-01 00:00:00', 'endDate': '2020-03-01 00:00:00', 'game': 'Counter Strike: Global Offensive'},
                {'name': 'Weans Games 2027', 'startDate': '2020-03-01 00:00:00', 'endDate': '2020-03-01 00:00:00', 'game': 'Grand Theft Auto V'},
                {'name': 'Weans Games 2028', 'startDate': '2020-03-01 00:00:00', 'endDate': '2020-03-02 00:00:00', 'game': 'The Witcher 3: Wild Hunt'},
                {'name': 'Weans Games 2029', 'startDate': '2020-03-02 00:00:00', 'endDate': '2020-03-02 00:00:00', 'game': 'The Elder Scrolls V: Skyrim'},
                {'name': 'Weans Games 2030', 'startDate': '2020-03-02 00:00:00', 'endDate': '2020-03-02 00:00:00', 'game': 'The Legend of Zelda: Breath of the Wild'},
                {'name': 'Weans Games 2031', 'startDate': '2020-03-02 00:00:00', 'endDate': '2020-03-02 00:00:00', 'game': 'Red Dead Redemption 2'},
                {'name': 'Weans Games 2032', 'startDate': '2020-03-02 00:00:00', 'endDate': '2020-03-02 00:00:00', 'game': 'Fallout 4'},
                {'name': 'Weans Games 2033', 'startDate': '2020-03-02 00:00:00', 'endDate': '2020-03-02 00:00:00', 'game': 'God of War'},
                {'name': 'Weans Games 2034', 'startDate': '2020-03-02 00:00:00', 'endDate': '2020-03-02 00:00:00', 'game': 'Uncharted 4: A Thief\'s End'},
                {'name': 'Weans Games 2035', 'startDate': '2020-03-02 00:00:00', 'endDate': '2020-03-02 00:00:00', 'game': 'Horizon Zero Dawn'},
                {'name': 'Weans Games 2036', 'startDate': '2020-03-02 00:00:00', 'endDate': '2020-03-02 00:00:00', 'game': 'Bloodborne'},
                {'name': 'Weans Games 2037', 'startDate': '2020-03-03 00:00:00', 'endDate': '2020-03-03 00:00:00', 'game': 'The Last of Us Remastered'},]

    kids = [{'name': 'John', 'surname': 'Smith', 'age': 10, 'availability': True},
            {'name': 'Jane', 'surname': 'Doe', 'age': 11, 'availability': True},
            {'name': 'Bob', 'surname': 'Smith', 'age': 12, 'availability': True},
            {'name': 'Alice', 'surname': 'Doe', 'age': 13, 'availability': True},]
    
    volunteers = [{'name': 'Jack', 'surname': 'Smith', 'age': 14, 'isVerified': True},
                {'name': 'Jill', 'surname': 'Doe', 'age': 15, 'isVerified': True},
                {'name': 'Bill', 'surname': 'Smith', 'age': 16, 'isVerified': True},
                {'name': 'John', 'surname': 'Doe', 'age': 17, 'isVerified': True},] 
    
    staff = [{'firstname': 'John', 'surname': 'Smith', 'role_choice': 'N', 'availability': True},
             {'firstname': 'Jane', 'surname': 'Doe', 'role_choice': 'D', 'availability': True},
             {'firstname': 'Bob', 'surname': 'Smith', 'role_choice': 'A', 'availability': False},
             {'firstname': 'Alice', 'surname': 'Doe', 'role_choice': 'N', 'availability': False},
             {'firstname': 'Jack', 'surname': 'Smith', 'role_choice': 'D', 'availability': True},
             {'firstname': 'Jill', 'surname': 'Doe', 'role_choice': 'A', 'availability': True},]
    
    player_preferences = [{'player': 'John Smith', 'genre': 'Action'},
                          {'player': 'John Smith', 'genre': 'Adventure'},
                          {'player': 'John Smith', 'genre': 'RPG'},
                          {'player': 'John Smith', 'genre': 'Simulation'},
                          {'player': 'John Smith', 'genre': 'Strategy'},
                          {'player': 'John Smith', 'genre': 'Sports'},
                          {'player': 'John Smith', 'genre': 'Puzzle'},
                          {'player': 'John Smith', 'genre': 'Idle'},
                          {'player': 'John Smith', 'genre': 'Casual'},
                          {'player': 'John Smith', 'genre': 'Arcade'},
                          {'player': 'Jane Doe', 'genre': 'Action'},
                          {'player': 'Jane Doe', 'genre': 'Adventure'},
                          {'player': 'Jane Doe', 'genre': 'RPG'},
                          {'player': 'Jane Doe', 'genre': 'Simulation'},
                          {'player': 'Jane Doe', 'genre': 'Strategy'},
                          {'player': 'Jane Doe', 'genre': 'Sports'},
                          {'player': 'Jane Doe', 'genre': 'Puzzle'},
                          {'player': 'Jane Doe', 'genre': 'Idle'},
                          {'player': 'Jane Doe', 'genre': 'Casual'},
                          {'player': 'Jane Doe', 'genre': 'Arcade'},
                          {'player': 'Bob Smith', 'genre': 'Action'},
                          {'player': 'Bob Smith', 'genre': 'Adventure'},
                          {'player': 'Bob Smith', 'genre': 'RPG'},
                          {'player': 'Bob Smith', 'genre': 'Simulation'},
                          {'player': 'Bob Smith', 'genre': 'Strategy'},
                          {'player': 'Bob Smith', 'genre': 'Sports'},
                          {'player': 'Bob Smith', 'genre': 'Puzzle'},
                          {'player': 'Bob Smith', 'genre': 'Idle'},
                          {'player': 'Bob Smith', 'genre': 'Casual'},
                          {'player': 'Bob Smith', 'genre': 'Arcade'},
                          {'player': 'Alice Doe', 'genre': 'Action'},
                          {'player': 'Alice Doe', 'genre': 'Adventure'},
                          {'player': 'Alice Doe', 'genre': 'RPG'},
                          {'player': 'Alice Doe', 'genre': 'Simulation'},
                          {'player': 'Alice Doe', 'genre': 'Strategy'},
                          {'player': 'Alice Doe', 'genre': 'Sports'},
                          {'player': 'Alice Doe', 'genre': 'Puzzle'},
                          {'player': 'Alice Doe', 'genre': 'Idle'},]

    game_results = [{'event': 'Weans Games 2020', 'player_one': 'John Smith', 'player_two': 'Jane Doe', 'player_one_won': True},
                    {'event': 'Weans Games 2021', 'player_one': 'John Smith', 'player_two': 'Bob Smith', 'player_one_won': False},
                    {'event': 'Weans Games 2022', 'player_one': 'John Smith', 'player_two': 'Alice Doe', 'player_one_won': True},
                    {'event': 'Weans Games 2023', 'player_one': 'John Smith', 'player_two': 'Jack Smith', 'player_one_won': True},
                    {'event': 'Weans Games 2024', 'player_one': 'John Smith', 'player_two': 'Jill Doe', 'player_one_won': False},
                    {'event': 'Weans Games 2025', 'player_one': 'John Smith', 'player_two': 'Bill Smith', 'player_one_won': True},
                    {'event': 'Weans Games 2026', 'player_one': 'Jane Doe', 'player_two': 'Bob Smith', 'player_one_won': True},
                    {'event': 'Weans Games 2027', 'player_one': 'Jane Doe', 'player_two': 'Alice Doe', 'player_one_won': True},]

    for player in players:
        add_player(player['name'], player['surname'])

    for kid in kids:
        add_kid(kid['name'], kid['surname'], kid['age'], kid['availability'])

    for volunteer in volunteers:
        add_volunteer(volunteer['name'], volunteer['surname'], volunteer['isVerified'])

    for genre in genres:
        add_genre(genre)

    for staff_member in staff:
        add_staff(staff_member['firstname'], staff_member['surname'], staff_member['role_choice'], staff_member['availability'])

    for game in games:
        add_game(game['name'], game['quantity'], game['description'], game['genre'])
    
    for event in events:
        add_event(event['name'], event['startDate'], event['endDate'], event['game'])

    for player_preference in player_preferences:
        add_player_preference(player_preference['player'], player_preference['genre'])
    
    for game_result in game_results:
        add_game_result(game_result['event'], game_result['player_one'], game_result['player_two'], game_result['player_one_won'])

#works
def add_player(name, surname):
    p = Player.objects.get_or_create(name=name, surname=surname)[0]
    p.save()
    return p
#works
def add_kid(name, surname, age, availability):
    p = Player.objects.get_or_create(name=name, surname=surname)[0]
    k = Kid.objects.get_or_create(player=p, age=age, availability=availability)[0]
    k.save()
    return k

#works
def add_volunteer(name, surname, isVerified):
    p = Player.objects.get_or_create(name=name, surname=surname)[0]
    user = User.objects.create(username=name+surname, password="DontJudgeMe!")
    v = Volunteer.objects.get_or_create(player=p, user=user, isVerified=isVerified)[0]
    v.save()
    return v

#works
def add_staff(firstname, surname, role_choice, availability):
    s = Staff.objects.get_or_create(firstname=firstname, surname=surname, role_choice=role_choice, availability=availability)[0]
    s.save()
    return s

#works
def add_genre(name):
    g = Genre.objects.get_or_create(name=name)[0]
    g.save()
    return g

#works
def add_game(name, quantity, description, genre):
    game_genre = Genre.objects.get(name=genre)
    g = Game.objects.get_or_create(name=name, quantity=quantity, description=description, genre=game_genre)[0]
    g.save()
    return g

#works
def add_event(name, startDate, endDate, game):
    g = Game.objects.get(name=game)
    e = Event.objects.get_or_create(name=name, startDate=startDate, endDate=endDate, game=g)[0]
    e.save()
    return e

#works
def add_game_result(event, player_one, player_two, player_one_won):
    event_obj = Event.objects.get(name=event)
    player_one_obj = Player.objects.get(name=player_one.split()[0], surname=player_one.split()[1])
    player_two_obj = Player.objects.get(name=player_two.split()[0], surname=player_two.split()[1])
    gr = GameResult.objects.get_or_create(event=event_obj, player_one=player_one_obj, player_two=player_two_obj, player_one_won=player_one_won)[0]
    gr.save()
    return gr

#works
def add_player_preference(player, genre):
    player_obj = Player.objects.get(name=player.split()[0], surname=player.split()[1])
    genre_obj = Genre.objects.get(name=genre)
    pp = PlayerGamePreferences.objects.get_or_create(player=player_obj, genre=genre_obj)[0]
    pp.save()
    return pp

# Start execution here!
if __name__ == "__main__":
    print("Populating Weans...")
    populate()