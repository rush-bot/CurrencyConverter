#Setting the correct amount of money in the proper format

def moneyAmount(currencyOne, currencyTwo):
    while True:
        try:
            #The program will try to assign the user's input to a variable based the value typed in
            amount = float(input())
        except ValueError as err:
            #If there is an error, the user will need to type in a new numerical value
            print("Error: You typed in a value that was not in an acceptable format.\n"
                  "Please enter a valid value.")
            continue
        #The money information is printed out and returned from this function
        print("The value that will be converted is: {} {} into {}\n"
              .format(amount, currencyOne["Name"], currencyTwo["Name"]))
        return amount
        break