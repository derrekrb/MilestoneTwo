from model import Memory
from controller import Controller
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

    window = tk.Tk()
    mainFrame = tk.Frame(window)
    mainFrame.grid(sticky="news", pady=50, padx=50)

    # Displays the greeting to the UVsim
    greeting = tk.Label(
        mainFrame,
        text="---- Instructions given in the UVsim must be in the format of +0000.  Ex. +1001 is a valid instruction ----",
    )
    greeting.grid(row=0, column=1, pady=10, padx=10)

    frame_canvas = tk.Frame(mainFrame)
    frame_canvas.grid(row=1, column=0, pady=(5, 0), sticky="nw")
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)
    frame_canvas.grid_propagate(False)

    canvas = tk.Canvas(frame_canvas)
    canvas.grid(row=0, column=0, sticky="news")

    vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=vsb.set)

    frame_input = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_input, anchor="nw")

    for line in range(len(memory)):
        lineNum = tk.Label(frame_input, text=str(line).zfill(2) + "   ")
        lineEntry = tk.Entry(frame_input)
        lineNum.grid(column=1, row=line, sticky="news")
        lineEntry.grid(column=2, row=line, sticky="news")

    frame_input.update_idletasks()
    frame_canvas.config(width=200, height=400, padx=10, pady=10)
    canvas.config(scrollregion=canvas.bbox("all"))

    memory_frame = tk.Frame(mainFrame)
    memory_location = 0
    for i in range(10):
        for j in range(10):
            mem_content = tk.Label(memory_frame, text=memory[memory_location])
            mem_content.grid(row=i, column=j, padx=5, pady=5)
            memory_location += 1
    memory_frame.grid(column=1, row=1)

    register_frame = tk.Frame(mainFrame)

    ir_frame = tk.Frame(register_frame)
    tk.Label(ir_frame, text="Instruction Register").grid(row=0)
    tk.Label(ir_frame, text=instruction_register).grid(row=1)
    ir_frame.grid(row=0, pady=10)

    ic_frame = tk.Frame(register_frame)
    tk.Label(ic_frame, text="Instruction Counter").grid(row=0)
    tk.Label(ic_frame, text=instruction_counter).grid(row=1)
    ic_frame.grid(row=1, pady=10)

    ac_frame = tk.Frame(register_frame)
    tk.Label(ac_frame, text="Accumulator").grid(row=0)
    tk.Label(ac_frame, text=accumulator).grid(row=1)
    ac_frame.grid(row=2, pady=10)

    opcode_frame = tk.Frame(register_frame)
    tk.Label(opcode_frame, text="Op Code").grid(row=0)
    tk.Label(opcode_frame, text=operation_code).grid(row=1)
    opcode_frame.grid(row=3, pady=10)

    operand_frame = tk.Frame(register_frame)
    tk.Label(operand_frame, text="Operand").grid(row=0)
    tk.Label(operand_frame, text=operand).grid(row=1)
    operand_frame.grid(row=4, pady=10)

    register_frame.grid(row=1, column=2, padx=10, pady=10)

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

    c = Controller(
        memory,
        instruction_counter,
        instruction_register,
        operation_code,
        operand,
        accumulator,
    )
    c.run_instructions()

    p = View(
        c.memory,
        c.instruction_counter,
        c.instruction_register,
        c.operation_code,
        c.operand,
        c.accumulator,
    )
    p.printing()

    window.mainloop()


if __name__ == "__main__":
    main()
