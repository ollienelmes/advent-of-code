import timeit
def input_cleaner(text):
    line_by_line = text.split('\n')
    output=[]
    for line in line_by_line:
        clean_line = line.replace(" -> ", ",")
        output.append(clean_line.split(","))

    return output
        
def challenge_1(input):
    graph_dict = {}
    for x in range(0,1000):
        for y in range(0,1000):
            key = str(x) + " " + str(y)
            graph_dict[key] = 0

    for line in input:
        #vertical check
        if line[0] == line[2]:
            if int(line[1]) > int(line[3]):
                larger = int(line[1]) + 1
                smaller = int(line[3])
            else:
                larger = int(line[3]) + 1
                smaller = int(line[1]) 
            for y in range(smaller, larger):
                graph_dict[line[0] + " " + str(y)] += 1
        #horizontal check
        if line[1] == line[3]:
            if int(line[0]) > int(line[2]):
                larger = int(line[0]) + 1
                smaller = int(line[2])
            else:
                larger = int(line[2]) + 1
                smaller = int(line[0])
            for x in range(smaller, larger):
                graph_dict[str(x) + " " + line[1]] += 1

    intersection_count = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            key = str(x) + " " + str(y)
            if graph_dict[key] > 1:
                intersection_count +=1
    return intersection_count, graph_dict


def challenge_2(input, graph_dict):
    graph_dict = graph_dict

    for line in input:
        gradient = 0
        x1 = int(line[0])
        y1 = int(line[1])
        x2 = int(line[2])
        y2 = int(line[3])
        #check the gradient
        if (x1 == x2) or (y1 == y2):
            pass
        else:    
            gradient = (y1 - y2)/(x1 - x2)
        if gradient == 1 or gradient == -1:
            for length in range(0, abs(x1-x2)+1):
                #positive gradient
                if x1 < x2 and y1 < y2:
                    key = str(x1 + length)  + " " + str(y1 + length)
                    graph_dict[key] += 1
                #positive gradient
                elif x2 < x1 and y2 < y1:
                    key = str(x2 + length) + " " + str(y2 + length)
                    graph_dict[key] += 1
                #negative gradient
                elif x1 < x2 and y1 > y2:
                    key = str(x1 + length) + " " + str(y1 - length)
                    graph_dict[key] += 1
                #negative gradient
                elif x1 > x2 and y1 < y2:
                    key = str(x1 - length) + " " + str(y1 + length)
                    graph_dict[key] += 1
    intersection_count = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            key = str(x) + " " + str(y)
            if graph_dict[key] > 1:
                intersection_count +=1
    return intersection_count

if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'input5.txt', 'r') as f:
        text = f.read()
    input = input_cleaner(text)
    intersection_count, graph_dict = challenge_1(input)
    print(f'Challenge 1 Answer: {intersection_count}')
    print(f'Challenge 2 Answer: {challenge_2(input, graph_dict)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))