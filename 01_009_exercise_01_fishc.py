for narcissistic_number in range(100, 1000):
    sum_0 = 0
    for i in str(narcissistic_number):
        sum_0 += int(i) ** 3
    if narcissistic_number == sum_0:
        print('found:', narcissistic_number)
