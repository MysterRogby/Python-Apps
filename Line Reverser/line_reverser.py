file = open("input.txt")
lines = file.readlines()
lines[-1] = lines[-1] + "\n"
lines.reverse()
newfile = open("result.txt", "w")
newfile.writelines(lines)

file.close()
newfile.close()
