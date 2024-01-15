album_set1 = set(["Thriller","Back in Black","AC/DC"])
album_set2 = set(["AC/DC","Back in Black","The Dark Side of the Moon"])

isSuper = set(album_set1).issuperset(album_set2)
isSub = set(album_set2).issubset(album_set1)

print(isSuper)
print(isSub)