import timeit
import re

def input_cleaner(text):
    lines = text.split('\n')

    return lines

def crate_vector(lines):
    crate1 = ['B','W','N']
    crate2 = ['L','Z','S','P','T','D','M','B']
    crate3 = ['Q','H','Z','W','R']
    crate4 = ['W','D','V','J','Z','R']
    crate5 = ['S','H','M','B']
    crate6 = ['L','G','N','J','H','V','P','B']
    crate7 = ['J','Q','Z','F','H','D','L','S']
    crate8 = ['W','S','F','J','G','Q','B']
    crate9 = ['Z','W','M','S','C','D','J']

    yard = [crate1,crate2,crate3,crate4,crate5,crate6,crate7,crate8,crate9]

    for line in lines:
        iterator = int(re.search(r'move ([0-9]+) from', line).group(1))
        start = int(re.search(r'from ([0-9]+) to', line).group(1))
        end = int(re.search(r'to ([0-9]+)', line).group(1))

        while (iterator > 0):
            yard[end-1].append(yard[start-1].pop())
            iterator -= 1
    
    output = ''
    for crate in yard:
        output += crate.pop()

    return output

def new_crate_vector(lines):
    crate1 = ['B','W','N']
    crate2 = ['L','Z','S','P','T','D','M','B']
    crate3 = ['Q','H','Z','W','R']
    crate4 = ['W','D','V','J','Z','R']
    crate5 = ['S','H','M','B']
    crate6 = ['L','G','N','J','H','V','P','B']
    crate7 = ['J','Q','Z','F','H','D','L','S']
    crate8 = ['W','S','F','J','G','Q','B']
    crate9 = ['Z','W','M','S','C','D','J']

    yard = [crate1,crate2,crate3,crate4,crate5,crate6,crate7,crate8,crate9]

    for line in lines:
        iterator = int(re.search(r'move ([0-9]+) from', line).group(1))
        start = int(re.search(r'from ([0-9]+) to', line).group(1))
        end = int(re.search(r'to ([0-9]+)', line).group(1))

        yard[end-1].extend(yard[start-1][len(yard[start-1])-iterator:])
        del yard[start-1][len(yard[start-1])-iterator:]
    
    output = ''
    for crate in yard:
        output += crate.pop()

    return output

if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'/Users/godfreynelmes/Documents/GitHub/advent-of-code/2022/day5/input5.txt', 'r') as f:
        text = f.read()
    lines = input_cleaner(text)
    print(f'Challenge 1 Answer: {crate_vector(lines)}')
    print(f'Challenge 2 Answer: {new_crate_vector(lines)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))