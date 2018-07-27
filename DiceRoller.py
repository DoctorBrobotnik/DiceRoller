import random
import sys

def rollDice():
	print('What sided dice should I roll?')

	dice = input()
	try:
		dice = int(dice)
		pass
	except ValueError:
		print('Please enter in a valid number!')
		print('')
		return rollDice()

	print('')
	print('Rolling a d' + str(dice))

	diceRoll = random.randint(1,int(dice))

	print('')
	print('You rolled ' + str(diceRoll))
		
	if diceRoll == 20:
		print('Critical Success!')
	elif (int(dice) == 20 and diceRoll == 1):
		print('Critical Failure!')

def reRoll():
	print('')
	choice = input('Roll another? Y/N: ')
	try:
		if choice.lower() == 'y':
			print('')
			return True
		elif choice.lower() == 'n':
			print('Goodbye!')
			sys.exit()
		else:
			print('')
			print('Please choose Y or N.')
		return reRoll()
	except Exception as error:
		print('Please enter a valid input')
		print(error)
		return reRoll()

while True:
	rollDice()
	reRoll()
