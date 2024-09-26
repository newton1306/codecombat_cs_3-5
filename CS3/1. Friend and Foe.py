# Peasants and peons are gathering in the forest.
# Command the peasants to battle and the peons to go away!

while True:
    friend,enemy = hero.findNearestFriend(),hero.findNearestEnemy()
    if friend:
        hero.say("To battle, " + friend.id + "!")
    # Now find the nearest enemy and tell them to go away.
    if enemy:
        hero.say("To go away, " + enemy.id + "!")
