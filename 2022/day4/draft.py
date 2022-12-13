import timeit

def input_cleaner(text):
    lines = text.split('\n')

    return lines

def range_calc(lines):
    count = 0
    
    for line in lines:
        range1, range2 = line.split(',')
        range1n1, range1n2 = range1.split('-')
        range2n1, range2n2 = range2.split('-')
        
        if range1n1 != range1n2:
            list1 = list(range(int(range1n1),(int(range1n2)+1)))
        else:
            list1 = [range1n1]

        if range2n1 != range2n2:
            list2 = list(range(int(range2n1),(int(range2n2)+1)))
        else:
            list2 = [range2n1]

        set1 = set(list1)
        set2 = set(list2)
        if (set1 & set2):
            count += 1

            

    return count

if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'/Users/godfreynelmes/Documents/GitHub/advent-of-code/2022/day4/input4.txt', 'r') as f:
        text = f.read()
    lines = input_cleaner(text)
    print(f'Challenge 1 Answer: {range_calc(lines)}')
    #print(f'Challenge 2 Answer: {three_group(lines)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))