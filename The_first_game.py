import random

secret_num = random.randint(1, 10)
i = 1
while i <= 3:
	print('-----------------------')

	if i == 3:
		print('Last Chance!')
	elif i == 2:
		print('Second time!')
	elif i == 1:
		print('First time!')
	else:
		continue
	while True:
		temp = input('Guess a number:')
		if temp.isdigit():
			break
		else:
			print('Input Error!')
	guess = int(temp)
	if guess == secret_num:
		print('Bingo! You are right!')
		print(':\)')
		break
	else:
		if guess < secret_num:
			print('Too small!')
		else:
			print('Too large!')
	i = i + 1
print('Game over!')
