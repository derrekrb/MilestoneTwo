class View():
    def __init__(self, memory, instruction_counter, instruction_register, operation_code, operand, accumulator):
        self.memory = memory
        self.instruction_counter = instruction_counter
        self.instruction_register = instruction_register
        self.operation_code = operation_code
        self.operand = operand
        self.accumulator = accumulator


    def printing(self):
        print("\nREGISTERS:")
        print("Accumulator:            " + str(self.accumulator))
        print("Instruction Counter:    " + str(self.instruction_counter))
        print("InstructionRegister:    " + self.instruction_register)
        print("Operation Code:         " + str(self.operation_code).zfill(2))
        print("Operand:                " + str(self.operand).zfill(2))

        print("Memory:")
        print("       00     01     02     03     04     05     06     07     08     09")
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
