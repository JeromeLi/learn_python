import random

secret_num = random.randint(1, 10)
i = 1
while i <= 3:
	print('-----------------------')
	temp = input('Guess a number:')
	guess = int(temp)
	if guess == secret_num:
		print('Bingo! You are right!')
		print(':\)')
		break
	else:
		if guess <= secret_num:
			print('Too small!')
		else:
			print('Too large!')
	i = i + 1
	if i == 3:
		print('Last Chance!')
	else:
		continue
print('Game over!')
