#number guessing game
import random
low = 1
high = 100
guesses = 0
answer = random.randint(low,high)

while True:
	guess = input(f"guess a number between {low} and {high}:")
	if guess.isdigit():
		guess = int(guess)
		guesses += 1
		if guess <low or guess >high:
			print("out of range")
			print(f"please guess a number between {low} and {high}: ")
			continue
		if guess < answer :
			print("too low")
			print("Try again")
		elif guess > answer:
			print("too high")
			print("Try again")
		elif guess == answer:
			print(f"Awesome! the answer was {answer}:")
			break
	else:
		print("invalid guess")
		print(f"please guess a number between {low} and {high}:")
print(f"You guessed the answer in {guesses} tries")