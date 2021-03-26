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

    memory = ["+0000"] * 100
    accumulator = 0
    instruction_counter = 0
    instruction_register = ""
    operation_code = 0
    operand = 0

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
