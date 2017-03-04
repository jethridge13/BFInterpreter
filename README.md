This is an interpreter for an esoteric programming language with a rather vulgar name that I am omitting due to this
being linked to my professional accounts. That being said, here is the Wikipedia link about the language if you wish to
read about it: https://goo.gl/vIFJJ1

A helloworld.txt file is included so you can see how it works.

The language uses a series of cells, which are all initialized to 0, and a pointer. For BFInterpreter.py, the number of
cells is specified as an optional argument when loading up the script. A default of 100 is used if no number is specified
 or the argument isn't a usable number. In BFC.py, the number of cells is specified with the -c argument.

The language uses only 8 characters. They are specified as follows:
    >   Move the pointer one cell to the right. Throws an error if moving the cursor outside the array of cells.
    <   Move the pointer one cell to the left. Throws an error if moving the cursor outside the array of cells.
    +   Adds one to the value in the cell specified by the pointer, up to a maximum of 255. Adding 1 to 255 flows over
        back to 0.
    -   Subtracts one to the value in the cell specified by the pointer, up to a minimum of 0. Subtracting 1 to 0 flows
        over to 255.
    .   Outputs to the console the character associated with the value of the cell associated with the pointer.
    ,   Accepts one byte of input from the console.
    [   Begins a loop.
    ]   Ends a loop. If the value in the cell associated with the pointer is 0, then the loop exits. Otherwise, the
        program jumps back to the start of the loop and begins executing that code.
    All other characters are considered part of comments and subsequently ignored.


BFInterpreter.py
    BFInterpreter.py has an optional argument for specifying the number of cells wanted.
    When the program is launched, it will prompt the user for a file name. All recognized code will then be executed.

BFC.py
    BFC.py -f <input file> -c <number of cells>
    BFC.py is the same program as BFInterpreter, except is entirely console based so you don't need to prompt for a
    filename. Instead, the file is specified by the -f command. The number of cells is specified with the -c command,
    but it is not necessary to function. If not specified or invalid, the default value of 100 will be used.