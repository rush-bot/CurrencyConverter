#Calculating the conversion between the first currency and the second currency

def convert(amount, currencyOne, currencyTwo):

    #A list of all conversion rates relative to the United States Dollar
    valueData = [1.00, 1.13, 0.0087, 1.35, 0.78,
                    1.09, 0.16, 0.73, 0.11, 0.11,
                    0.049, 0.00084, 0.079, 0.013, 0.014,
                    0.18, 0.27, 0.063, 0.25, 0.03,
                    0.00007, 0.045, 0.32, 0.0031, 0.27]

    #Setting the correct currency conversion rates for both currencies
    codeOne = currencyOne["Code"]
    codeTwo = currencyTwo["Code"]

    #Calculating the amount in the second currency in terms of the first currency and the United States Dollar
    tempDollarsOne = amount * valueData[codeOne - 1]
    tempDollarsTwo = tempDollarsOne / valueData[codeTwo - 1]

    #Outputting the amount of money in terms of the second currency
    return tempDollarsTwo