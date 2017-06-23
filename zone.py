import pickle


def load(name):
    global terrain, sprites 
    terrain = pickle.load(open(name + ".terrain", "r"))
    sprites = pickle.load(open(name + ".sprites", "r"))

def save(name):
    pickle.dump(terrain, open(name + ".terrain", 'w'))
    pickle.dump(sprites, open(name + ".sprites", 'w'))


terrain = {}
sprites = {}

