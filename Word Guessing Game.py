import random
""" 
"RANDOM" module has been used in this code.
 This module is used to generate random elements from the given list (HERE IT IS WORDS)
""" 

name = input("Your good name please!!! ")
# Here the user is asked to enter the name first
# 'input()' function allows the user to insert data (numbers, words, symbols etc.) into a program

print("Wish You Good Luck , Mi Amigo! ", name)

words = ['macintosh', 'catastrophe', 'ballistics', 'microsoft', 'butler','kerosene',
         'android','lethargy','saponification','kebab','chicken','integration',
         'botany','pluviophile','calligraphy','season','trauma','pendulum',
         'crankshaft','turbocharger','photography','minecraft','introvert','corpuscle',
		 'integrals','denounce','zoology','autumn','spring','exploratory',
		 'quantum','fascist','passive','mythology','fortress','lethargy',
		 'guerrilla','antelope','amnesia','vocabulary','mystical','overshine',
		 'criminal','tarnish','tungsten','coding','brainstorming','symphony']

# RANDOM function selects a word in random
# from the specified list (HERE IT IS WORDS) 

word = random.choice(words)


print("Guess the alphabets! Try to win, IF YOU'RE SMART ! ")

guesses = ''

# any number of turns can be specified by the programmer 
turns = 16


while turns > 0:
	
	# counts the number of times the user failed to guess the character (alphabet)
	failed = 0
	
	#  all characters from the input
	#  word are taken one at a time.
	for char in word:
		
		# This compares the character given by the user  
		# with the character from the word  
		if char in guesses:
			print(char)
			
		else:
			print("_")
			
			# for every failed attempt 1 will be
			# incremented in failure
			failed += 1
			

	if failed == 0:
		# user wins the game when the number of failed attempts is 0
		# and the following statement is given as output
		print("YAY! You're indeed SMART!")
		
		# The correct word is displayed
		print("The word is: ", word)
		break
	
	# When the user gives a wrong alphabet as an input
	# it will ask the user to enter another alphabet
	guess = input("Give It Another Shot:")
	
	# the input character given by the user will be stored in guesses 
	guesses += guess
	
	# verifies the character given by the user with the character from the word selected at random
	if guess not in word:
		
		turns -= 1
		
		# When the character given by the user does not match with the character from the word		
		# then “Wrong” will be given as output
		print("OOPS! missed the target, TRY AGAIN!")
		
		# This will print the number of
		# turns left for the user to guess the word
		print("KEEP GOING! you have", + turns, "more guesses")
		
		#If user ran out of guesses/turns
		#"YOU LOSE" will be printed
		if turns == 0:
			print("Don't give up! BETTER LUCK NEXT TIME..... ")