while True:
    # Check the distance to the nearest enemy.
    nearestEnemy = hero.findNearestEnemy()
    distance = hero.distanceTo(nearestEnemy)
    # If it comes closer than 10 meters, cleave it!
    if (distance<5):
        if hero.isReady("cleave"):
            hero.cleave(nearestEnemy)
        else:
            hero.attack(nearestEnemy)
    # Else, attack the "Chest" by name.
    else:
        hero.attack('Chest')

    