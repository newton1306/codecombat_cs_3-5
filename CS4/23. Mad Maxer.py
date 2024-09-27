# Attack the enemy that's farthest away first.

while True:
    farthest = None
    maxDistance = 0
    enemyIndex = 0
    enemies = hero.findEnemies()

    # Look at all the enemies to figure out which one is farthest away.
    while enemyIndex < len(enemies):
        target = enemies[enemyIndex]
        enemyIndex += 1

        # Is this enemy farther than the farthest we've seen so far?
        distance = hero.distanceTo(target)
        if distance > maxDistance: # This is farther than we've seen so far
            maxDistance = distance # So let's update `maxDistance` to the new largest `distance`
            farthest = target # `farthest` is who we plan to attack

    if farthest:
        # Take out the farthest enemy!
        # Keep attacking the enemy while its health is greater than 0.
        while farthest.health > 0:
            if (hero.isReady("cleave")):
                hero.cleave(farthest)
            elif (hero.isReady("bash")):
                hero.bash(farthest)
            elif (hero.isReady("power-up")):
                hero.powerUp()
            else:
                hero.attack(farthest)
        pass
