import timeit

def position_calc(command_list):

    depth_pos = 0
    horizontal_pos = 0

    for x in command_list:
        if 'forward' in x:
            horizontal_pos += int(x[-1])
        elif 'down' in x:
            depth_pos += int(x[-1])
        elif 'up' in x:
            depth_pos -= int(x[-1])
    return depth_pos * horizontal_pos

def position_calc_new(command_list):

    depth_pos = 0
    horizontal_pos = 0
    aim = 0

    for x in command_list:
        if 'forward' in x:
            horizontal_pos += int(x[-1])
            if aim > 0:
                depth_pos += aim * int(x[-1])
        elif 'down' in x:
            aim += int(x[-1])
        elif 'up' in x:
            aim -= int(x[-1])    

    return depth_pos * horizontal_pos

if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'input2.txt', 'r') as f:
        text = f.read()
    command_list = text.split("\n")
    print(f'Challenge 1 Answer: {position_calc(command_list)}')
    print(f'Challenge 2 Answer: {position_calc_new(command_list)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))