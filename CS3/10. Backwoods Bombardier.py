# The pos property is an object with x and y properties.
# pos.x is a number representing the horizontal position on the map
# pos.y is a number representing the vertical position on the map

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        x = enemy.pos.x
        # Get the enemy's y position!
        # ไม่จำเป็นนน
        #y = 0 # ∆ Change this!
        
        # say the x and y position separated by a comma
        hero.say(enemy.pos.x + "," + enemy.pos.y)
    else:
        hero.say("Cease" + " " + "Fire!")
