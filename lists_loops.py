
# question 1
songs = ["ROCKSTAR", "Do It", "For The Night"]

# question 2
# print(songs[1:3])

# question 3
songs[2] = "Poker Face"

# question 4 add
songs.extend(["Goodbyes", "Alors on danse", "99.9%"])
# question 4 remove
songs.remove("Goodbyes")

# question 6
#1
animals = ["Cat", "Dog", "Bird"]
#2
animals.append("Fish")
#3
# print(animals[2])
#4
animals.pop(0)
#5
for i in range(len(animals)):
    print(animals[i])
