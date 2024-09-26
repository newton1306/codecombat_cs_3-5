# Move right, to the oasis.
# Build a "fence" above or below when you see a yak.

while True:
    yak = hero.findNearestEnemy()
    if yak:
        if yak.pos.y > hero.pos.y:
            hero.buildXY('fence', hero.pos.x, yak.pos.y - 10)
        if yak.pos.y < hero.pos.y:
            hero.buildXY('fence', hero.pos.x, yak.pos.y + 10)
        pass
    else:
        hero.moveXY(hero.pos.x + 10, hero.pos.y)
        pass
