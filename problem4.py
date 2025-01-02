#Repeat the last question for the list of such words which are to be censored.

words = ["Tiger", "Donkey", "Bad", "worst"]
with open("censor.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#"*len(word))

with open("censor.txt", "w") as f:
    f.write(content)