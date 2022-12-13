import timeit

def start_of_packet(input):
    for i in range(len(input)):
        word = input[i:i+4]
        lock = 0
        for letter in word:
            if word.count(letter) == 1:
                lock += 1
        
        if lock == 4:
            return i + 4

def start_of_message(input):
    for i in range(len(input)):
        word = input[i:i+14]
        lock = 0
        for letter in word:
            if word.count(letter) == 1:
                lock += 1
        
        if lock == 14:
            return i + 14


if __name__ == "__main__":
    start_time = timeit.default_timer()
    with open(r'/Users/godfreynelmes/Documents/GitHub/advent-of-code/2022/day6/input6.txt', 'r') as f:
        input = f.read()
    print(f'Challenge 1 Answer: {start_of_packet(input)}')
    print(f'Challenge 2 Answer: {start_of_message(input)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))