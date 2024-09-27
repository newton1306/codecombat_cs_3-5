# You can use findNearestEnemy() on your soldiers to get their nearest enemy instead of yours.
while True:
    friends = hero.findFriends()
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 20:
        if hero.isReady("jump") and hero.distanceTo(enemy) > 10:
            hero.jumpTo(enemy.pos)
        elif hero.isReady("cleave"):
            hero.cleave(enemy)
        elif hero.isReady("bash"):
            hero.bash(enemy)
        elif hero.isReady("power-up"):
            hero.powerUp()
            hero.attack(enemy)
        else:
            hero.attack(enemy)
    else:
        if hero.now() < 7:
            pos = {'x': 87, 'y': 49}
        else:
            pos = {'x': 12, 'y': 47}
        if hero.isReady("jump"):
            hero.jumpTo(pos)
        else:
            hero.move(pos)

    # Use for-loop and for each friend:
    for j in range(len(friends)):
        friend = friends[j]
        if friend.pos.y > 46 and hero.now() < 5:
            pos = {'x': 12, 'y': 64}
        elif friend.pos.y > 46:
            if friend.type != 'archer':
                pos = {'x': 61, 'y': 67}
            else:
                pos = {'x': 42, 'y': 67}
        else:
            if friend.type != 'archer':
                pos = {'x': 45, 'y': 32}
            else:
                pos = {'x': 51, 'y': 32}

        enemy = friend.findNearestEnemy()
        # If they see an enemy then command to attack.
        if friend.health < 29 or (enemy and friend.type == 'archer' and friend.distanceTo(enemy) < 22):
            hero.command(friend, 'move', {'x': 11, 'y': 47})
        elif enemy and friend.distanceTo(enemy) < 20:
            hero.command(friend, 'attack', enemy)
        # Else, command to move east by small steps.
        else:
            hero.command(friend, 'move', pos)
