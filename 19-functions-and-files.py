from sys import argv

script, inputFile = argv

def printAll(file):
    print file.read()

def rewind(file):
    file.seek(0)

def printLine(line_count, file):
    print line_count, file.readline()

currentFile = open(inputFile)

print "First, we print the whole file:"
printAll(currentFile)

print "Now, we go back to ze beginning"
rewind(currentFile)

print "Then we print three lines:"

line = 1
printLine(line, currentFile)

line += 1
printLine(line, currentFile)

line += 1
printLine(line, currentFile)
