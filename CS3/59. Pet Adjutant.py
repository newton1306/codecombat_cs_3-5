# Your pet can help you survive until you can escape.

def onHear(event):
    # event.message contains the text that was heard.
    # If somebody said "Fire"
    if event.message == "Fire":
        # Move to the bottom X mark with pet.moveXY()
        pet.moveXY(64, 16)
        # Say something with pet.say()
        pet.say("jubjub")
        pass
    # If somebody said "Heal"
    elif event.message == "Heal":
        # Move to the top X mark with pet.moveXY()
        hero.moveXY(64, 52)
        # Say something with pet.say()
        hero.say("jubjub")
        pass

pet.on("hear", onHear)

# You don't have to change the code below.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # If an enemy is too strong.
        if enemy.type == "brawler":
            hero.say("Fire")
        else:
            hero.attack(enemy)
    else:
        # If your hero needs healing.
        if hero.health < hero.maxHealth / 2:
            hero.say("Heal")
