import pygame

sheets = [[
    # 0
    pygame.image.load("Objects/Floor.png"),
    pygame.image.load("Objects/Floor.png")
    ],[
    # 1
    pygame.image.load("Objects/Fence.png"),
    pygame.image.load("Objects/Fence.png")
    ],[
    # 2
    pygame.image.load("Objects/Wall.png"),
    pygame.image.load("Objects/Wall.png")
    ],[
    # 3
    pygame.image.load("Objects/Decor0.png"),
    pygame.image.load("Objects/Decor1.png")
    ],[
    # 4
    pygame.image.load("Objects/Door0.png"),
    pygame.image.load("Objects/Door1.png")
    ],[
    # 5
    pygame.image.load("Objects/Effect0.png"),
    pygame.image.load("Objects/Effect1.png")
    ],[
    # 6
    pygame.image.load("Objects/Ground0.png"),
    pygame.image.load("Objects/Ground1.png")
    ],[
    # 7
    pygame.image.load("Objects/Hill0.png"),
    pygame.image.load("Objects/Hill1.png")
    ],[
    # 8
    pygame.image.load("Objects/Map0.png"),
    pygame.image.load("Objects/Map1.png")
    ],[
    # 9
    pygame.image.load("Objects/Ore0.png"),
    pygame.image.load("Objects/Ore1.png")
    ],[
    # 10
    pygame.image.load("Objects/Pit0.png"),
    pygame.image.load("Objects/Pit1.png")
    ],[
    # 11
    pygame.image.load("Objects/Trap0.png"),
    pygame.image.load("Objects/Trap1.png")
    ],[
    # 12
    pygame.image.load("Objects/Tree0.png"),
    pygame.image.load("Objects/Tree1.png")
    ],[
    # 13
    pygame.image.load("Characters/Aquatic0.png"),
    pygame.image.load("Characters/Aquatic1.png")
    ],[
    # 14
    pygame.image.load("Characters/Avian0.png"),
    pygame.image.load("Characters/Avian1.png")
    ],[
    # 15
    pygame.image.load("Characters/Cat0.png"),
    pygame.image.load("Characters/Cat1.png")
    ],[
    # 16
    pygame.image.load("Characters/Demon0.png"),
    pygame.image.load("Characters/Demon1.png")
    ],[
    # 17
    pygame.image.load("Characters/Dog0.png"),
    pygame.image.load("Characters/Dog1.png")
    ],[
    # 18
    pygame.image.load("Characters/Elemental0.png"),
    pygame.image.load("Characters/Elemental1.png")
    ],[
    # 19
    pygame.image.load("Characters/Humanoid0.png"),
    pygame.image.load("Characters/Humanoid1.png")
    ],[
    # 20
    pygame.image.load("Characters/Misc0.png"),
    pygame.image.load("Characters/Misc1.png")
    ],[
    # 21
    pygame.image.load("Characters/Pest0.png"),
    pygame.image.load("Characters/Pest1.png")
    ],[
    # 22
    pygame.image.load("Characters/Plant0.png"),
    pygame.image.load("Characters/Plant1.png")
    ],[
    # 23
    pygame.image.load("Characters/Player0.png"),
    pygame.image.load("Characters/Player1.png")
    ],[
    # 24
    pygame.image.load("Characters/Quadraped0.png"),
    pygame.image.load("Characters/Quadraped1.png")
    ],[
    # 25
    pygame.image.load("Characters/Reptile0.png"),
    pygame.image.load("Characters/Reptile1.png")
    ],[
    # 26
    pygame.image.load("Characters/Rodent0.png"),
    pygame.image.load("Characters/Rodent1.png")
    ],[
    # 27
    pygame.image.load("Characters/Slime0.png"),
    pygame.image.load("Characters/Slime1.png")
    ],[
    # 28
    pygame.image.load("Characters/Undead0.png"),
    pygame.image.load("Characters/Undead1.png")
    ],[
    # 29
    pygame.image.load("Items/Ammo.png"),
    pygame.image.load("Items/Ammo.png")
    ],[
    # 30
    pygame.image.load("Items/Amulet.png"),
    pygame.image.load("Items/Amulet.png")
    ],[
    # 31
    pygame.image.load("Items/Armor.png"),
    pygame.image.load("Items/Armor.png")
    ],[
    # 32
    pygame.image.load("Items/Book.png"),
    pygame.image.load("Items/Book.png")
    ],[
    # 33
    pygame.image.load("Items/Boot.png"),
    pygame.image.load("Items/Boot.png")
    ],[
    # 34
    pygame.image.load("Items/Chest0.png"),
    pygame.image.load("Items/Chest1.png")
    ],[
    # 35
    pygame.image.load("Items/Flesh.png"),
    pygame.image.load("Items/Flesh.png")
    ],[
    # 36
    pygame.image.load("Items/Food.png"),
    pygame.image.load("Items/Food.png")
    ],[
    # 37
    pygame.image.load("Items/Glove.png"),
    pygame.image.load("Items/Glove.png")
    ],[
    # 38
    pygame.image.load("Items/Hat.png"),
    pygame.image.load("Items/Hat.png")
    ],[
    # 39
    pygame.image.load("Items/Key.png"),
    pygame.image.load("Items/Key.png")
    ],[
    # 40
    pygame.image.load("Items/Light.png"),
    pygame.image.load("Items/Light.png")
    ],[
    # 41
    pygame.image.load("Items/LongWep.png"),
    pygame.image.load("Items/LongWep.png")
    ],[
    # 42
    pygame.image.load("Items/MedWep.png"),
    pygame.image.load("Items/MedWep.png")
    ],[
    # 43
    pygame.image.load("Items/Money.png"),
    pygame.image.load("Items/Money.png")
    ],[
    # 44
    pygame.image.load("Items/Music.png"),
    pygame.image.load("Items/Music.png")
    ],[
    # 45
    pygame.image.load("Items/Potion.png"),
    pygame.image.load("Items/Potion.png")
    ],[
    # 46
    pygame.image.load("Items/Ring.png"),
    pygame.image.load("Items/Ring.png")
    ],[
    # 47
    pygame.image.load("Items/Rock.png"),
    pygame.image.load("Items/Rock.png")
    ],[
    # 48
    pygame.image.load("Items/Scroll.png"),
    pygame.image.load("Items/Scroll.png")
    ],[
    # 49
    pygame.image.load("Items/Shield.png"),
    pygame.image.load("Items/Shield.png")
    ],[
    # 50
    pygame.image.load("Items/ShortWep.png"),
    pygame.image.load("Items/ShortWep.png")
    ],[
    # 51
    pygame.image.load("Items/Tool.png"),
    pygame.image.load("Items/Tool.png")
    ],[
    # 52
    pygame.image.load("Items/Wand.png"),
    pygame.image.load("Items/Wand.png")
    ],[
    # 53
    pygame.image.load("GUI/GUI0.png"),
    pygame.image.load("GUI/GUI1.png")
]]

# Pixels in a tile
width = 16

def grid((x, y)):
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
