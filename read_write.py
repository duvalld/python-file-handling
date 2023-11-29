# Opens for reading and writing
with open("python-file-handling/doc.txt", "r+") as file:
    file.write("data")
    content = file.read()
    print(content)