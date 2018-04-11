the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print "This is the count %d" %number

for fruit in fruits:
    print "A type of fruit is %s" %fruit

for i in change:
    print "I got %r" %i

elements = []

for i in range (0,6):
    print "Adding %d to the list" %i
    #append is a function that lists understand
    elements.append(i)

# printing them out
for i in elements:
    print "Element was: %d" %i
