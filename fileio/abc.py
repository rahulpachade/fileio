import sys

fname = "python.txt"
num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)
while True:
    option = input("Choose Your Option:--")
    if option == 'l' or option == 'L':
        print(f"Number Of Line Present in the file {num_lines}")
    elif option == 'C' or option == 'c':
        print(f"Number Character Present in the file {num_chars}")
    elif option == 'W' or option == 'w':
        print(f"Number Character Present in the file {num_words}")
    elif option == 'E' or option == 'e':
        print("Thank You!!")
        sys.exit()
    else:
        print("Please Choose proper option")            

