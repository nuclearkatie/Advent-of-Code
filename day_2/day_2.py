import csv
import argparse


def main(noun, verb):
    intcode = []
    with open('intcode.csv', 'r+') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            intcode.append(row)

    intcode = [int(i) for i in intcode[0]]
    intcode = Restore_Gravity_Assist(intcode, noun, verb)

    Intcode_Program(intcode, 0)

    print(intcode[0])

    return intcode[0]


def Intcode_Program(intcode, i):
    if intcode[i] == 1:
        output = Opcode1(intcode, i)
    elif intcode[i] == 2:
        output = Opcode2(intcode, i)
    elif intcode[i] == 99:
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


def Restore_Gravity_Assist(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb

    return intcode


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--noun", help='noun value', type=int, nargs=1,
                        default=12)
    parser.add_argument("-v", "--verb", help='verb value', type=int, nargs=1,
                        default=2)
    args = parser.parse_args()

    noun = args.noun
    verb = args.verb

    main(noun, verb)
