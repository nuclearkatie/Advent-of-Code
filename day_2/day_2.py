import csv


def main():
    intcode = []
    with open('intcode.csv', 'r+') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            intcode.append(row)

    intcode = [int(i) for i in intcode[0]]
    intcode = Restore_Gravity_Assist(intcode)

    Intcode_Program(intcode, 0)


def Intcode_Program(intcode, i):
    if intcode[i] == 1:
        output = Opcode1(intcode, i)
    elif intcode[i] == 2:
        output = Opcode2(intcode, i)
    elif intcode[i] == 99:
        print(intcode)
        return
    else:
        raise Exception('Intcode Error: Unknown intcode')

    overwrite_position = intcode[i+3]
    intcode[overwrite_position] = output
    i += 4

    Intcode_Program(intcode, i)


def Opcode1(intcode, i):
    position1 = intcode[i+1]
    position2 = intcode[i+2]
    output = intcode[position1] + intcode[position2]

    return output


def Opcode2(intcode, i):
    position1 = intcode[i+1]
    position2 = intcode[i+2]
    output = intcode[position1] * intcode[position2]

    return output


def Restore_Gravity_Assist(intcode):
    intcode[1] = 12
    intcode[2] = 2

    return intcode


if __name__ == "__main__":
    main()
