# Only your pet can wake the wizard up.

def onHear(event):
    # "hear" events set the event.speaker property.
    # Check if the pet has heard the hero:
    if event.speaker == hero:
        pet.say("WOOF")

# Assign the event handler for "hear" event.
pet.on("hear", onHear)

while True:
    enemy = hero.findNearestEnemy()
    # If there is an enemy:
    if enemy:
        # Use hero.say() to alert your pet
        hero.say("555")
        # Move to the X in the camp.
        hero.moveXY(30, 33)
        # Then return to the X outside the camp.
        hero.moveXY(30, 15)
