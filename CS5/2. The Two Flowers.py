# If the peasant is damaged, the flowers will shrink!

def summonSoldiers():
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")

# Define the function: commandSoldiers
def commandSoldiers():
    for soldier in hero.findByType("soldier"):
        enemy = soldier.findNearestEnemy()
        if enemy:
            hero.command(soldier, "attack", enemy)

# Define the function: pickUpNearestCoin
def pickUpNearestCoin():
    nearestCoin = hero.findNearest(hero.findItems())
    if nearestCoin:
        hero.move(nearestCoin.pos)

peasant = hero.findByType("peasant")[0]

while True:
    summonSoldiers()
    commandSoldiers()
    pickUpNearestCoin()
