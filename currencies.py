#Defining the currency codes and outputting them

def printCurrencies():
    #A list of all the currencies and their codes is printed to the screen
    print("List of Currencies:\n"
          "Dollar (United States of America) --> 01\n"
          "Euro (Europe) ----------------------> 02\n"
          "Yen (Japan)-------------------------> 03\n"
          "Pound (United Kingdom) -------------> 04\n"
          "Dollar (Canada) --------------------> 05\n"
          "Franc (Switzerland) ----------------> 06\n"
          "Renminbi (China) -------------------> 07\n"
          "Dollar (Australia) -----------------> 08\n"
          "Krona (Sweden) ---------------------> 09\n"
          "Krone (Netherlands) ----------------> 10\n"
          "Peso (Mexico) ----------------------> 11\n"
          "Won (South Korea) ------------------> 12\n"
          "Lira (Turkey) ----------------------> 13\n"
          "Rupee (India) ----------------------> 14\n"
          "Ruble (Russia) ---------------------> 15\n"
          "Real (Brazil) ----------------------> 16\n"
          "Riyal (Saudi Arabia) ---------------> 17\n"
          "Rand (Africa) ----------------------> 18\n"
          "Zloty (Poland) ---------------------> 19\n"
          "Baht (Thailand) --------------------> 20\n"
          "Rupiah (Indonesia) -----------------> 21\n"
          "Koruna (Czech Republic) ------------> 22\n"
          "New Shekel (Israel) ----------------> 23\n"
          "Forint (Hungary) -------------------> 24\n"
          "Dirham (United Arab Emirates) ------> 25\n")

#Defining information for each currency and outputtign the correct information for the chosen currency

def chooseCurrencies(code):
    #A dictionary is created for every single currency with all the informqtion about it
    dollarUSA = {"Code": 1, "Name": "Dollar", "Country": "United States of America"}
    euro = {"Code": 2, "Name": "Euro", "Country": "Europe"}
    yen = {"Code": 3, "Name": "Yen", "Country": "Japan"}
    pound = {"Code": 4, "Name": "Pound", "Country": "United Kingdom"}
    dollarCAN = {"Code": 5, "Name": "Dollar", "Country": "Canada"}
    franc = {"Code": 6, "Name": "Franc", "Country": "Switzerland"}
    renminbi = {"Code": 7, "Name": "Yuan Renminbi", "Country": "China"}
    dollarAUS = {"Code": 8, "Name": "Dollar", "Country": "Australia"}
    krona = {"Code": 9, "Name": "Krona", "Country": "Sweden"}
    krone = {"Code": 10, "Name": "Krone", "Country": "Netherlands"}
    peso = {"Code": 11, "Name": "Peso", "Country": "Mexico"}
    won = {"Code": 12, "Name": "Won", "Country": "South Korea"}
    lira = {"Code": 13, "Name": "Lira", "Country": "Turkey"}
    rupee = {"Code": 14, "Name": "Rupee", "Country": "India"}
    ruble = {"Code": 15, "Name": "Ruble", "Country": "Russia"}
    real = {"Code": 16, "Name": "Real", "Country": "Brazil"}
    riyal = {"Code": 17, "Name": "Riyal", "Country": "Saudi Arabia"}
    rand = {"Code": 18, "Name": "Rand", "Country": "Africa"}
    zloty = {"Code": 19, "Name": "Zloty", "Country": "Poland"}
    baht = {"Code": 20, "Name": "Baht", "Country": "Thailand"}
    rupiah = {"Code": 21, "Name": "Rupiah", "Country": "Indonesia"}
    koruna = {"Code": 22, "Name": "Koruna", "Country": "Czech Republic"}
    shekel = {"Code": 23, "Name": "New Shekel", "Country": "Isreal"}
    forint = {"Code": 24, "Name": "Forint", "Country": "Hungary"}
    dirham = {"Code": 25, "Name": "Dirham", "Country": "United Arab Emirates"}

    #A list of all the dictionaries above is created to combine all the information into one spot
    currencyData = [dollarUSA, euro, yen, pound, dollarCAN,
                    franc, renminbi, dollarAUS, krona, krone,
                    peso, won, lira, rupee, ruble,
                    real, riyal, rand, zloty, baht,
                    rupiah, koruna, shekel, forint, dirham]
    #The correct currency information will be returned based on the input value
    return currencyData[code - 1]
