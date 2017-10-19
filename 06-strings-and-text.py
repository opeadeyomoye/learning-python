##########

x = "There are %d types of people" % 10
binary = "binary"
doNot = "don't"

y = "Those who know %s and those who %s." % (binary, doNot)

print x; print
print y; print

print "I said: %r" % x
print "I also said: '%s'." % y
print

hilarious = False
joke_evaluation = "Isn't that joke just so funny? %r"

print joke_evaluation % hilarious

w = 'This is the left side of a string ...'
e = 'with a right side'

print w + e
print w, e

