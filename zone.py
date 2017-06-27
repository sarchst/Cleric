import pickle
import user
import tile

class Thing():
    """
    A tile on a sheet is classified as a Thing.
    """
    def __init__(self, tile, sheet):
        self.tile = tile
        self.sheet = sheet

class public:
    """
    Layer 0: Terrain - Ground, Snow, Grass, etc.
    Layer 1: Footing - Necklaces, Weapons, Leaves, etc.
    layer 2: Tabling - Stuff on tables: Food, Girls, etc.
    Layer 3: No Pass - Walls, Characters, Water, Lava, etc.
    Layer 4: Overtop - Above player: door frames, explosions, GUI
    """
    layers = [ {}, {}, {}, {}, {} ]
    # Number or layers
    thickness = 5

def layer(sheet):
    # Layer 0: Terrain
    if sheet in [0]:
        return 0
    # Layer 1: Footing
    if sheet in [3, 6, 11, 47]:
        return 1
    # Layer 2: Tabling
    if sheet in range(29, 47)\
    or sheet in range(48, 53):
        return 2
    # Layer 3: No Pass
    if sheet in [1, 2, 7, 8, 9, 10]\
    or sheet in range(12, 29):
        return 3
    # Layer 4: Overtop
    if sheet in [4, 5, 53]:
        return 4

def update():
    """
    Adds to either terrain or sprites dictionary what user selected.
    """
    if not user.public.editing and user.public.selected:
        # The sprite sheet indicates the render layer
        public.layers[layer(user.public.sheet)][user.public.selected] =\
            Thing(user.public.choice, user.public.sheet)

def load(name):
    """
    Loads sprite and terrain dictionaries from disk.
    """
    public.layers[0] = pickle.load(open(name + ".terrain", "r"))
    public.layers[1] = pickle.load(open(name + ".footing", "r"))
    public.layers[2] = pickle.load(open(name + ".tabling", "r"))
    public.layers[3] = pickle.load(open(name + ".no_pass", "r"))
    public.layers[4] = pickle.load(open(name + ".overtop", "r"))

def save(name):
    """
    Saves sprite and terrain dictionaries to disk.
    """
    pickle.dump(public.layers[0], open(name + ".terrain", "w"))
    pickle.dump(public.layers[1], open(name + ".footing", "w"))
    pickle.dump(public.layers[2], open(name + ".tabling", "w"))
    pickle.dump(public.layers[3], open(name + ".no_pass", "w"))
    pickle.dump(public.layers[4], open(name + ".overtop", "w"))
