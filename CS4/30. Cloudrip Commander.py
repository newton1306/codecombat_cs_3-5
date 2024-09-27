# Summon some soldiers, then direct them to your base.

# Each soldier costs 20 gold.
while hero.gold >= hero.costOf("soldier"):
    hero.summon("soldier")
    
soldiers = hero.findFriends()
soldierIndex = 0
# Add a while loop to command all the soldiers.
while soldierIndex < len(soldiers):  # Loop through all soldiers
    soldier = soldiers[soldierIndex]
    hero.command(soldier, "move", {"x": 50, "y": 40})  # Command the soldier to move to base
    soldierIndex += 1  # Increment the soldierIndex

# Go join your comrades!
hero.moveXY(50, 40)  # Move the hero to the same location
