# Get to the oasis. Watch out for new enemies: ogre scouts!
# Go up and right by adding to the current X and Y position.

while True:
    # If there's an enemy, attack.
    enemy = hero.findNearestEnemy()
    if enemy:
        if (hero.isReady("cleave")):
            hero.cleave(enemy)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
        elif (hero.isReady("power-up")):
            hero.powerUp()
        else:
            hero.attack(enemy)
    # Else, keep moving up and to the right. 
    else:
        x = hero.pos.x + 10
        y = hero.pos.y + 10
        hero.moveXY(x, y)
    pass
    