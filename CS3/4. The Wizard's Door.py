# Move to 'Laszlo' and get his secret number.
hero.moveXY(30, 13)
las = hero.findNearestFriend().getSecret()

# Add 7 to 'Laszlo's number to get 'Erzsebet's number.
# Move to 'Erzsebet' and say her magic number.
erz = las + 7
hero.moveXY(17, 26)
hero.say(erz)

# Divide 'Erzsebet's number by 4 to get 'Simonyi's number.
# Go to 'Simonyi' and tell him his number.
hero.moveXY(30, 39)
hero.say(erz/4)
# Multiply 'Simonyi's number by 'Laszlo's to get 'Agata's number.
# Go to 'Agata' and tell her her number.
hero.moveXY(43, 26)
hero.say(erz/4*las)
