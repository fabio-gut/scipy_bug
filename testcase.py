#!/usr/bin/env python3

from scipy.stats import genextreme as gev


def read_data():
    with open('testcase.data', 'r') as file:
        return [float(x) for x in file]

def testcase():
    data = read_data()
    all_float = True
    for x in data:
        if type(x) != float:
            all_float = False
    print(f"All values were floats? {all_float}")
    print(f"Starting test with only first 2000 points of data...")
    shape, loc, scale = gev.fit(data[0:2000])
    print(f"Starting test with only all points of data...")
    shape, loc, scale = gev.fit(data)


if __name__ == '__main__':
    testcase()
