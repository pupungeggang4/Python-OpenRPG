import json

empty_save = {
    'place': 'home_town',
    'level': 1,
    'exp': 0,
    'card': [],
    'weapon': [],
    'equipment': [],
    'item': []
}

def load_save_data(game):
    try:
        f = open('save/save.txt', 'r')
        game.save = json.loads(f.read())
        f.close()

    except:
        f = open('save/save.txt', 'w')
        f.write(json.dumps(empty_save))
        f.close()
        f = open('save/save.txt', 'r')
        game.save = json.loads(f.read())
        f.close()

def erase_save_data(game):
    pass