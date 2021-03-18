class Controller():
    def __init__(self, memory, instruction_counter, instruction_register, operation_code, operand, accumulator):
        self.memory = memory
        self.instruction_counter = instruction_counter
        self.instruction_register = instruction_register
        self.operation_code = operation_code
        self.operand = operand
        self.accumulator = accumulator


    def add(self, memory_location):
        """Adds a number from a specific location in memory to the number in the accumulator."""
        memory_value = self.memory[memory_location]
        self.accumulator += memory_value
        if self.accumulator > 9999 or self.accumulator < -9999:
            raise ValueError("Your accumulator number exceeds the range available.")
        return self.accumulator


    def subtract(self, memory_location):
        """Subtracts a number from a specific location in memory from the number in the accumulator."""

        memory_value = self.memory[memory_location]
        self.accumulator -= memory_value
        if self.accumulator > 9999 or self.accumulator < -9999:
            raise ValueError("Your accumulator number exceeds the range available.")
        return self.accumulator


    def multiply(self, memory_location):
        """Multiplies a number from a specific memory location to the number in the accumulator
        and returns the accumulator"""

        memory_value = self.memory[memory_location]
        self.accumulator *= memory_value
        self.accumulator = int(self.accumulator)
        if self.accumulator > 9999 or self.accumulator < -9999:
            raise ValueError("Your accumulator number exceeds the range available.")
        return


    def divide(self, memory_location):
        """Divides the number in the accumulator by a number from a specific location in memory
        and returns the accumulator."""

        memory_value = self.memory[memory_location]
        self.accumulator /= memory_value
        self.accumulator = int(self.accumulator)
        if self.accumulator > 9999 or self.accumulator < -9999:
            raise ValueError("Your accumulator number exceeds the range available.")
        return


    def read(self, memory_location):
        """Asks the user for an integer and puts it into a specific location in memory"""
        userInput = input("Enter an integer between -9999 and 9999: ")
        try:
            userInput = int(userInput)
        except ValueError:
            print("Must be an int")
        except TypeError:
            print("Must be an int")
        else:
            if userInput > 9999 or userInput < -9999:
                print("must be an integer between -9999 and +9999")

            else:
                # userInput = str(userInput)
                # userInput = "+" + userInput.zfill(
                # 4
                # )   Formats input to be the same as memory format
                self.memory[memory_location] = userInput
                return


    def write(self, memory_location):
        """Prints the contents of the given memory location to the screen"""

        print(
            f"Contents of memory location {memory_location} is {self.memory[memory_location]}."
        )
        return


    def load(self, memory_location):
        """ Will take a memory location and load what ever is there into the accumulator  """

        self.accumulator = self.memory[memory_location]
        return


    def store(self, memory_location):
        """ Will take whatever is in the accumulator and will store it in the given location """

        self.memory[memory_location] = self.accumulator
        return


    def branch_neg(self):
        """Will return True if the accumulator is less than zero, otherwise will return False"""

        if self.accumulator < 0:
            return True
        else:
            return False


    def branch_zero(self):
        """Will return True if the accumulator is equal to zero, otherwise will return False"""

        if self.accumulator == 0:
            return True
        else:
            return False


    def run_instructions(self):
        """Runs the program written into the memory"""
        
        print("---- Running Program ----\n")
        index = 0
        while index < (len(self.memory) - 1):
            if self.memory[index] == "-99999":
                break

            op = int(self.memory[index][1:3])
            memory_location = int(self.memory[index][3:5])

            if op == 10:
                self.read(memory_location)
                index += 1
                self.instruction_counter += 1
            elif op == 11:
                self.write(memory_location)
                index += 1
                self.instruction_counter += 1
            elif op == 20:
                self.load(memory_location)
                index += 1
                self.instruction_counter += 1
            elif op == 21:
                self.store(memory_location)
                index += 1
                self.instruction_counter += 1
            elif op == 30:
                self.add(memory_location)
                index += 1
                self.instruction_counter += 1
            elif op == 31:
                self.subtract(memory_location)
                index += 1
                self.instruction_counter += 1
            elif op == 32:
                self.divide(memory_location)
                index += 1
                self.instruction_counter += 1
            elif op == 33:
                self.multiply(memory_location)
                index += 1
                self.instruction_counter += 1
            elif op == 40:
                index = memory_location
                self.instruction_counter += 1
            elif op == 41:
                if self.branch_neg() is True:
                    index = memory_location
                    self.instruction_counter += 1
                else:
                    index += 1
            elif op == 42:
                if self.branch_zero() is True:
                    index = memory_location
                    self.instruction_counter += 1
                else:
                    index += 1
            elif op == 43:  # Halt the program
                self.instruction_counter += 1
                self.operation_code = op
                self.operand = memory_location
                break

            else:
                self.instruction_counter += 1
                self.instruction_register = self.memory[index]
                self.operation_code = op
                self.operand = memory_location
                index += 1

            self.instruction_register = self.memory[index]
            self.operation_code = op
            self.operand = memory_location 
        print("\n---- Program Finished ----")
    def __str__(self):
        pass