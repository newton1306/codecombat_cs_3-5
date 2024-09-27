# Protect the cage.
# Put a soldier at each X.
points = [{"x": 33, "y": 42},
          {"x": 47, "y": 42},
          {"x": 33, "y": 26},
          {"x": 47, "y": 26}]

# 1. Collect 80 gold.
while hero.gold < 80:
    item = hero.findNearestItem()
    if item:
        if hero.isReady("jump"):
            hero.jumpTo({'x': item.pos.x, 'y': item.pos.y})
        else:
            hero.move(item.pos)

# 2. Build 4 soldiers.
for i in range(4):
    hero.summon("soldier")
    
# 3. Send your soldiers into position.
while True:
    friends = hero.findFriends()
    for j in range(len(friends)):
        point = points[j]
        friend = friends[j]
        enemy = friend.findNearestEnemy()
        if enemy and enemy.team == "ogres" and friend.distanceTo(enemy) < 5:
            # Command friend to attack.
            hero.command(friend, 'attack', enemy)
        else:
            # Command friend to move to point.
            hero.command(friend, 'move', point)
