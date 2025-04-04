import csv
from math import fsum


# CASE from bulk file reading videos
def getDataInput():
    with open('RealEstateData.csv', 'r') as f:
        reader = csv.reader(f)
        # Make a list out of each row of data skipping the header
        data = [row for row in reader][1:]
        return data


# CASE median function from previous project
def getMedian(number):
    # if for odd numbers, else for even
    if len(number) % 2 == 1:
        iMedian = int(len(number) / 2)
        median = number[iMedian]
    else:
        iMedian1 = int(len(number) // 2)
        iMedian2 = int(len(number) // 2 - 1)
        median = (number[iMedian1] + number[iMedian2]) / 2
    return median


def main():
    # declare lists
    lstPropertyPrices = []
    lstData = getDataInput()
    # declare dictionaries
    dictCity = {}
    dictZip = {}
    dictType = {}
    # Scan through lstData; heading already removed
    for record in lstData:
        record[8] = float(record[8])
        lstPropertyPrices.append(record[8])
        # 2nd column of lstData (city) for dict; numbered 1 starting at 0
        dictCity[record[1]] = dictCity.get(record[1], 0) + record[8]
        # 3rd column of lstData (zip) for dict; numbered 2 starting at 0
        dictZip[record[2]] = dictZip.get(record[2], 0) + record[8]
        # 8th column of lstData (property type) for dict; numbered 7 starting at 0
        dictType[record[7]] = dictType.get(record[7], 0) + record[8]

    print("Price Summary by City:")
    for city, price in dictCity.items():
        print(f'{city:15s}{price:15,.2f}')
    print("\nPrice Summary by Area Code:")
    for zip, price in dictZip.items():
        print(f'{zip:15s}{price:15,.2f}')
    print("\nPrice Summary by Property Type:")
    for type, price in dictType.items():
        print(f'{type:15s}{price:15,.2f}')

    lstPropertyPrices.sort()
    print("\nOverall Price Summary:")
    print(f"{'Minimum:':15s}{min(lstPropertyPrices):15,.2f}")
    print(f"{'Maximum:':15s}{max(lstPropertyPrices):15,.2f}")
    print(f"{'Total:  ':15s}{fsum(lstPropertyPrices):15,.2f}")
    print(f"{'Average:':15s}{fsum(lstPropertyPrices) / len(lstPropertyPrices):15,.2f}")
    print(f"{'Median: ':15s}{getMedian(lstPropertyPrices):15,.2f}")


main()
