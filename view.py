import tkinter as tk
from model import Memory


class View:
    def __init__(
        self,
        master,
        memory,
        instruction_counter,
        instruction_register,
        operation_code,
        operand,
        accumulator,
    ):
        # Initialize variables from main
        # and initialize main window
        self.mainFrame = tk.Frame(master)
        self.memory = memory
        self.instruction_counter = instruction_counter
        self.instruction_register = instruction_register
        self.operation_code = operation_code
        self.operand = operand
        self.accumulator = accumulator

        # Initialize Memory Class from model
        self.M = Memory(self.memory)

        self.createWindow()

    def createWindow(self):
        # Begin creating widgets
        self.mainFrame.grid(sticky="news", pady=50, padx=50)

        # Displays the greeting to the UVsim
        greeting = tk.Label(
            self.mainFrame,
            text="---- Instructions given in the UVsim must be in the format of +0000.  Ex. +1001 is a valid instruction ----",
        )
        greeting.grid(row=0, column=1, pady=10, padx=10)

        # Begin creating input box and scroll bar
        frame_canvas = tk.Frame(self.mainFrame)
        frame_canvas.grid(row=1, column=0, pady=(5, 0), sticky="nw")
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        frame_canvas.grid_propagate(False)
        canvas = tk.Canvas(frame_canvas)
        canvas.grid(row=0, column=0, sticky="news")
        vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=vsb.set)

        # Create frame for input and initialize input boxes
        frame_input = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame_input, anchor="nw")
        self.entry_list = []
        for line in range(len(self.memory)):
            lineNum = tk.Label(frame_input, text=str(line).zfill(2) + "   ")
            lineEntry = tk.Entry(frame_input)
            self.entry_list.append(lineEntry)
            lineNum.grid(column=1, row=line, sticky="news")
            lineEntry.grid(column=2, row=line, sticky="news")
        frame_input.update_idletasks()
        frame_canvas.config(width=200, height=400, padx=10, pady=10)
        canvas.config(scrollregion=canvas.bbox("all"))

        # Initialize memory frame
        self.memory_frame = tk.Frame(self.mainFrame)

        # Load memory into frame
        memory_location = 0
        self.retreive_mem_contents = []
        for i in range(10):
            for j in range(10):
                mem_content = tk.Label(
                    self.memory_frame, text=self.memory[memory_location]
                )
                mem_content.grid(row=i + 1, column=j, padx=5, pady=5)
                self.retreive_mem_contents.append(mem_content)
                memory_location += 1
        self.memory_frame.grid(column=1, row=1)

        self.load_memory_btn = tk.Button(self.mainFrame, text="Load Memory")
        self.load_memory_btn.grid(row=2, columnspan=1, pady=10)

        # Initialize all Register Frames
        register_frame = tk.Frame(self.mainFrame)

        ir_frame = tk.Frame(register_frame)
        tk.Label(ir_frame, text="Instruction Register").grid(row=0)
        tk.Label(ir_frame, text=self.instruction_register).grid(row=1)
        ir_frame.grid(row=0, pady=10)

        ic_frame = tk.Frame(register_frame)
        tk.Label(ic_frame, text="Instruction Counter").grid(row=0)
        tk.Label(ic_frame, text=self.instruction_counter).grid(row=1)
        ic_frame.grid(row=1, pady=10)

        ac_frame = tk.Frame(register_frame)
        tk.Label(ac_frame, text="Accumulator").grid(row=0)
        tk.Label(ac_frame, text=self.accumulator).grid(row=1)
        ac_frame.grid(row=2, pady=10)

        opcode_frame = tk.Frame(register_frame)
        tk.Label(opcode_frame, text="Op Code").grid(row=0)
        tk.Label(opcode_frame, text=self.operation_code).grid(row=1)
        opcode_frame.grid(row=3, pady=10)

        operand_frame = tk.Frame(register_frame)
        tk.Label(operand_frame, text="Operand").grid(row=0)
        tk.Label(operand_frame, text=self.operand).grid(row=1)
        operand_frame.grid(row=4, pady=10)

        register_frame.grid(row=1, column=2, padx=10, pady=10)

        # Update memory when load Memory button is pressed
        self.load_memory_btn.bind("<Button-1>", self.loadMemory)

    def loadMemory(self, event):
        """When load memory button is pressed, the memory is updated with new values in the entry and loaded into the memory frame"""

        for i in range(100):
            new_memory = self.entry_list[i].get()
            if new_memory != "":
                self.memory[i] = new_memory

        # Checks if inputs are valid words in BASIC ml
        if self.M.checkMemory(self.memory) == 1:

            self.M.clean_memory(self.memory)

            # Creates new memory frame with new memory values
            self.memory_frame.destroy()
            self.memory_frame = tk.Frame(self.mainFrame)
            memory_location = 0
            self.retreive_mem_contents = []
            for i in range(10):
                for j in range(10):
                    mem_content = tk.Label(
                        self.memory_frame, text=self.memory[memory_location]
                    )
                    mem_content.grid(row=i + 1, column=j, padx=5, pady=5)
                    self.retreive_mem_contents.append(mem_content)
                    memory_location += 1
            self.memory_frame.grid(column=1, row=1)

    def updateRegisters(self):
        pass

    def runProgram(self):
        pass

    def printing(self):
        print("\nREGISTERS:")
        print("Accumulator:            " + str(self.accumulator))
        print("Instruction Counter:    " + str(self.instruction_counter))
        print("InstructionRegister:    " + self.instruction_register)
        print("Operation Code:         " + str(self.operation_code).zfill(2))
        print("Operand:                " + str(self.operand).zfill(2))

        print("Memory:")
        print(
            "       00     01     02     03     04     05     06     07     08     09"
        )
        tens = 0
        i = 0
        index = 0

        while i < len(self.memory):
            if isinstance(self.memory[i], int):
                if self.memory[i] >= 0:
                    self.memory[i] = str(self.memory[i])
                    self.memory[i] = "+" + self.memory[i].zfill(4)
                    i += 1
                else:
                    self.memory[i] = str(self.memory[i])
                    self.memory[i] = self.memory[i].zfill(5)
                    i += 1
            else:
                i += 1

        while index < len(self.memory):
            print(
                f"{str(tens).zfill(2)}  {self.memory[index]}  {self.memory[index+1]}  "
                f"{self.memory[index+2]}  {self.memory[index+3]}  {self.memory[index+4]}  "
                f"{self.memory[index+5]}  {self.memory[index+6]}  {self.memory[index+7]}  "
                f"{self.memory[index+8]}  {self.memory[index+9]}"
            )
            index += 10
            tens += 10
