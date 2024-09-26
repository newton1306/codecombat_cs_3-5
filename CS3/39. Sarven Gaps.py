# Get to the Oasis by moving down 10m at a time.
# Build fences 20m to the left of each ogre.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # buildXY a "fence" 20 meters to enemy's left.
        hero.buildXY('fence', enemy.pos.x - 20, enemy.pos.y)
        pass
    else:
        # moveXY down 10 meters.
        hero.moveXY(hero.pos.x, hero.pos.y - 10)
        pass
