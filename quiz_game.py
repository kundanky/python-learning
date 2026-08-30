#quiz game 
print("QUIZ GAME")
questions = ("How many elements are there in periodic table?","Best aimer in valorant?","Best player in CS2?","Best Player in CODM? ")

options = (("A.119","B.117","C.118","D.121"), ("A.Demon1","B.Something","C.Kr1stal","D.Primmie"), ("A.Zywoo","B.Donk","C.Monesy","D.S1mple"), ("A.Tectonic","B.Abhiz","C.Zai","D.Ouling"))
answers = ("C","A","B","C")
guesses =[]
score = 0
question_num= 0
for question in questions:
	print("--- ")
	print(question)
	for option in options[question_num]:
		print(option)
	guess = input("Enter your guess (A,B,C,D):").upper()
	guesses.append(guess)
	if guess == answers[question_num]:
		score += 1
		print("correct!")
	else:
		print("incorrect!")
		print(f"correct answer is:{answers[question_num]}") 
	print("Your guess:",guess)
	print()
	question_num += 1
	total = int((score / question_num)*100)
print(f"You total score is:{score}/{question_num} = {total}%")
print("Your Guesses↓")
print(" ".join(guesses))
print("<----->")