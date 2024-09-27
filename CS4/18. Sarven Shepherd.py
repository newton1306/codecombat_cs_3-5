# Use while loops to pick out the ogre

while True:
    enemies = hero.findEnemies()
    enemyIndex = 0

    # Wrap this logic in a while loop to attack all enemies.
    # Find the array's length with:  len(enemies)
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        # "!=" means "not equal to."
        if enemy.type != "sand-yak":
            # While the enemy's health is greater than 0, attack it!
            hero.attack(enemy)
            pass
        enemyIndex += 1
        # Between waves, move back to the center.
        
    