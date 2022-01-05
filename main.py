#Centralized World Currency Converter
#Made By - Rushil Desai

#Imports
from currencies import printCurrencies
from selection import selectCurrencies
from money import moneyAmount
from calculate import convert

#The starting statements
print("Welcome to the currency converter!")
print("Here you can convert money between any two currencies quickly and easily.")
print("Created By: Rushil Desai\n\n")

#Choosing the first currency (the base currency that is being converted from)
print("Start by entering the correct code that corresponds to the currency you have.")
printCurrencies()
firstCurrency = selectCurrencies()

#Choosing the second currency (the resultant currency that is being converted to)
print("Next, enter the correct code that corresponds to the currency you want to convert to.")
printCurrencies()
secondCurrency = selectCurrencies()

#Setting the amount of money that is going to be converted from base currency into the resultant currency
print("Finally, the last step is to enter the amount of {} you want to be converted into {}."
      .format(firstCurrency["Name"], secondCurrency["Name"]))
amount = moneyAmount(firstCurrency, secondCurrency)

#Calculating the amount of the first currency that is equal to the second currency
actualAmount = convert(amount, firstCurrency, secondCurrency)
print("The amount of {} {} concverted to {} is: {}\n"
      .format(amount, firstCurrency["Name"], secondCurrency["Name"], actualAmount))

