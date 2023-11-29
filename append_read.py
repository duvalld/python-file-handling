# Opens for appending and reading, creates if not exists.
with open("python-file-handling/doc1.txt", "a+") as file:
    file.write("\nNew Line")
    # file.writeline("\nNew Line") bf
    file.seek(0)
    content = file.read()
    print(content)