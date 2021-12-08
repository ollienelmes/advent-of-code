import timeit

def input_cleaner(text):
    input_list = text.split(",")
    map_object = map(int, input_list)
    list_of_integers = list(map_object)
    return list_of_integers

def challenge_1(input):
    set_of_pos = set(input)
    fuel_dict = {}
    for num in set_of_pos:
        fuel_dict[num] = 0

    for index in fuel_dict:
        for num in input:
            fuel_dict[index] += abs(index-num) 

    least_fuel_key = min(fuel_dict, key=fuel_dict.get)

    return fuel_dict[least_fuel_key]

def challenge_2(input):
    set_of_pos = set(input)
    fuel_dict = {}
    for num in range(max(set_of_pos)):
        fuel_dict[num] = 0

    for index in fuel_dict:
        for num in input:
            fuel_dict[index] += new_fuel_val(abs(index-num))
            

    least_fuel_key = min(fuel_dict, key=fuel_dict.get)
    
    return fuel_dict[least_fuel_key]

def new_fuel_val (num):
    running_total = 0
    for step in range(1, num+1):
        running_total += step
    
    return running_total



if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'input7.txt', 'r') as f:
        text = f.read()
    input = input_cleaner(text)
    print(f'Challenge 1 Answer: {challenge_1(input)}')
    print(f'Challenge 2 Answer: {challenge_2(input)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))