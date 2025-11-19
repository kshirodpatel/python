import random
import time

OPEARTORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPEARND = 12
TOTAL_QUESTIONS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPEARND)
    right = random.randint(MIN_OPERAND, MAX_OPEARND)
    opeartor = random.choice(OPEARTORS)

    expression = str(left) + " " + str(opeartor) + " "  + str(right)
    answer = eval(expression)
    return expression, answer

wrong = 0
right = 0
input('Press enter to start the game')
print('-----------------------------')
   
start_time = time.time()
for i in range(TOTAL_QUESTIONS):
    expression, answer = generate_problem()

    while True:
        guess = input("Problem #" + str(i +1) + ": " + expression + " = ")
        if guess == str(answer):
            right += 1
            break
        else:
            wrong += 1
            break
    end_time = time.time()
print('---------------------------------------------')
total_time = round(end_time - start_time, 2)
print("You have total wrong answers",wrong, " and right answers", right, "total time you took is", total_time, "in seconds")
