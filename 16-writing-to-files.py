from sys import argv

script, filename = argv

print "We're going to empty %r" % filename
print "If you don't want that, hit Ctrl+C (^C)"
print "If you DO wan't that, hit RETURN (Enter)"

raw_input('? ')

print "Opening the file..."
File = open(filename, 'w')

print "Emptying the file..."
File.truncate()

print "Enter three lines you want us to write to the now empty file:"
line1 = raw_input('Line 1: ')
line2 = raw_input('Line 2: ')
line3 = raw_input('Line 3: ')

print "Writing to the file..."
text = "%s\n%s\n%s" % (line1, line2, line3)
File.write(text)
print "Write complete!"

File.close()
