class Memory():
    def __init__(self, memory):
        self.memory = memory

    def clean_memory(self, memory):
        index = 0
        while index < len(memory):
            number = memory[index]
            valid = False

            while not (valid):
                if (len(number) != 5) and (
                    number != "-99999"
                ):  # Checks if length of instruction is correct
                    print(f"{number} is not a valid instruction")
                    number = str(input("Enter a valid instruction:"))

                elif (number[0] not in ("+", "-")) and (
                    number != "-99999"
                ):  # Checks if instruction contain a + (Except if -99999)
                    print(f"{number} is not a valid instruction")
                    number = str(input("Enter a valid instruction:"))

                else:
                    valid = True
                    memory[index] = str(number)
            index += 1
        return self.memory