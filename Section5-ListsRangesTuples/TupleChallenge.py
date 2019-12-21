__author__ = 'Michael E Miles'

# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.

# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

imelda = ("More Mayhem", "Imilda May", 2011, [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"),
          (4, "Kentish Town Waltz")])

# My Solution
print("My Solution")
print("Title: {}\nArtist: {}\nReleased: {}".format(imelda[0], imelda[1], imelda[2]))
for track in range(4):
    print("\tTrack: {}, {}".format(imelda[3][track][0], imelda[3][track][1]))
print("*" * 40 + "\n")


# His Solution
print("His Solution")
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTracks number {}, Title: {}".format(track, title))
print("*" * 40 + "\n")

# Combination Solution
print("Combined Solution")
title, artist, year, tracks = imelda
print("Title: {}\nArtist: {}\nReleased: {}".format(title, artist, year))
for song in tracks:
    track, title = song
    print("\tTrack: {}, {}".format(track, title))
