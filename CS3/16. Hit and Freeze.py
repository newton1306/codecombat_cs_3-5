# You are trapped. Don't move, it'll be painful.

# This function checks if the enemy is in your attack range.
def inAttackRange(enemy):
    distance = hero.distanceTo(enemy)
    # Almost all swords have attack range of 3.
    if distance <= 3:
        return True
    else:
        return False

# Attack ogres only when they're within reach.
while True:
    # Find the nearest enemy and store it in a variable.
    enemy = hero.findNearestEnemy()
    
    # Call inAttackRange(enemy), with the enemy as the argument
    # and save the result in the variable canAttack.
    # ไม่จำเป็นนน
    # If the result stored in canAttack is True, then attack!
    if inAttackRange(enemy):
        hero.attack(enemy)
    pass
