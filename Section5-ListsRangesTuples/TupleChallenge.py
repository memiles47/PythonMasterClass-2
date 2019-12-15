__author__ = 'Michael E Miles'

# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.

# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

imelda = ("More Mayhem", "Imilda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"),
          (4, "Kentish Town Waltz")))

# My Solution
print("Title: {}\nArtist: {}\nReleased: {}".format(imelda[0], imelda[1], imelda[2]))
for x in range(3, 7):
    print("\ttrack: {}, {}".format(imelda[x][0], imelda[x][1]))

# His Solution
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTracks number {}, Title: {}".format(track, title))

# Combination Solution
