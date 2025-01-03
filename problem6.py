#Write a Program to find out the line numnber where Python is present in the file.

with open("logs.html") as f:
    lines = f.readlines()

lineno=1
for line in lines:
    if("Python" in line):
        print(f"Yes, Python is present in the file. Line No:{lineno}")
        break
    lineno += 1

else:
    print("No, Python is not present in the given file.")