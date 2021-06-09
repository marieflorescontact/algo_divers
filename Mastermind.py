import random

color_list = ["blue", "green", "yellow", "red", "white", "black", "violet", "grey"]

code_maker=[]

while len(code_maker) < 4:
    new_color = random.choice(color_list)
    code_maker.append(new_color)
   
print(code_maker)

def game_loop():
    print("Hi, welcome to Mastermind ! Please write 4 colours and press enter after each one.")

    code_breaker = []
    for i in range(len(code_maker)):
        code_breaker.append(input())


    good_color_good_place = 0
    good_color_bad_place = 0
    final_score = []

    for i in range(len(code_maker)):
        for j in range(len(code_breaker)):
            if code_maker[i] == code_breaker[j] and i == j:
                good_color_good_place += 1
            elif code_maker[i] == code_breaker[j] and i != j:
                good_color_bad_place += 1  

    final_score.append(good_color_good_place)
    final_score.append(good_color_bad_place)
    print(final_score)

game = 0

while game <= 12:
    game_loop()
    game = game + 1