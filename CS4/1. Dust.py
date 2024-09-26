# Use a while to loop until you have counted 10 attacks.

attacks = 0
while attacks < 10:
    enemy = hero.findNearestEnemy()
    if (enemy):
        hero.attack(enemy)
        attacks += 1
# Как только закончишь, отступай к засаде.
if (enemy and hero.isReady('cleave')):
    hero.cleave(enemy)
hero.moveXY(51, 31)
hero.moveXY(68, 27)
hero.moveXY(79, 33)

# When you're done, retreat to the ambush point.
hero.say("I should retreat!") #∆ Don't just stand there blabbering!
