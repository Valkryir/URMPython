# Example Program provided
exampleProgramInput = [2, 4]
exampleProgram = [
    [3, 1, 2, 4],
    [1, 0, 0, 0],
    [1, 2, 0, 0],
    [3, 0, 0, 0]
]

multiplicationProgramInput = [3, 7];
multiplicationProgram = [
    [2, 0, 2, 0],
    [0, 0, 0, 0],
    [3, 1, 4, 99],
    [1, 0, 0, 0],
    [1, 3, 0, 0],
    [3, 3, 2, 7],
    [3, 0, 0, 2],
    [1, 4, 0, 0],
    [3, 1, 4, 99],
    [0, 3, 0, 0],
    [3, 0, 0, 2],
]

# an invalid program to demonstrate the "unhappy path" when checking for valid commands
invalidProgramInput = [2, 4];
invalidProgram = [
    [6, 1, 2, 4],
    [1, 0, 0, 0],
    [1, 2, 0, 0],
    [3, 0, 0, 0]
]

register = [];


def addToRegisterIfRequired(index):
    global register
    if index >= len(register):
        while index >= len(register):
            register.append(0)


def zero(instruction):
    global register
    n = instruction[1]
    register[n] = 0


def successor(instruction):
    global register
    n = instruction[1]
    old_val = register[n] + 1
    register[n] = old_val


def transfer(instruction):
    global register
    m = instruction[1]
    n = instruction[2]

    addToRegisterIfRequired(m)
    addToRegisterIfRequired(n)

    register[n] = register[m]


# if jump is required, return true, run function will handle the jump too
def jump(instruction):
    global register
    m = instruction[1]
    n = instruction[2]

    addToRegisterIfRequired(m)
    addToRegisterIfRequired(n)

    if register[m] == register[n]:
        return True
    else:
        return False


# check if instruction is the correct length and a valid code
def isValidCommand(instruction):
    if len(instruction) > 4 or len(instruction) < 4:
        print("Invalid instruction Length")
        return False
    # is the instruction "letter" valid (0-3)
    if instruction[0] > 3 or instruction[0] < 0:
        print("Invalid Instruction")
        return False

    return True


def isValidProgram(program):
    for inst in program:
        if not isValidCommand(inst):
            print("Invalid Program")
            return False
    print("Valid Program")
    return True


def run(program, reg):
    global register

    if not isValidProgram(program):
        print("Exiting")
        return False

    print("Starting Register:")
    register = reg
    print(register)

    nextInstruction = 0

    while nextInstruction < len(program):
        currentInstruction = program[nextInstruction]
        if currentInstruction[0] == 0:
            zero(currentInstruction)
            nextInstruction = nextInstruction + 1
        elif currentInstruction[0] == 1:
            successor(currentInstruction)
            nextInstruction = nextInstruction + 1
        elif currentInstruction[0] == 2:
            transfer(currentInstruction)
            nextInstruction = nextInstruction + 1
        elif currentInstruction[0] == 3:
            if jump(currentInstruction):
                nextInstruction = currentInstruction[3]
            else:
                nextInstruction = nextInstruction + 1

    print("PROGRAM COMPLETE")
    print(f"RESULT IS: {register[0]}")
    print("Full Register At Completion:")
    print(register)

    print("\n")


if __name__ == '__main__':
    print("############################\n")
    print("Addition Program\n")
    run(exampleProgram, exampleProgramInput)

    print("############################\n")
    print("Multiplication Program\n")
    run(multiplicationProgram, multiplicationProgramInput)

    print("############################\n")
    print("Invalid Program\n")
    run(invalidProgram, invalidProgramInput)
