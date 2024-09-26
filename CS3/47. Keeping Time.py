# Use your new skill to choose what to do: hero.time

while True:
    if hero.time < 10 or hero.time > 30:
        enemy = hero.findNearestEnemy()
        if enemy:
            if hero.health < hero.maxHealth / 4:
                hero.moveXY(21, 52)
            elif hero.isReady("cleave"):
                hero.cleave(enemy)
            elif hero.isReady("bash"):
                hero.bash(enemy)
            elif hero.isReady("power-up"):
                hero.powerUp()
            else:
                hero.attack(enemy)
    elif hero.time <= 30:
        item = hero.findNearestItem()
        if item:
            moveToX = item.pos.x
            moveToY = item.pos.y
            hero.moveXY(moveToX, moveToY)

