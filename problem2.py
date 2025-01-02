#Write a program to generate the multiplication tables from 2 to 20 and write it to the different files. Place all these files of the tables in one folder.

def generateTable(n):
    table=""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"

        with open(f"table/table_{n}.txt", "w") as f:
            f.write(table)

for i in range(2,21):
    generateTable(i)