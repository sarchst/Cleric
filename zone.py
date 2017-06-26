import pickle
import user
import tile

class Thing():
    """
    Sprites and Terrain objects are things.
    They both contain a tile coordinate and a sheet number.
    """
    def __init__(self, tile, sheet):
        self.tile = tile
        self.sheet = sheet

class public:
    """
    Public attributes.
    """
    terrain = {
        (0,0) : Thing((0,0), 0) # Sample - will be overwritten by a load
    }
    sprites = {
        (0,0) : Thing((0,0), 1) # Sample - will be overwritten by a load
    }

class private:
    """
    Private attributes.
    """
    pass

def update():
    """
    Adds to either terrain or sprites dictionary what user selected.
    """
    global public
    if not user.public.editing and user.public.selected:
        if tile.sprite(user.public.sheet):
            public.sprites[user.public.selected] =\
                Thing(user.public.choice, user.public.sheet)
        else:
            public.terrain[user.public.selected] =\
                Thing(user.public.choice, user.public.sheet)

def load(name):
    """
    Loads sprite and terrain dictionaries from disk.
    """
    global public
    public.terrain = pickle.load(open(name + ".terrain", "r"))
    public.sprites = pickle.load(open(name + ".sprites", "r"))

def save(name):
    """
    Saves sprite and terrain dictionaries to disk.
    """
    pickle.dump(public.terrain, open(name + ".terrain", "w"))
    pickle.dump(public.sprites, open(name + ".sprites", "w"))
