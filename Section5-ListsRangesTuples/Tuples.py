__author__ = 'Michael E Miles'

# Tuples are an orders set of data, similar to lists.
# The difference between tuples and list is that Tuples are immutable,
# meaning they can't be changed.

# t = "a", "b", "c"  # This is correct but you should us brackets.
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

welcome = ("Welcome to my Nightmare", "Alice Cooper", 1975)
bad = ("Bad Company", "Bad Company", 1974)
budgie = ("Nightflight", "Budgie", 1981)
imelda = ("More Mayhem", "Imilda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"),
          (4, "Kentish Town Waltz"))
metallica = ("Ride the Lightning", "Metallica", 1984)

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# metallica[0] = "Master of puppets"
# imelda = (imelda[0], "Imelda May", imelda[2])
# print(imelda)
#
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)

title, artist, year, track1, track2, track3, track4 = imelda
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)
