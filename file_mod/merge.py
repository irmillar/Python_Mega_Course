from datetime import datetime

# Take in all text file names as arguments
def merge(*args):
    # Open a new file
    filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f.txt")
    with open(filename, "w") as combined:
        for inputfile in args:
            with open(inputfile, "r") as file:
                combined.write(file.read())
    # print the file to make sure it has worked properly
    with open(filename, "r") as final:
        output = final.read()
    return print(output)

merge("file1.txt", "file2.txt", "file3.txt")
