import csv
import math


class Tax:
    def __init__(self, lower, upper, tax):
        self.lower = lower
        self.upper = upper
        self.tax = tax


def pretax(r, o):
    return (r*123.68) + (o*185.52) + ((r+o)*22.26)


def taxred(p):
    for a in avdrag:
        if a.lower <= p <= a.upper:
            return a.tax
        else:
            continue


def posttax(reg, ovr):
    return pretax(reg, ovr) - taxred(pretax(reg, ovr))


def decimalfix(num):
    return math.ceil(num*100)/100


def main():
    print("\nVälkommen till lönekalkylatorn! \n\n")
    regular = float(input("Antal vanliga timmar: "))
    overtime = float(input("Antal övertidstimmar: "))
    print("\nDin lön blir:\n\n" + str(decimalfix(posttax(regular, overtime))) + " efter skatt\n\noch\n\n" +
          str(decimalfix(pretax(regular, overtime))) +
          " före skatt.\n")


avdrag = []
with open('skatt.csv', 'r') as skatt:
    skattreader = csv.reader(skatt, delimiter=',')
    for row in skattreader:
        avdrag.append(Tax(float(row[0]), float(row[1]), float(row[2])))


if __name__ == '__main__':
    main()
