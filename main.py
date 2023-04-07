import csv


def main():
    with open('blocks_population.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for n in row:
                print(n)



if __name__ == '__main__':
    main()

