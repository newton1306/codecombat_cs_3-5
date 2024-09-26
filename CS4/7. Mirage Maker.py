# Lure the ogres into an ambush!

# While your gold is less than 25, collect coins.
while True:
        items = hero.findItems()
        if (hero.gold < 25):
            nearestItem = hero.findNearest(items)
            if nearestItem:
                hero.moveXY(nearestItem.pos.x, nearestItem.pos.y)
        else:
            break
    
# After the while loop, build a "decoy" at the white X.

# While your health equals maxHealth, say insults

# Then move back to the red X.
hero.buildXY('decoy', 72, 68)
while True:
    if (hero.health == hero.maxHealth):
        hero.say('waka')
    else:
        hero.moveXY(21, 16)
