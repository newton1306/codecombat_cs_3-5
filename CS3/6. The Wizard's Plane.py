# Move to 'Eszter' and get the secret number from her.
hero.moveXY(16, 32)
esz = hero.findNearestFriend().getSecret()
#xxx=secret
# Multiply by 3 and subtract 2 to get 'Tamas's number.
# Remember to use parentheses to do calculations in the right order.
# Move to 'Tamas' and say his magic number.
num_doctor = esz * 3 - 2
hero.moveXY(24, 28)
hero.say(num_doctor)
# Move to Zsofi and say her magic number.
num_bird = (num_doctor - 1) * 4
hero.moveXY(32, 25)
hero.say(num_bird)
# Move to Istvan and say his magic number.
num_hermes = (num_bird + num_doctor) / 2
hero.moveXY(40, 21)
hero.say(num_hermes)
# Move to Csilla and say her magic number.
num_purple = (num_doctor + num_bird) * (num_bird - num_hermes)
hero.moveXY(48, 16)
hero.say(num_purple)
