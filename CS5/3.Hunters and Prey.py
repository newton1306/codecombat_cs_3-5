# Ogres are trying to take out your reindeer!
# Keep your archers back while summoning soldiers to attack.

def pickUpCoin():
    # Collect coins.
    items = hero.findItems()
    nearestCoin = hero.findNearest(items)
    if nearestCoin:
        hero.move(nearestCoin.pos)

def summonTroops():
    # Summon soldiers if you have the gold.
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")

# This function has an argument named soldier.
# Arguments are like variables.
# The value of an argument is determined when the function is called.
def commandSoldier(soldier):
    # Soldiers should attack enemies.
    enemy = soldier.findNearestEnemy()
    if enemy:
        hero.command(soldier, "attack", enemy)

# Write a commandArcher function to tell your archers what to do!
# It should take one argument that will represent the archer passed to the function when it's called.
# Archers should only attack enemies who are closer than 25 meters, otherwise, stay still.
def commandArcher(archer):
    enemy = archer.findNearestEnemy()
    if enemy and archer.distanceTo(enemy) < 25:
        hero.command(archer, "attack", enemy)

while True:
    pickUpCoin()
    summonTroops()
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == "soldier":
            # This friend will be assigned to the variable soldier in commandSoldier
            commandSoldier(friend)
        elif friend.type == "archer":
            # Be sure to command your archers.
            commandArcher(friend)
