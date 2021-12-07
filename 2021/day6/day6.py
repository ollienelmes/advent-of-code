import timeit
import math

def input_cleaner(text):
    input_list = text.split(",")
    map_object = map(int, input_list)
    list_of_integers = list(map_object)
    return list_of_integers

def challenge_1(input_list):
    growth_dict = {}
    day_limit = 81
    day = 0
    new_list = input_list
    while day < day_limit:
        growth_dict[day] = len(new_list)
        input_list = new_list
        new_list = []
        for fish in input_list:
            if fish > 0:
                fish -= 1
                new_list.append(fish)
            else:
                fish = 6
                new_list.append(fish)
                new_list.append(8)
        day += 1
        #print(new_list)

    return len(input_list)

def dict_method(input):
    vector_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for i in input:
        vector_dict[i] += 1
    day = 0
    while day < 256:
        new_dict = {}
        for index in range (1,9):
            new_dict[index-1] = vector_dict[index]
        new_dict[6] += vector_dict[0]
        new_dict[8] = vector_dict[0]
        vector_dict = new_dict
        day +=1

    pop_count = 0
    for index in range (0,9):
        pop_count+= vector_dict[index]
    return pop_count



        


if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'input6.txt', 'r') as f:
        text = f.read()
    input = input_cleaner(text)
    #input = [3,4,3,1,2]
    #challenge_1_answer, growth_dict = challenge_1(input)
    print(f'Challenge 1 Answer: {challenge_1(input)}')
    print(f'Challenge 2 Answer: {dict_method(input)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
    #print(growth_dict)