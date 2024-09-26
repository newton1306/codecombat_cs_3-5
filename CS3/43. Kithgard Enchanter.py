# Define your own simple movement functions.
# Define moveRight
# Note: each function should move the hero 12 meters!
def moveRight():
    target = {"x": hero.pos.x + 12, "y": hero.pos.y}
    while hero.distanceTo(target) > 0:
        hero.moveXY(hero.pos.x + 12, hero.pos.y);

# Define moveLeft
def moveLeft():
    target = {"x": hero.pos.x - 12, "y": hero.pos.y}
    while hero.distanceTo(target) > 0:
        hero.moveXY(hero.pos.x - 12,hero.pos.y);

# Define moveUp
def moveUp():
    target = {"x": hero.pos.x, "y": hero.pos.y + 12}
    while hero.distanceTo(target) > 0:
        hero.moveXY(hero.pos.x, hero.pos.y + 12);

# Define moveDown
def moveDown():
    target = {"x": hero.pos.x, "y": hero.pos.y - 12}
    while hero.distanceTo(target) > 0:
        hero.moveXY(hero.pos.x,hero.pos.y-12);

# Now, use those functions!
moveRight()
moveDown()
moveUp()
moveUp()
moveRight()
