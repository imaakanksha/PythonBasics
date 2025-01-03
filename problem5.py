#Write a program to find if the word "Python" is present in that logs file or not.

with open("logs.html") as f:
    content = f.read()

if ("Python" in content):
    print("Yes, Python is present in the given file.")
else:
    print("No, Python is not present in the given file.")