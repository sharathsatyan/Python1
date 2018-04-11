from sys import argv
script, filename = argv

print "We're going to erase %r" %filename
print "If you don't want that, hit CTRL-C (^C) "
print "If you do want this, hit return"

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "truncating the file, Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1:\n")
line2 = raw_input("line2:\n")
line3 = raw_input("line3:\n")

print "I'm going to write these lines to the file."

target.write(line1)
target.write(line2)
target.write(line3)

print "And finally, we closed it."

target.close()
