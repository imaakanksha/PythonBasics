# Write a program to make a copy of the text file. "poem.txt"

with open("poem.txt") as f:
    content = f.read()

with open("poem_copy.txt","w") as f:
    f.write(content)