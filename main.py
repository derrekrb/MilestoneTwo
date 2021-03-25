from view import View
import tkinter as tk

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

    # print(
    #     "---- Instructions given in the UVsim must be in the format of +0000.  Ex. +1001 is a valid instruction ----"
    # )

    # while entry_command != "-99999":
    #     entry_command = input(str(program_counter).zfill(2) + " ? ")
    #     if entry_command != "-99999":
    #         memory[program_counter] = entry_command
    #         program_counter += 1

    window = tk.Tk()
    window.title("UVsim")
    window.geometry("1000x600")
    v = View(
        window,
        memory,
        instruction_counter,
        instruction_register,
        operation_code,
        operand,
        accumulator,
    )

    window.mainloop()


if __name__ == "__main__":
    main()
