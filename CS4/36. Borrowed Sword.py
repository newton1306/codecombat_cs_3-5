# For this level, your hero doesn't fight.
# Command your archers to focus fire on the enemy with the most health!
def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'archer':
            CommandArcher(friend)

def CommandArcher(soldier):
    target = None
    leastHealth = 0
    enemyIndex = 0
    enemies = hero.findEnemies()
    # Просмотрите всех врагов.
    while enemyIndex < len(enemies):
        if enemies[enemyIndex].health > leastHealth:
            leastHealth = enemies[enemyIndex].health
            target = enemies[enemyIndex]
        enemyIndex += 1
    if target:
        hero.command(soldier, "attack", target)

while True:
    commandTroops()
