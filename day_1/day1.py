import argparse


def Fuel_Counter_Upper(fuel):
    total_fuel = sum(fuel)

    return total_fuel


def Fuel_Required(mass):
    fuel = int(mass/3)-2

    return fuel


def Fuel_Recursion(fuel, total_fuel):
    fuel_fuel = Fuel_Required(fuel)
    if fuel_fuel <= 0:
        return total_fuel

    else:
        total_fuel = total_fuel + fuel_fuel
        return Fuel_Recursion(fuel_fuel, total_fuel)


def main(args):
    rocket = []
    with open("rocket.txt", "r+") as file:
        for line in file:
            rocket.append(int(line))

    fuel = []
    fuel_for_fuel = 1
    for module in rocket:
        module_fuel = Fuel_Required(module)
        if args.fuelfuel:
            fuel.append(Fuel_Recursion(module_fuel, module_fuel))
        else:
            fuel.append(module_fuel)

    module_fuel = Fuel_Counter_Upper(fuel)
    print(module_fuel)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fuelfuel", help='compute fuel for the fuel?',
                        action='store_true')
    args = parser.parse_args()

    main(args)
