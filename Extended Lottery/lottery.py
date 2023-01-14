import random

file = open("users.txt")
users = file.readlines()
winner = random.choice(users)
winner = winner.rstrip()
newfile = open("winner.txt", "w")
newfile.write("Winner: " + winner + "\n—————\n")
newfile.write("Participants: \n")
newfile.writelines(users)

file.close()
