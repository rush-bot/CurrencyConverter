#Selecting the intended currency

def selectCurrencies():
    from currencies import chooseCurrencies
    while True:
        try:
            # The program will try to assign the user's input to a variable based the value typed in
            tempCurrency = int(input())
        except ValueError as err:
            # If there is an error, the user will need to type in a new numerical value
            print("Error: The code typed in is in the wrong format.\n"
                  "Type in a positive integer code.")
            continue
        if (tempCurrency < 0):
            #If the code is out of bounds, the user will need to type in a new code
            print("Error: The code typed in does not match any of the currency codes.\n"
                  "Type a code that is positive in numeric value.")
            continue
        elif (tempCurrency > 25):
            #If the code is out of bounds, the user will need to type in a new code
            print("Error: The code typed in does not match any of the currency codes.\n"
                  "Type a code that is lower in numeric value.")
            continue
        elif isinstance(tempCurrency, float):
            #If the code is not in the right numerical format, the user will need to type in a new code
            print("Error: The code typed in does not match any of the currency codes.\n"
                  "Type a code that is a positive integer.")
            continue
        else:
            #The correct currency information is displayed and the chosen currency is returned
            selectedCurrency = chooseCurrencies(tempCurrency)
            print("The code number {} was chosen successfully: The {} from {}.\n"
                  .format(selectedCurrency["Code"], selectedCurrency["Name"], selectedCurrency["Country"]))
            return selectedCurrency
            break