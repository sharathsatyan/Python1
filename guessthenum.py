import random

guessesTaken = 0
print "Hello! What is your name?"
myName = raw_input(">")

number = random.randint(1,20)
print "Well %s, I am thinking of a number between 1 to 20" %myName
print "Try to guess that number!"

while guessesTaken < 6:

    while True:

        try:
            guess = int(raw_input("Take a guess!\n>>"))
            break
        except:
            print "Please input an integer value."


    guessesTaken += 1

    if guess < number:
        print "Your number is too low."
    elif guess > number:
        print "Your number is too high."
    elif guess == number:
        break

if guess == number:
    print "Good job, %s! You guessed my number in %d guesses!" %(myName,guessesTaken)

if guess != number:
    print "Nope. The number I was thinking of was %d" %number
