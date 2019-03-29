while True:
    exam_score = input('Input score:')
    if exam_score.isdigit() and 0 <= int(exam_score) <= 100:
        score_int = int(exam_score)
        break
    else:
        print('Please input correct number!')
if 60 <= score_int < 80:
    print('C')
elif score_int >= 90:
    print('A')
elif 80 <= score_int < 90:
    print('B')
else:
    print('D')
