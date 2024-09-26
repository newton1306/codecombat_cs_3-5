# Defeat the enemy hero in two minutes.

summonOrder = ["soldier", "soldier"]
summonCount = 0

while True:
    enemies = hero.findEnemies()
    nearestEnemy = hero.findNearest(enemies)
    
    # Your hero can collect coins and summon troops.
    summonType = summonOrder[summonCount % summonOrder.length]
    if hero.gold > hero.costOf(summonType):
        hero.summon(summonType)
        summonCount += 1
    
    # He also commands your allies in battle.
    friends = hero.findFriends()
    for friend in friends:
        hero.command(friend, "attack", friend.findNearest(enemies))
    
    # Gather coins, attack the enemy, or both!
    
    