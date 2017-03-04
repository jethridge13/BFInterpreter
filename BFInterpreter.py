import sys

DEFAULT_CELLS = 100
numberOfCells = DEFAULT_CELLS
cells = [0]
ptr = 0
loopStack = []

# @return array
# This method prompts the user for a file name and then attempts to open it. If the file is not found, it throws an
# error. It returns a list of all the data in the file. A line in the file is a cell in the list.
def openFile():
    # Open the file
    stdin = input("File name: ")
    try:
        f = open(stdin)


        # Read from the file
        lines = []
        for line in f:
            lines.append(line)

        # Close the file
        f.close()
    except:
        print("Error: File not found or corrupted.")
        return -1

    return lines

# @param c The character to handle logic for
# @param line The line from which the character came
# @param char The char position in the line
# @return tuple Returns a tuple with the (line, char) of the current position in the logic. This is used in loops.
# This function handles the logic of the languuage. It manipulates the pointer, cells, input, and output.
def handleChar(c, line, char):
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
    elif(c) == "[":
        loopStack.append((line, char))
    # ] End of loop
    elif(c) == "]":
        if cells[ptr] == 0:
            loopStack.pop()
        else:
            return loopStack[-1]
    return (line, char)

# @param array The array with the information as obtained from calling openFile()
# This method moves through the array with the language logic.
def parse(array):
    line = 0
    maxLine = len(array)
    char = 0
    while line < maxLine:
        activeLine = array[line]
        c = activeLine[char]
        tup = handleChar(c, line, char)
        line = tup[0]
        char = tup[1]
        char += 1
        if char >= len(array[line]):
            char = 0
            line += 1

def main(argv):
    global numberOfCells
    global cells
    # Load the optional number of cells
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
    if f == -1:
        sys.exit(-1)

    # Handle the code
    parse(f)

if __name__ == "__main__":
    main(sys.argv)