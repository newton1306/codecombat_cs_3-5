# This level shows how to define your own functions.
# The code inside a function is not executed immediately. It's saved for later.

def pickUpNearestCoin():
    nearestCoin = hero.findNearest(hero.findItems())
    if nearestCoin:
        hero.move(nearestCoin.pos)

def summonSoldier():
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")

def commandSoldiers():
    for soldier in hero.findFriends():
        enemy = soldier.findNearestEnemy()
        if enemy:
            hero.command(soldier, "attack", enemy)

while True:
    pickUpNearestCoin()
    summonSoldier()
    commandSoldiers()
