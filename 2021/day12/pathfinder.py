from collections import deque

def path_constructor(input):
    lines = input.split("\n")
    path_dict = {}
    for line in lines:
        start, end = line.split("-")
        if start not in path_dict:
            path_dict[start] = [end]
        else:
            path_dict[start].append(end)
        if end not in path_dict:
            path_dict[end] = [start]
        else:
            path_dict[end].append(start)

    return path_dict

def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True

# MAIN ALGORITHM
with open(r'test_data1.txt', 'r') as f:
    text = f.read()

path_dict = path_constructor(text)
move_list = [key for key in path_dict if key != 'start']
print(move_list)
print(path_dict)
queue = ['start']

list_of_moves = [queue]

while set([line[-1] for line in list_of_moves]) != 'end':
    
    for list in list_of_moves:
        if list[-1] != 'end':
            for move in path_dict[list[-1]]:
                new_list = list
                print(move)
                new_list.append(move)
                list_of_moves.append(new_list)


print(list_of_moves)