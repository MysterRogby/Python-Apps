import random

file = open("users.txt")
users = file.readlines()
winner = random.choice(users)
winner = winner.rstrip()
newfile = open("winner.txt", "w")
newfile.writelines(winner)

file.close()
