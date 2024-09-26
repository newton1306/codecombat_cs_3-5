# We need to know the name of our new pet.

# Use this function as a handler for "hear" events on pet.
def onHear(event):
    # Don't change this function.
    pet.say("Meow Woof Meow")
    pet.say("Woof Woof")
    pet.say("Meow")
    pet.say("Meow")
    pet.say("Meow Woof Meow Meow")

# Use the pet.on(eventType, eventHandler) method
# Assign the onHear function to handle "hear" events.


# It must be after "pet.on".
pet.on("hear", onHear)
hero.say("What's you name, buddy?")
hero.say("Could you repeat it?")
