# Lists and Loops Tutorial by Tristan Thompson 9-23-2000

songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[1])
print(songs[1:3]) # prints first and last element ("Rockstar" and "Do It")

#update the last element
songs[2] = "Drops of Jupiter"

songs.extend(["Little Rain", "Peach", "Black Betty"])

songs.remove("ROCKSTAR")

# print the list
print(songs)

# Option 1
for song in songs:
    print(song)

# Option 2
for i in range(len(songs)):
    print(songs[i])

animals = ["dog", "cat", "fish"]

animals.append("lizard")

print(animals[2])

animals.pop(0)

for animal in animals:
    print(animal)

