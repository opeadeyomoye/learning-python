from sys import argv

script, username = argv
prompt = '> '

print "Hi %s! I'm the %s script" % (username, "ex-14")
print "I'd like to ask a few questions.", "Here we go:"

print "%s, do you like me?" % username
like = raw_input(prompt)

print "Where do you live %s"% username
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me,
you live in %r, and you have a %r computer. Nice!
""" % (like, lives, computer)
