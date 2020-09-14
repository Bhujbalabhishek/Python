# Use Generator to parse csv file

import csv


def parse_Csv(file):
    with open(file, "r") as csv1:
        reader1 = csv.reader(csv1)

        for row in reader1:
            yield row


for i in parse_Csv("text.csv"):
    print(i)