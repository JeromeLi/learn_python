line_no = 1
for red_ball in range(0, 4):
    for yellow_ball in range(0, 4):
        for green_ball in range(2, 7):
            if red_ball + yellow_ball + green_ball == 8:
                print(line_no, ' ', 'red_ball:', red_ball, 'yellow_ball:', yellow_ball, 'green_ball:', green_ball)
                line_no += 1
