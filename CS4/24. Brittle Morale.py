# You have one arrow. Make it count!

# This should return the enemy with the most health.
def findStrongestEnemy(enemies):
    strongest = None
    strongestHealth = 0
    enemies = hero.findEnemies()
    for enemy in enemies:
        if enemy.health > strongestHealth:
            strongestHealth = enemy.health
            strongest = enemy
    return strongest


enemies = hero.findEnemies()
leader = findStrongestEnemy(enemies)
if leader:
    hero.say(leader)
