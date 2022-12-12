import timeit
import string

def input_cleaner(text):
    lines = text.split('\n')

    return lines

def alphabet_dict():
    alphabet = list(string.ascii_letters)
    dict = {}
    counter = 1
    for letter in alphabet:
        dict[letter] = counter
        counter += 1
    
    return dict

def sum_calculator(lines):
    total = 0
    dict = alphabet_dict()
    for line in lines:
        common_letter = ''
        length = len(line)
        point1 = int(length/2)
        word1 = line[0:point1]
        word2 = line[point1:]

        for letter in word1:
            if letter in word2:
                common_letter = letter
        
        total += int(dict[common_letter])

    return total

def three_group(lines):
    counter = 0
    new_list = []
    new_line = ''
    for line in lines:
        if counter < 3:
            new_line += line
            new_line += '\n'
            counter += 1
        elif counter == 3:
            new_list.append(new_line)
            new_line = ''
            new_line += line
            new_line += '\n'
            counter = 1
    
    new_list.append(new_line)
    
    total = 0
    common_letter = ''
    dict = alphabet_dict()
    for line in new_list:
        word1, word2, word3, blank = line.split('\n')
        for letter in word1:
            if letter in word2 and letter in word3:
                common_letter = letter
        
        total += int(dict[common_letter])

    return total

if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'/Users/godfreynelmes/Documents/GitHub/advent-of-code/2022/day3/input3.txt', 'r') as f:
        text = f.read()
    lines = input_cleaner(text)
    print(f'Challenge 1 Answer: {sum_calculator(lines)}')
    print(f'Challenge 2 Answer: {three_group(lines)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))