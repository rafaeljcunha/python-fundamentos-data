album_set1 = set(["Thriller","Back in Black","AC/DC"])
album_set2 = set(["AC/DC","Back in Black","The Dark Side of the Moon"])

album1_dif = album_set1.difference(album_set2)
print(album1_dif)

album2_dif = album_set2.difference(album_set1)
print(album2_dif)