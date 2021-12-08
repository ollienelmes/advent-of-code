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

def full_digit_decoder(key, output_digits):
    output_dig = ""
    #number 0
    if ():
       output_dig += '0' 
    #number 1
    elif len(num) == 2:
        output_dig += '1'
    #number 2
    elif ():
        output_dig += '2'
    #number 3
    elif num == find_three(num):
        output_dig += '3' 
    #number 4
    elif len(num) == 4:
        output_dig += '4' 
    #number 5
    elif len(num) == find_five(num):
        output_dig += '5'
    #number 6
    elif ():
        output_dig += '6'
    #number 7
    elif len(num) == 3:
        output_dig += '7'
    #number 8
    elif len(num) == 7:
        output_dig += '8'
    #number 9
    elif num == find_nine(num):
        output_dig += '9'        
    

    return 
#finds the number 3
def find_three (keys):
    list_of_digs = []
    full_list = keys.split(" ")
    for dig in full_list:
        if len(dig) == 5:
            char_list = []
            for char in dig:
                char_list.append(char)
            list_of_digs.append(char_list)
    
    for char in list_of_digs[0]:       
        if char in list(set(list_of_digs[1]) | set(list_of_digs[2])):
            three = list_of_digs[0]
            break
    for char in list_of_digs[1]:       
        if char in list(set(list_of_digs[0]) | set(list_of_digs[2])):
            three = list_of_digs[1]
            break
    for char in list_of_digs[2]:       
        if char in list(set(list_of_digs[1]) | set(list_of_digs[0])):
            three = list_of_digs[2]
            break
    return "".join(three)

def pos_finder (keys):
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
    code_dict = {0: [1,2,3,5,6,7], 1: [3,6], 2:[1,3,4,5,7], 3:[1,3,4,6,7], 4:[2,3,4,6], 5:[1,2,4,6,7], 6:[1,2,5,6,7], 7:[1,3,6], 8:[1,2,3,4,5,6,7], 9:[1,2,3,4,6,7]}
    key_dict = pos_finder(keys)
    coded_dict = {}
    for i in range(9):
        code_list = []
        for positions in code_dict[i]:
            code_list.append(key_dict[positions])
        coded_dict[i] = code_list
    
    return coded_dict

key_generator('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab')

def find_nine (keys):
    full_list = keys.split(" ")
    list_of_nine = []
    for key in full_list:
        if len(key) == 4:
            for char in key:
                list_of_nine.append(char)
    
    key_dict = pos1_7(keys)
    
    list_of_nine.append(key_dict[1])
    list_of_nine.append(key_dict[7])
    # number 9 is not 4 union 1, I'm going to need to work out the chars for 1 and 7 and then add that to the chars in set 4
    
    set_of_nine = set(list_of_nine)
    print(list_of_nine)
    for key in full_list:
        temp_list = []
        for char in key:
            temp_list.append(key)
        if set(temp_list) == set(set_of_nine):
            return "".join(temp_list)

find_nine('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab')


def find_five(keys):
    full_list = keys.split(" ")
    five_long_list = []
    six_long_list = []
    for key in full_list:
        temp_list = []
        if len(key) == 5:
            if key != find_three(keys):
                for char in key:
                    temp_list.append(char)
            five_long_list.append(temp_list)
        if len(key) == 6:
            print(find_nine(keys))
            if key != find_nine(keys):
                for char in key:
                    temp_list.append(char) 
            six_long_list.append(temp_list)
    
    print(five_long_list)
    print(six_long_list)
            
#find_five('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab')

def full_digit(output, keys):
    total_count = 0
    for index in range(len(output)):
        output_numbers = output[index].split(" ")
        for num in output_numbers:
            output_string = ""
            if len(num) == 2:
                output_string += '1'
            elif len(num) == 4:
                output_string += '4'
            elif len(num) == 3:
                output_string += '7'
            elif len(num) == 7:
                output_string += '8'
            elif len(num) == 5:
                key = keys[index].split(" ")
                if num == find_three(key):
                    output_string += '3'
            elif len(num) == 6:
                key = keys[index].split(" ")
                if num == find_nine(key):
                    output_string += '9'
            total_count += int(output_string)
    
    return easy_digit_count
    
if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'input8.txt', 'r') as f:
        text = f.read()
    key, output_numbers = input_cleaner(text)
    print(f'Challenge 1 Answer: {easy_digits(output_numbers)}')
    #print(f'Challenge 2 Answer: {challenge_2(input)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))