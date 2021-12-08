import timeit

def input_cleaner(text):
    key = []
    output_numbers = []
    input_list = text.split("\n")
    for line in input_list:
        parts = line.split(" | ")
        key.append(parts[0])
        output_numbers.append(parts[1])
    
    return key, output_numbers

def easy_digits(input):
    easy_digit_count = 0
    for line in input:
        output_numbers = line.split(" ")
        for num in output_numbers:
            if len(num) == 2 or len(num) == 4 or len(num) == 3 or len(num) == 7:
                easy_digit_count += 1
    
    return easy_digit_count

def full_digits(keys, outputs):
    total_count = 0
    for index in range(len(keys)):
        coded_dict = key_generator(keys[index])
        output_numbers = outputs[index].split(" ")
        number_string = ""
        for output in output_numbers:
            char_list = [char for char in output]
            letter = [k for k, v in coded_dict.items() if set(v) == set(char_list)]
            if len(letter) == 1:
                number_string += str(letter[0])
            
        total_count += int(number_string)
        

    return total_count

def pos_finder (keys):
    #starting at the top we visualize each part of the 7 segment
    #   1111
    #  2    3
    #  2    3
    #   4444
    #  5    6
    #  5    6
    #   7777
    # this function works out which letter matches with each number in this configuration using various different methods relating to number distribution
    full_list = keys.split(" ")
    key_dict = {}
    for key in full_list:
        if len(key) == 3:
            seven = [char for char in key]
        if len(key) == 2:
            one = [char for char in key]
        if len(key) == 4:
            four = [char for char in key]
    
    pos = [char for char in seven if char not in one]
    key_dict[1] = pos[0]
    pos2or4 = [char for char in four if char not in one]
    count_dict = {'a':0, 'b': 0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0}
    
    for char in keys:
        if char in count_dict:
            count_dict[char] += 1

    for char in count_dict:
        if count_dict[char] == 6:    
            key_dict[2] = char
        elif count_dict[char] == 9:
            key_dict[6] = char
        elif count_dict[char] == 4:
            key_dict[5] = char
    
    pos = [char for char in pos2or4 if char != key_dict[2]]
    key_dict[4] = pos[0]

    for char in count_dict:
        if count_dict[char] == 7 and char != key_dict[4]:
            key_dict[7] = char
        if count_dict[char] == 8 and char != key_dict[1]: 
            key_dict[3] = char

    
    return key_dict

def key_generator(keys):
    code_dict = {0: [1,2,3,5,6,7], 1: [3,6], 2:[1,3,4,5,7], 3:[1,3,4,6,7], 4:[2,3,4,6], 5:[1,2,4,6,7], 6:[1,2,4,5,6,7], 7:[1,3,6], 8:[1,2,3,4,5,6,7], 9:[1,2,3,4,6,7]}
    key_dict = pos_finder(keys)
    coded_dict = {}
    for i in range(10):
        code_list = []
        for positions in code_dict[i]:
            code_list.append(key_dict[positions])
        coded_dict[i] = code_list

    return coded_dict
  
if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'input8.txt', 'r') as f:
        text = f.read()
    key, output_numbers = input_cleaner(text)
    print(f'Challenge 1 Answer: {easy_digits(output_numbers)}')
    print(f'Challenge 2 Answer: {full_digits(key, output_numbers)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))