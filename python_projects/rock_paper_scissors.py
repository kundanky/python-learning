#rock paper scissors game
import random
game = ("rock","paper","scissors")
playing = True
while playing:
	player =""
	computer =random.choice(game)
	while player not in game:
			player =input(f"Enter your choice {game}").lower()
			print("<-------------------->")
			if player  not in game:
				print("invalid input try again")
	if computer == player:
		print("Tied")
	elif player =="rock" and computer =="scissors":
		print("You win")
	elif player == "scissors" and computer == "paper":
			print(" You win")
	elif player == "paper" and computer == "rock":
			print(" You win!")
	else:
			print("You lose!")
	print("<-------------------->")
	print(f"player choice : {player}")
	print(f"computer choice : {computer}")
	print("<-------------------->")
	more =input("Do you like to play more?press yes/no:").lower()
	print()
	if more !="yes":
				playing = False
				print("Thanks for playing!")
				
			
			