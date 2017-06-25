import pickle
import user
import tile

class Thing():
    def __init__(self, tile, sheet):
        self.tile = tile
        self.sheet = sheet

terrain = {
    (0,0) : Thing((0,0), 0)
}

sprites = {
    (0,0) : Thing((0,0), 1)
}

def update():
    global terrain, sprites
    if not user.editing and user.selected:
        if tile.sprite(user.sheet):
            sprites[user.selected] = Thing(user.choice, user.sheet)
        else:
            terrain[user.selected] = Thing(user.choice, user.sheet)

def load(name):
    global terrain, sprites
    terrain = pickle.load(open(name + ".terrain", "r"))
    sprites = pickle.load(open(name + ".sprites", "r"))

def save(name):
    pickle.dump(terrain, open(name + ".terrain", "w"))
    pickle.dump(sprites, open(name + ".sprites", "w"))
