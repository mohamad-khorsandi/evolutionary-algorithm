import csv
import config
import numpy as np


def main():
    with open('blocks_population.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = np.array(list(csv_reader)).astype(float)
    config.read_config()
    # print(data)



if __name__ == '__main__':
    main()

