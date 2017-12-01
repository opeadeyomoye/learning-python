from sys import argv
from os import path

script, source, destination = argv

print "Copying fron %s to %s" % (source, destination)

data = open(source).read()

print "The input file is %d bytes long" % (len(data))
print "Does the destination file exist? %r" % (path.exists(destination))
print "Ready? Hit RETURN. Or hit Ctrl+C to cancel"
raw_input('> ')

open(destination, 'w').write(data)
print "Alright, done."
