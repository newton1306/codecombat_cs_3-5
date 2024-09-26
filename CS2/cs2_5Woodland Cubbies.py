# Navigate to red X marks, but be on the lookout!
# These forest areas may contain ogres!

hero.moveXY(19, 33)
enemy = hero.findNearestEnemy()
# The if-statement will check if a variable has an ogre.
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)

hero.moveXY(49, 51)
enemy = hero.findNearestEnemy()
if enemy:
    # Attack the enemy here:
    hero.attack(enemy)
    hero.attack(enemy)
    # `pass` statement is a placeholder. It does nothing and helps close if-statements.
    pass

hero.moveXY(58, 14)
enemy = hero.findNearestEnemy()
# Use an if-statement to check if enemy exists:

    # If enemy exists, attack it:
    
    