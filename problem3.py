#A File contains a word "Machine" multiple times. We need to write a program which replace this word with this special Character ##### by updating the file.

word = "Machine"
with open("anyfile.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word,"######")

with open("anyfile.txt", "w") as f:
    content = f.write(contentNew)