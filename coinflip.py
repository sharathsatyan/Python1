import random
print "Now I am going to flip a coin thousand times and check how many times I get head!"
raw_input("Press Any Key")
heads=0
tails=0
flips=0

while flips<1000:
    if random.randint(0,1)==1:
        heads+=1
    else:
        tails+=1
    flips+=1

    if flips==1000:
        print "After 1000 flips we have %d heads and %d tails." %(heads,tails)
    elif flips==500:
        print "Half way through and we have %d heads and %d tails"  %(heads,tails)
    elif flips==100:
        print "After 100 flips we have %d heads and %d tails." %(heads,tails)

raw_input("Was your guess close?")
