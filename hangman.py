import random
import re

def diag(num):
    if num==1:
        print ("           ---------------|")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("    H                     |")
        print ("--------------------------|")
    if num==2:
        print ("           ---------------|")
        print ("           |              |")
        print ("          * *             |")
        print ("        *     *           |")
        print ("          * *             |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("                          |")
        print ("    HA                    |")
        print ("--------------------------|")
    elif num==3:
        print ("           ---------------|")
        print ("           |              |")
        print ("          * *             |")
        print ("        *     *           |")
        print ("          * *             |")
        print ("           |              |")
        print ("           |              |")
        print ("           |              |")
        print ("           |              |")
        print ("           |              |")
        print ("           |              |")
        print ("           |              |")
        print ("                          |")
        print ("                          |")
        print ("    HAN                   |")
        print ("--------------------------|")
    elif num==4:
        print ("           ---------------|")
        print ("           |              |")
        print ("          * *             |")
        print ("        *     *           |")
        print ("          * *             |")
        print ("           |              |")
        print ("           |              |")
        print ("           | *            |")
        print ("           |   *          |")
        print ("           |              |")
        print ("           |              |")
        print ("           |              |")
        print ("                          |")
        print ("    HANG                  |")
        print ("--------------------------|")
    elif num==5:
         print ("           ---------------|")
         print ("           |              |")
         print ("          * *             |")
         print ("        *     *           |")
         print ("          * *             |")
         print ("           |              |")
         print ("           |              |")
         print ("         * | *            |")
         print ("       *   |   *          |")
         print ("           |              |")
         print ("           |              |")
         print ("                          |")
         print ("                          |")
         print ("    HANGM                 |")
         print ("--------------------------|")
    elif num==6:
         print ("           ---------------|")
         print ("           |              |")
         print ("          * *             |")
         print ("        *     *           |")
         print ("          * *             |")
         print ("           |              |")
         print ("           |              |")
         print ("         * | *            |")
         print ("       *   |   *          |")
         print ("           |              |")
         print ("           |              |")
         print ("             *            |")
         print ("               *          |")
         print ("    HANGMA                |")
         print ("--------------------------|")
    elif num==7:
         print ("           ---------------|")
         print ("           |              |")
         print ("          * *             |")
         print ("        *     *           |")
         print ("          * *             |")
         print ("           |              |")
         print ("           |              |")
         print ("         * | *            |")
         print ("       *   |   *          |")
         print ("           |              |")
         print ("           |              |")
         print ("         *   *            |")
         print ("       *       *          |")
         print ("        HANGMAN!          |")
         print ("--------------------------|")

WORDS = open('words.txt', 'r' )
read_word = WORDS.read()


list_of_words = [word for word in read_word.split() if len(word) >= 3]

hangword = random.choice(list_of_words)
print (hangword)
fail_iteration = 0
print ("The word has %d alphabets" %len(hangword))
test= [ '_' ] * len(hangword)
print (test)
used = []
#test1 = list(test)
flag=0


while (fail_iteration <7):

    guessed_alphabet = input(str("Please guess one of the alphabet : "))
    k=0
    for i in range(len(hangword)):
        if hangword[i] == guessed_alphabet:
            test[i] = guessed_alphabet
            k= 1
    if k==0:
        fail_iteration+=1
        print (diag(fail_iteration))
        used.append(guessed_alphabet)
        print ("You have used", used)
        print ("You have %d tries left" %(8-fail_iteration))
    guessed_word = "".join(test)

    if guessed_word == hangword :
        print ("Congratulations!")

        flag = 1
        break
    print (" ".join(test))

if flag !=1:
    print ("It was %s" %hangword)
    print ("Better luck next time!")


    #break
    #print test
#"".join(s)
