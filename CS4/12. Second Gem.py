# One gem is safe, the others are bombs.
# But you know the answer: always take the second.

while True:
    items = hero.findItems()
    # If the length of items is greater or equal to 2:
    if (len(items) > 1):
        # Move to the second item in items
        hero.moveXY(items[1].pos.x, items[1].pos.y)
    # Else:
    else:
        # Move to the center mark.
        hero.moveXY(40, 34)
    