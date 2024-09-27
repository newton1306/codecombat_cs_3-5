# Defeat skeletons and collect lightstones.

while True:
    enemies = hero.findEnemies()
    enemyIndex = 0
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        # Attack while enemy has health.
        while enemy.health > 0:
            hero.attack(enemy)
        enemyIndex += 1
    items = hero.findItems()
    itemIndex = 0
    # Iterate over all items.
    while itemIndex < len(items):
        item = items[itemIndex]
        # While the distance greater than 2:        
        while item and hero.distanceTo(item)>2:
            # Try to take the item.
            hero.moveXY(item.pos.x, item.pos.y)
        # Don't forget to increase itemIndex.
        itemIndex += 1
