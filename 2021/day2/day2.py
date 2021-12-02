with open(r'input2.txt', 'r') as f:
    text = f.read()

def position_calc(input):
    command_list = input.split("\n")

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

def position_calc_new(input):
    command_list = input.split("\n")

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

print(position_calc(text))
print(position_calc_new(text))