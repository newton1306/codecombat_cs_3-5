# Lure ogres into traps with decoys.

# This function has the hero collect gold until they have enoughGold.
def collectUntil(enoughGold):
    # While hero.gold is less than enoughGold:
    while enoughGold>hero.gold: 
        item = hero.findNearestItem()
        # Find a coin and take it: 
        hero.moveXY(item.pos.x,item.pos.y)
    pass

# Collect 25 gold for one decoy and build it on the red mark.
collectUntil(25)
hero.buildXY("decoy", 40, 52)
# It's better to hide.
hero.moveXY(20, 52)
# Use the collectUntil function to collect 50 gold:
collectUntil(50)
# Build a "decoy" on the bone mark:
hero.buildXY("decoy", 68, 22)
# Build a "decoy" on the wooden mark:
hero.buildXY("decoy", 30, 20)
