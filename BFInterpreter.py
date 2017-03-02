import sys

DEFAULT_CELLS = 10
numberOfCells = DEFAULT_CELLS
cells = [0]
ptr = 0
loopStack = []

def openFile():
    # Open the file
    stdin = input("File name: ")
    try:
        f = open(stdin)
    except:
        print("Error: File not found or corrupted.")

    # Read from the file
    lines = []
    for line in f:
        lines.append(line)

    # Close the file
    f.close()

    return lines

def handleChar(c):
    global ptr
    global cells
    global loopStack
    # + Add one to the cell currently pointed
    if(c) == "+":
        cells[ptr] = cells[ptr] + 1
        if cells[ptr] > 255:
            cells[ptr] = cells[ptr] - 256
    # - Subtract one to the cell currently pointed
    elif(c) == "-":
        cells[ptr] = cells[ptr] - 1
        if cells[ptr] < 0:
            cells[ptr] = cells[ptr] + 256
    # > increase the pointer by 1
    elif(c) == ">":
        ptr += 1
        if ptr > numberOfCells:
            print("Memory Error: " + str(ptr))
            sys.exit(-1)
    # < decrease the pointer by 1
    elif(c) == "<":
        ptr -= 1
        if ptr < 0:
            print("Memory Error: " + str(ptr))
            sys.exit(-1)
    # . Print char at pointer
    elif(c) == ".":
        print(chr(cells[ptr]), end='')
    # , Accept one byte of input
    elif(c) == ",":
        cells[ptr] = sys.stdin.read(1)
    # [ Start of loop
    #elif(c) == "[":

    # ] End of loop
    #elif(c) == "]":



# Load the optional number of cells
argv = sys.argv
if len(argv) > 1:
    try:
        numberOfCells = int(argv[1])
    except:
        print("Invalid number of cells. Using default.")
        numberOfCells = DEFAULT_CELLS
for i in range(1, numberOfCells):
    cells.append(0)

# Open the file
f = openFile()

# Handle the code
for i in f:
    for j in i:
        handleChar(j)

print(cells)
