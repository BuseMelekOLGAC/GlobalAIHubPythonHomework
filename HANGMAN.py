print("Please enter your name:")
x=input()
print("Hello,"+x)
import random

words = ["corona","lung","pain","hospital","medicine","doctor","ambulance","nurse","intubation"]
word = random.choice(words)
NumberOfPrediction = 10
harfler = []
x = len(word)
z = list('_' * x)
print(' '.join(z), end='\n')
while NumberOfPrediction > 0:
    y = input("Guess a letter:")
    if y in words:
        print("Please don't tell the letter that you've guessed before!")
        continue

    elif len(y) > 1:
        print("Please just enter one letter!!!")
        continue

    elif y not in word:
        NumberOfPrediction -= 1
        print("Misestimation.You have {} prediction justification last!".format(NumberOfPrediction))

    else:
        for i in range(len(word)):
            if y == word[i]:
                print("Correct Guess!")
                z[i] = y
                words.append(y)
        print(' '.join(z), end='\n')
        answer = input("Do you still want to guesss all of the word? ['yes' or 'no'] : ")

        if answer == "yes":
            guess = input("You can guess all of the word then : ")
            if guess == word:
                print("Congrats!You know right!!!")
                break
            else:
                NumberOfPrediction -= 1
                print("Misestimation! You have {} prediction justification last".format(NumberOfPrediction))

        if NumberOfPrediction== 0:
            print("Oh no,you don't have any prediction justification.You lost the game.Your hangman is hanged hahah!")
            break