import timeit

def input_cleaner(text):
    lines = text.split('\n')

    return lines

def calorie_counter(lines):
    running_count = 0
    count_list = []
    for line in lines:
        if line != "":
            running_count += int(line)
        else:
            count_list.append(running_count)
            running_count = 0
    
    count_list.sort(reverse=True)

    return max(count_list), sum(count_list[0:3])


if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'/Users/godfreynelmes/Documents/GitHub/advent-of-code/2022/day1/input1.txt', 'r') as f:
        text = f.read()
    lines = input_cleaner(text)
    print(f'Challenge 1 Answer: {calorie_counter(lines)[0]}')
    print(f'Challenge 2 Answer: {calorie_counter(lines)[1]}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))