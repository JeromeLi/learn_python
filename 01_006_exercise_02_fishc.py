step_length = 0
while step_length <= 1000:
    if (step_length % 2 == 1) and (step_length % 3 == 2) and (step_length % 5 == 4) \
       and (step_length % 6 == 5):
        print(step_length)
        break
    step_length += 7
