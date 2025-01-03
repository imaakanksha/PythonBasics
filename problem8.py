#Write a program to find whether a file is identical & matches the content of the another file.

with open("poem.txt") as f:
    content1 = f.read()

with open("poem_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes, the files are identical.")
else:
    print("No, the given files are not identical.")