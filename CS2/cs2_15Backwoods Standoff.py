# Munchkins are attacking!
# The swarms will come at regular intervals.
# Whenever you can, cleave to clear the mass of enemies.

while True:
    enemy = hero.findNearestEnemy()
    # Use an if-statement with isReady to check "cleave":
    if (enemy and hero.isReady('cleave')):
        # Cleave!
        hero.cleave(enemy)
    # Else, if cleave is not ready:
    else:
        # Attack the nearest ogre!
        hero.attack(enemy)
