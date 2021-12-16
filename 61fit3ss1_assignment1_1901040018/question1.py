import random

print("I have a secret number in 1 to 100!")

lower = 1

upper = 100


x = random.randint(lower, upper)


count = 0

while True:
	count += 1
	guess = int(input("Guess a number (enter 0 to quit): "))

	if x == guess:
		print("Congratulations you did it in "+str(count)+ " try")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You guessed too high!")
	if guess == 0:
		print("The number is %d" % x)
		print("Better Luck Next time!")
		break


