import os
while True:
    text = input(": ")
    if text == "exit":
        break
    file = open("save.txt", "a")
    file.write(text)
    file.write("\n")
exit()
