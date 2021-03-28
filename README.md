M-2 CS 2450 By William Martell, Matthew Palmer, Tanner Erekson, and Derrek Buttars.

Overview: -The UVSim is a Graphical User Interface software simulator created by us over at IED (Innovative EDucation). Universities typically have a course where computer science students learn to work with registers and very low level coding, so this simulator allows for a simple and effective machine language environment. UVSIM works with a language called BasicML, which consists of instructions written in a signed four-digit decimal number, such as +1050, -5768, etc. UVSim has a 100-word memory, which are referenced by the last two digits of whatever command is entered. The BasicML program must be loaded into main memory starting at location 00 before running the program.
The UVSim contains a CPU, register, and main memory. There is also an accumulator, which is what we will use to do different arithmetic or move around numbers in various ways. Each instruction (signed four-digit decimal number) occupies one word of the 100 word UVSim memory. Each slot may contain one of these instructions, or a data value that is placed inside one of the memory slots to be worked with.

The first two digits of each instruction are the operation code specifying the operation to be performed, which will be explained in the Features section.

The last two digits of each instruction are the operand, the address of the memory location containing the word we will be operating with.

Features:
Here is a list of the operations that can be performed (Based on the first two digits of the signed four digit instruction).
I/O operation:

READ = 10 Read a word from the keyboard into a specific location in memory.
WRITE = 11 Write a word from a specific location in memory to screen. Load/store operations:
LOAD = 20 Load a word from a specific location in memory into the accumulator.
STORE = 21 Store a word from the accumulator into a specific location in memory. Arithmetic operation:
Add = 30 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)
SUBTRACT = 31 Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
DIVIDE = 32 Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator).
MULTIPLY = 33 multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator). Control operation:
BRANCH = 40 Branch to a specific location in memory
BRANCHNEG = 41 Branch to a specific location in memory if the accumulator is negative.
BRANCHZERO = 42 Branch to a specific location in memory if the accumulator is zero.
HALT = 43 Pause the program
Ending the Program / Output:
Along with all of these operations that can be performed, the UVSim will complete once it has either ran through all 100-word memory slots, or if the command -99999 is entered. Use -99999 if you can to end the program at a quicker speed. Once the input is done being read, it will be checked for validity to make sure there are no commands that are invalid and dont follow the signed four digit decimal number format. The program will be ran to completion and output the following:
Registers:

Accumulator
Instruction Counter (Counts the number of instructions ran in your program)
Instruction Register (Contains the last instruction read by your program before completion)
Operation Code (Contains the last operation code read by your program before completion)
Operand (Contains the last operand read by your program before completion)
Memory:

Memory will be printed out in a table format, with each of the instructions in the correct memory locations that they were assigned. If there was an integer number stored in a memory-word location, then it will be converted to the format that the instructions are. If the integer is negative, it will have a '-' sign in front, and if it is a positive integer it will have a '+' sign like the other instructions.
Conclusion:

All of this will be presented in a GUI tyoe environment. We hope this provides a solid work environment for each of your students at your university/college and that it will help them come to a stronger understanding of how to work with registers, along with how to work with a low-level language like BasicML.
