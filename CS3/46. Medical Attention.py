# Ask the healer for help when you're under one-half health.

while True:
    currentHealth = hero.health
    healingThreshold = hero.maxHealth / 2
    # If your current health is less than the threshold,
    # move to the healing point and say, "heal me".
    # Otherwise, attack. You'll need to fight hard!
    if (currentHealth < healingThreshold):
        hero.moveXY(65, 45)
        hero.say('heal me')
    else:
        enemy = hero.findNearestEnemy()
        if enemy:
            if (hero.isReady("cleave")):
                hero.cleave(enemy)
            elif (hero.isReady("bash")):
                hero.bash(enemy)
            elif (hero.isReady("power-up")):
                hero.powerUp()
            else: hero.attack(enemy)
    