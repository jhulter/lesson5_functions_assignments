# Task 1

questions = ["10 - 3? ", " 5 x 5? ", "300 - 200? ", "800 - 222? ", "2 + 3? ", "8 / 1? "]
answers = ["7", "25", "100", "578", "5", "8"]


# Task 2

def play_quiz():
    for q in questions:
        score = 0
        answer = input(questions[0])
        if answer == answers[0]:
            score += 1
            print("correct!")
        else:
            print("wrong!")
        answer = input(questions[1])
        if answer == answers[1]:
            score += 1
            print("correct!")
        else:
            print("wrong!")
        answer = input(questions[2])
        if answer == answers[2]:
            score += 1
            print("correct!")
        else:
            print("wrong!")
        answer = input(questions[3])
        if answer == answers[3]:
            score += 1
            print("correct!")
        else:
            print("wrong!")
        answer = input(questions[4])
        if answer == answers[4]:
            score += 1
            print("correct!")
        else:
            print("wrong!")
        answer = input(questions[5])
        if answer == answers[5]:
            score += 1
            print("correct!")
        else:
            print("wrong!")
        break
        # Task 3
    print(f"Your score is {score}")
play_quiz()



