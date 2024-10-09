import random

guessesTaken = 0

print('Hello what is your name?')
myName = input()

number = random.randint(1, 100)
print('Well ' + myName + ' i am thinking of a number 1 and 100')

while guessesTaken < 6:
  print('Take a guess: ')
  requestInput = input()
  requestInput = int(requestInput)
 
  guessesTaken = guessesTaken + 1
  if requestInput == number:
         break
  if requestInput < number:
     print('Number is too low')

if requestInput > number:
     print('NUmber is too high')


if requestInput == number:
    guessesTaken = str(guessesTaken)

    print('Good job,' + myName + '! You guessed my number in ' + guessesTaken + ' guesses')


    if requestInput != number:
        number = str(number)
        print('Nope. The number i was thinking of was '+ number)