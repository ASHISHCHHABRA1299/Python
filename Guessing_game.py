import random

random_number = random.randint(1,10)
number = None
while number != random_number:		
	number = input("GUESS A NUMBER ")
	number = int(number)
	if number < random_number:
		print("Too Low,try Again")
	elif number > random_number:
		print("Too High,try Again")
	else:
		print(" CORRECT CHOICE.YOU WON!")
print(random_number)		