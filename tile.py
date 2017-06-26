import pygame

sheets = [[
    pygame.image.load("Objects/Floor.png"),
    pygame.image.load("Objects/Floor.png")
    ],[
    pygame.image.load("Objects/Fence.png"),
    pygame.image.load("Objects/Fence.png")
    ],[
    pygame.image.load("Objects/Wall.png"),
    pygame.image.load("Objects/Wall.png")
    ],[
    pygame.image.load("Objects/Decor0.png"),
    pygame.image.load("Objects/Decor1.png")
    ],[
    pygame.image.load("Objects/Door0.png"),
    pygame.image.load("Objects/Door1.png")
    ],[
    pygame.image.load("Objects/Effect0.png"),
    pygame.image.load("Objects/Effect1.png")
    ],[
    pygame.image.load("Objects/Ground0.png"),
    pygame.image.load("Objects/Ground1.png")
    ],[
    pygame.image.load("Objects/Hill0.png"),
    pygame.image.load("Objects/Hill1.png")
    ],[
    pygame.image.load("Objects/Map0.png"),
    pygame.image.load("Objects/Map1.png")
    ],[
    pygame.image.load("Objects/Ore0.png"),
    pygame.image.load("Objects/Ore1.png")
    ],[
    pygame.image.load("Objects/Pit0.png"),
    pygame.image.load("Objects/Pit1.png")
    ],[
    pygame.image.load("Objects/Trap0.png"),
    pygame.image.load("Objects/Trap1.png")
    ],[
    pygame.image.load("Objects/Tree0.png"),
    pygame.image.load("Objects/Tree1.png")
    ],[
    pygame.image.load("Characters/Aquatic0.png"),
    pygame.image.load("Characters/Aquatic1.png")
    ],[
    pygame.image.load("Characters/Avian0.png"),
    pygame.image.load("Characters/Avian1.png")
    ],[
    pygame.image.load("Characters/Cat0.png"),
    pygame.image.load("Characters/Cat1.png")
    ],[
    pygame.image.load("Characters/Demon0.png"),
    pygame.image.load("Characters/Demon1.png")
    ],[
    pygame.image.load("Characters/Dog0.png"),
    pygame.image.load("Characters/Dog1.png")
    ],[
    pygame.image.load("Characters/Elemental0.png"),
    pygame.image.load("Characters/Elemental1.png")
    ],[
    pygame.image.load("Characters/Humanoid0.png"),
    pygame.image.load("Characters/Humanoid1.png")
    ],[
    pygame.image.load("Characters/Misc0.png"),
    pygame.image.load("Characters/Misc1.png")
    ],[
    pygame.image.load("Characters/Pest0.png"),
    pygame.image.load("Characters/Pest1.png")
    ],[
    pygame.image.load("Characters/Plant0.png"),
    pygame.image.load("Characters/Plant1.png")
    ],[
    pygame.image.load("Characters/Player0.png"),
    pygame.image.load("Characters/Player1.png")
    ],[
    pygame.image.load("Characters/Quadraped0.png"),
    pygame.image.load("Characters/Quadraped1.png")
    ],[
    pygame.image.load("Characters/Reptile0.png"),
    pygame.image.load("Characters/Reptile1.png")
    ],[
    pygame.image.load("Characters/Rodent0.png"),
    pygame.image.load("Characters/Rodent1.png")
    ],[
    pygame.image.load("Characters/Slime0.png"),
    pygame.image.load("Characters/Slime1.png")
    ],[
    pygame.image.load("Characters/Undead0.png"),
    pygame.image.load("Characters/Undead1.png")
    ],[
    pygame.image.load("Items/Ammo.png"),
    pygame.image.load("Items/Ammo.png")
    ],[
    pygame.image.load("Items/Amulet.png"),
    pygame.image.load("Items/Amulet.png")
    ],[
    pygame.image.load("Items/Armor.png"),
    pygame.image.load("Items/Armor.png")
    ],[
    pygame.image.load("Items/Book.png"),
    pygame.image.load("Items/Book.png")
    ],[
    pygame.image.load("Items/Boot.png"),
    pygame.image.load("Items/Boot.png")
    ],[
    pygame.image.load("Items/Chest0.png"),
    pygame.image.load("Items/Chest1.png")
    ],[
    pygame.image.load("Items/Flesh.png"),
    pygame.image.load("Items/Flesh.png")
    ],[
    pygame.image.load("Items/Food.png"),
    pygame.image.load("Items/Food.png")
    ],[
    pygame.image.load("Items/Glove.png"),
    pygame.image.load("Items/Glove.png")
    ],[
    pygame.image.load("Items/Hat.png"),
    pygame.image.load("Items/Hat.png")
    ],[
    pygame.image.load("Items/Key.png"),
    pygame.image.load("Items/Key.png")
    ],[
    pygame.image.load("Items/Light.png"),
    pygame.image.load("Items/Light.png")
    ],[
    pygame.image.load("Items/LongWep.png"),
    pygame.image.load("Items/LongWep.png")
    ],[
    pygame.image.load("Items/MedWep.png"),
    pygame.image.load("Items/MedWep.png")
    ],[
    pygame.image.load("Items/Money.png"),
    pygame.image.load("Items/Money.png")
    ],[
    pygame.image.load("Items/Music.png"),
    pygame.image.load("Items/Music.png")
    ],[
    pygame.image.load("Items/Potion.png"),
    pygame.image.load("Items/Potion.png")
    ],[
    pygame.image.load("Items/Ring.png"),
    pygame.image.load("Items/Ring.png")
    ],[
    pygame.image.load("Items/Rock.png"),
    pygame.image.load("Items/Rock.png")
    ],[
    pygame.image.load("Items/Scroll.png"),
    pygame.image.load("Items/Scroll.png")
    ],[
    pygame.image.load("Items/Shield.png"),
    pygame.image.load("Items/Shield.png")
    ],[
    pygame.image.load("Items/ShortWep.png"),
    pygame.image.load("Items/ShortWep.png")
    ],[
    pygame.image.load("Items/Tool.png"),
    pygame.image.load("Items/Tool.png")
    ],[
    pygame.image.load("Items/Wand.png"),
    pygame.image.load("Items/Wand.png")
    ],[
    pygame.image.load("GUI/GUI0.png"),
    pygame.image.load("GUI/GUI1.png")
]]

width = 16

def sprite(sheet):
    return sheet > 1

def tile((x, y)):
    """
    Returns a tie tuple of a pixel tuple
    """
    return (x / width, y / width)

def pixel((x, y)):
    """
    Returns a pixel tuple of a tile tuple.
    """
    return (x * width, y * width)

def rect((x, y)):
    """
    Returns a rectangular tile tuple of a tile tuple.
    """
    return (pixel((x, y)), (width, width))
