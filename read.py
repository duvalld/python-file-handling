# opens for reading
with open("python-file-handling/doc.txt", "r") as file:
    # read
    content = file.read()
    print(content)
    # readlines get result as an array/list
    content = file.readlines()
    print(content)