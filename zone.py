import pickle

def load(terrain_dict, sprites_dict):
    terrainFile = open("home.terrain", "r")
    spritesFile = open("home.sprites", "r")
    return pickle.load(terrainFile), pickle.load(spritesFile)

def save(terrain_dict, sprites_dict):
    terrainFile = open("home.terrain", 'w')
    pickle.dump(terrain_dict, terrainFile)
    spritesFile = open("home.sprites", 'w')
    pickle.dump(sprites_dict, spritesFile)


terrain = {}
sprites = {}

