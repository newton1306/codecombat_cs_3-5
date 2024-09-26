# We are field testing a new battle unit: the decoy.
# Build 4 decoys, then report the total to Naria.

decoysBuilt = 0
while True:
    '''coin = hero.findNearestItem()
    if coin:
        # Collect the coin!'''
    item = hero.findNearestItem()
    hero.moveXY(item.pos.x, item.pos.y)
    
    goldAmount=hero.gold
    
    # Each decoy costs 25 gold.
    # If hero.gold is greater than or equal to 25:
    if (goldAmount >= 25):
        hero.buildXY('decoy', item.pos.x, item.pos.y)
        # buildXY a "decoy"
        decoysBuilt = decoysBuilt + 1
        # Add 1 to the decoysBuilt count.
        
    if decoysBuilt == 4:
        # Break out of the loop when you have built 4.
        break
    
hero.say("Done building decoys!")
hero.moveXY(14, 36)
# Say how many decoys you built.
hero.say(decoysBuilt)

