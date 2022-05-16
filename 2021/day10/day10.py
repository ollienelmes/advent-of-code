import timeit

def input_cleaner(text):
    lines = text.split("\n")

    return lines

def illegal_check(lines):
    point_counter = 0
    opening_list = ['{','[','(','<']
    illegal_chars = []
    for line in lines:
        #print(f'starting line: {line}')
        while '()' in line or '[]' in line or '<>' in line or '{}' in line:
            line2 = line.replace("()","").replace("[]","").replace("<>","").replace("{}","")
            line = line2

        for char in line:
            if char not in opening_list:
                illegal_chars.append(char)
                break

    
    for char in illegal_chars:
        if char == ')':
            point_counter += 3
        elif char == ']':
            point_counter += 57
        elif char == '}':
            point_counter += 1197
        elif char == '>':
            point_counter += 25137

    return point_counter

def incomplete_lines(lines):
    point_counter = []
    opening_list = ['{','[','(','<']
    incomplete_lines = []
    
    for line in lines:
        #print(f'starting line: {line}')
        while '()' in line or '[]' in line or '<>' in line or '{}' in line:
            line2 = line.replace("()","").replace("[]","").replace("<>","").replace("{}","")
            line = line2
            set_of_chars = set([char for char in line2])
            #print(set_of_chars)
            if set_of_chars <= set(opening_list):
                incomplete_lines.append(line2)

    for line in incomplete_lines:
        points = 0

        for char in line[::-1]:
            if char == '(':
                points = points * 5
                points += 1
            elif char == '[':
                points = points * 5
                points += 2
            elif char == '{':
                points = points * 5
                points += 3
            elif char == '<':
                points = points * 5
                points += 4


        point_counter.append(points)
    
    point_counter.sort()
    
    index_val = (len(point_counter)-1)/2
    return point_counter[int(index_val)]

if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'input10.txt', 'r') as f:
        text = f.read()
    lines = input_cleaner(text)
    print(f'Challenge 1 Answer: {illegal_check(lines)}')
    print(f'Challenge 2 Answer: {incomplete_lines(lines)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))