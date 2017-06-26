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
    if not user.public.editing and user.public.selected:
        if tile.sprite(user.public.sheet):
            sprites[user.public.selected] = Thing(user.public.choice, user.public.sheet)
        else:
            terrain[user.public.selected] = Thing(user.public.choice, user.public.sheet)

def load(name):
    global terrain, sprites
    terrain = pickle.load(open(name + ".terrain", "r"))
    sprites = pickle.load(open(name + ".sprites", "r"))

def save(name):
    pickle.dump(terrain, open(name + ".terrain", "w"))
    pickle.dump(sprites, open(name + ".sprites", "w"))
