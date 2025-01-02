#Write a program to read the text from a given file "poem.txt" and find out whether it contains the word "Machine Learning" or not?
f=open("poem.txt")
content = f.read()
if("Monkey" in content):
    print("The word is present in the file")
else:
    print("The word is not presernt in the file")
f.close()