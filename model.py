import tkinter as tk
from tkinter import messagebox


class Memory:
    def __init__(self, memory):
        self.memory = memory

    def checkMemory(self, memory):
        """Checks if memory input is valid.  returns 1 if valid, 0 if not"""

        check = 1
        index = 0
        while index < len(memory):
            number = memory[index]
            if len(number) != 5:  # Checks if length of instruction is correct
                self.popupmsg(f"{number} is not a valid word")
                check = 0
            elif number[0] not in (
                "+",
                "-",
            ):  # Checks if instruction contain a + or -
                self.popupmsg(f"{number} is not a valid word")
                check = 0
            else:
                check = 1
            index += 1
        return check

    def clean_memory(self, memory):
        index = 0
        while index < len(memory):
            number = memory[index]
            memory[index] = str(number)
            index += 1
        return memory

        # index = 0
        # while index < len(memory):
        #     number = memory[index]
        #     valid = False

        #     while not (valid):
        #         if len(number) != 5:  # Checks if length of instruction is correct
        #             self.popupmsg(f"{number} is not a valid word")
        #             # print(f"{number} is not a valid instruction")
        #             # number = str(input("Enter a valid instruction:"))

        #         elif number[0] not in (
        #             "+",
        #             "-",
        #         ):  # Checks if instruction contain a + or -
        #             self.popupmsg(f"{number} is not a valid word")
        #             # print(f"{number} is not a valid instruction")
        #             # number = str(input("Enter a valid instruction:"))

        #         else:
        #             valid = True
        #             memory[index] = str(number)
        #     index += 1
        # return memory

    def popupmsg(self, msg):
        messagebox.showinfo("!", msg)
