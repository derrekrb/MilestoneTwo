from model import Memory
from controller import Controller
from view import View

"""
CS2450: Milestone 1
William Martell
Tanner Erekson
Derrek Buttars
Matthew Palmer
"""

def main():
    entry_command = 1
    program_counter = 0
    
    memory = ["+0000"] * 100
    accumulator = 0
    instruction_counter = 0
    instruction_register = ""
    operation_code = 0
    operand = 0
    
    print(
        "---- Instructions given in the UVsim must be in the format of +0000.  Ex. +1001 is a valid instruction ----"
    )
    while entry_command != "-99999":
        entry_command = input(str(program_counter).zfill(2) + " ? ")
        if entry_command != "-99999":
            memory[program_counter] = entry_command
            program_counter += 1

    
    m = Memory(memory)
    m.clean_memory(memory)


    c = Controller(memory, instruction_counter, instruction_register, operation_code, operand, accumulator)
    c.run_instructions()


    p = View(c.memory, c.instruction_counter, c.instruction_register, c.operation_code, c.operand, c.accumulator)
    p.printing()


if __name__ == "__main__":
    main()

