i = 0
inc = 2
numbers = []

def increment(num,i):
    print "At the top i is %d" %num
    numbers.append(num)

    num+=i
    print "Numbers now:" , numbers
    print "At the bottom i is %d" %num
    return num

while i < 6:
    i=increment(i,inc)


print "The numbers:"

for num in numbers:
    print num
