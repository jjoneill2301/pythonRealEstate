import inputPromptValidationModule as validate

# Constants (Made a yes no tuple, also made it a global because its immutable
# Let me know if I should try to not make a habit of this or if this is okay
tplYES_NO_TUPLE = ("Y", "N")
fCOMMISSION_PERCENTAGE = 0.03

# Create median function
def getMedian(lstPropertyPrices):
    # if odd
    if len(lstPropertyPrices) % 2 == 1:
        iMedian = int(len(lstPropertyPrices) / 2)
        calculatedMedian = lstPropertyPrices[iMedian]

    # if even
    if len(lstPropertyPrices) % 2 == 0:
        iMedian1 = int(len(lstPropertyPrices) // 2)
        iMedian2 = int(len(lstPropertyPrices) // 2) - 1
        calculatedMedian = (lstPropertyPrices[iMedian1] + lstPropertyPrices[iMedian2]) / 2

    return calculatedMedian

# Create main function
def main():
    # Create empty list; initialize sRepeat variable
    lstPropertyPrices = []
    sRepeat = "Y"

    while sRepeat in tplYES_NO_TUPLE:
        # Validate property sales value; append list
        fPropertyPrice = validate.inputFloatValidation('Enter property sales value: ', 0.01)
        lstPropertyPrices.append(fPropertyPrice)

        # Go again?
        sRepeat = validate.inputStringValidation('Enter another value Y or N ').upper()
        # Make sure Y or N is inputted
        while sRepeat not in tplYES_NO_TUPLE:
            sRepeat = validate.inputStringValidation('Enter another value Y or N ').upper()
            continue
        # then end when user inputs 'N'
        if sRepeat == tplYES_NO_TUPLE[1]:
            break

    # Sort list
    lstPropertyPrices.sort()

    # Print to screen each real estate property as a newline
    for element in lstPropertyPrices:
        # Create incrementer
        n = int(lstPropertyPrices.index(element))
        # Print with increment
        print(f'Property {n + 1}\t${element:,.2f} ')

    # Calculations
    fMedian = getMedian(lstPropertyPrices)
    fMinimum = lstPropertyPrices[0]
    fMaximum = lstPropertyPrices[-1]
    fTotal = sum(lstPropertyPrices)
    fAverage = fTotal / len(lstPropertyPrices)
    fCommission = fTotal * fCOMMISSION_PERCENTAGE

    # Print to screen (added a Newline for the sex appeal)
    print()
    print(f'Minimum     $ {fMinimum:,.2f}')
    print(f'Maximum:    $ {fMaximum:,.2f}')
    print(f'Total:      $ {fTotal:,.2f}')
    print(f'Average:    $ {fAverage:,.2f}')
    print(f'Median:     $ {fMedian:,.2f}')
    print(f'Commission: $ {fCommission:,.2f}')

main()