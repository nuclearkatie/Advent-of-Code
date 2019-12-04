import day_2
import argparse


def main(output):
    results = [(day_2.main(i, j)) for i in range(100) for j in range(100)]

    nounverb = [i for i, value in enumerate(results) if value == 19690720]

    print(nounverb[0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help='desired output', type=int,
                        nargs=1, default=19690720)
    args = parser.parse_args()

    output = int(args.output[0])
    main(output)
