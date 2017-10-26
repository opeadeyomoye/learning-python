
def unpackAndPrint(*vars):
    var1, var2 = vars
    print "var1: %r, var2: %r" % (var1, var2)

def printTwo(var1, var2):
    print "var1: %r, var2: %r" % (var1, var2)

def printOne(one):
    print "Ze var: %r" % (one)

def printNone():
    print "I don't gat squat man"

unpackAndPrint("Ope", "Adeyomoye")
printTwo("Ope", "Adeyomoye")
printOne("First!")
printNone()

# this should cause an error
#unpackAndPrint("just one arg")