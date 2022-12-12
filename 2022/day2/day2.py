import timeit

def input_cleaner(text):
    lines = text.split('\n')

    return lines

def score_calculator(lines):
    choice_points = 0
    result_points = 0
    for line in lines:
        if 'X' in line:
            #Rock Selected (A)
            choice_points += 1
        elif 'Y' in line:
            #Paper Selected (B)
            choice_points += 2
        elif 'Z' in line:
            #Scissors Selected (C)
            choice_points += 3

        #ROCK
        if 'A' in line:
            if 'X' in line:
                #Draw
                result_points += 3
            elif 'Y' in line:
                #Win
                result_points += 6
            elif 'Z' in line:
                #Loss
                result_points += 0
        #PAPER
        elif 'B' in line:
            if 'X' in line: 
                #Loss
                result_points += 0
            elif 'Y' in line:
                #Draw
                result_points += 3
            elif 'Z' in line:
                #Win
                result_points += 6
        #SCISSORS        
        elif 'C' in line:
            if 'X' in line:
                #Win
                result_points += 6
            elif 'Y' in line:
                #Loss
                result_points += 0
            elif 'Z' in line:
                #Draw
                result_points += 3
    
    return choice_points + result_points

def correct_score_calculator(lines):
    choice_points = 0
    result_points = 0
    for line in lines:
        if 'X' in line:
            #loss
            result_points += 0
        elif 'Y' in line:
            #Draw
            result_points += 3
        elif 'Z' in line:
            #win
            result_points += 6

        #ROCK
        if 'A' in line:
            if 'X' in line:
                #loss scissors
                choice_points += 3
            elif 'Y' in line:
                #draw rock
                choice_points += 1
            elif 'Z' in line:
                #win paper
                choice_points += 2
        #PAPER
        elif 'B' in line:
            if 'X' in line: 
                #Loss rock
                choice_points += 1
            elif 'Y' in line:
                #Draw
                choice_points += 2
            elif 'Z' in line:
                #Win
                choice_points += 3
        #SCISSORS        
        elif 'C' in line:
            if 'X' in line:
                #loss
                choice_points += 2
            elif 'Y' in line:
                #draw
                choice_points += 3
            elif 'Z' in line:
                #win
                choice_points += 1
    
    return choice_points + result_points

    




if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'/Users/godfreynelmes/Documents/GitHub/advent-of-code/2022/day2/input2.txt', 'r') as f:
        text = f.read()
    lines = input_cleaner(text)
    print(f'Challenge 1 Answer: {score_calculator(lines)}')
    print(f'Challenge 2 Answer: {correct_score_calculator(lines)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))