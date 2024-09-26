# Stand between the peasant and the tower.

while True:
    enemy = hero.findNearestEnemy()
    friend = hero.findNearestFriend()
    # Calculate x by adding friend.pos.x to enemy.pos.x
    # Then divide by 2.
    # Check the guide if you need more help!
    x = (enemy.pos.x + friend.pos.x) / 2
    # Now do the same for y
    y = (enemy.pos.y + friend.pos.y) / 2
    # Move to the x and y coordinates you calculated.
    hero.moveXY(x,y)

