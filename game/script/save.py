import json

empty_save = {
    'progress': [],
    'position': [0, 0],
    'player_level': 1,
    'player_exp': 0,
    'player_exp_max': 40,
    'adventure_mode': False,
    'inventory': [],
    'deck': [],
    'weapon': 0,
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

def write_save_data(game):
    f = open('save/save.txt', 'w')
    f.write(json.dumps(game.save))
    f.close()

def erase_save_data(game):
    f = open('save/save.txt', 'w')
    f.write(json.dumps(empty_save))
    f.close()
    f = open('save/save.txt', 'r')
    game.save = json.loads(f.read())
    f.close()