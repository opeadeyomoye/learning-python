from sys import argv

script, filename = argv

fh = open(filename)

print "Here's your file: %r" % filename
print fh.read()

print "Try another file:"
anotherFile = raw_input('> ')

fh = open(anotherFile)
print fh.read()

fh.close()
