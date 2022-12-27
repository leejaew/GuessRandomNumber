import random

# Generate a random integer from 1 to 10
target = random.randint(1, 10)

# Give the user 3 tries to guess the correct number
for i in range(3):
  guess = int(input("Guess a number from 1 to 10: "))
  if guess == target:
    print("Your guess was correct!")
    break
  elif guess < target:
    print("higher")
  else:
    print("lower")

# If the user did not guess correctly after 3 tries, print "Better luck next time!" and the correct number
if guess != target:
  print("Better luck next time! The correct number was", target)