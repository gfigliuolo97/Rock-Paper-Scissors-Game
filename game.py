import random
choices = ['rock', 'scissors', 'paper','0']
exitGame = False
while(exitGame == False):
	computer_choice = random.choice(choices)
	user_choice = None
	while user_choice == None:
		print("\n############# ROCK PAPER SCISSORS ###########")
		print("## TYPE 'rock', 'paper', 'scissors' OR '0' TO EXIT ###########")
		
		user_choice = input("Make your choice:")
		if user_choice not in choices:
			user_choice = None
	if(user_choice == computer_choice):
		print("Draw")
	elif user_choice == 'paper':
		if computer_choice == 'scissors':
			print("Computer chose scissors")
			print("Computer Wins!")
		elif computer_choice == 'rock':
			print("Computer chose rock")
			print("+++ You Win +++")

	elif user_choice == 'rock':
		if computer_choice == 'paper':
			print("Computer chose paper")
			print("Computer Wins!")
		elif computer_choice == 'scissors':
			print("Computer chose scissors")
			print("+++ You Win +++")

	elif user_choice == 'scissors':
		if computer_choice == 'rock':
			print("Computer chose rock")
			print("Computer Wins!")
		elif computer_choice == 'paper':
			print("Computer chose paper")
			print("+++ You Win +++")
	elif user_choice == '0':
		exitGame = True
		user_choice = None
		print("Bye!")
