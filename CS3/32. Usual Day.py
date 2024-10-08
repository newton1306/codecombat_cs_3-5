# Defeat munchkins, collect coins. Everything as usual.
# Use AND to check existence and type in one statement.

while True:
    enemy = hero.findNearestEnemy()
    # With AND, the type is only checked if enemy exists.
    if enemy and enemy.type == "munchkin":
        hero.attack(enemy)
    # Find the nearest item.
    item = hero.findNearestItem()
    
    # Collect item if it exists and its type is "coin".
    if item and item.type is "coin":
        hero.moveXY(item.pos.x, item.pos.y)
