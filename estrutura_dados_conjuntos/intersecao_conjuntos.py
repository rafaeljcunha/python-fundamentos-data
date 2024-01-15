album_set1 = set(["Thriller","Back in Black","AC/DC"])
album_set2 = set(["AC/DC","Back in Black","The Dark Side of the Moon"])

intersection = album_set1 & album_set2
print(intersection)

album1 = album_set1.intersection(album_set2)
print(album1)
