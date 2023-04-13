import time

from autoShowroom import *
print(""""
=== WELCOME TO AUTO-SHOWROOM ===

What do you want to do?

[1] Show all of the automobiles
[2] Query the automobiles
[3] Add into database an automobile
[4] Delete from database an automobile
[5] Raise price of the automobile
[6] Reduce price of the automobile
[Exit] To exit, please enter 'q' or 'Q'

=================================
""")
showroom = Showroom()
while True:
    userSelect = input("Your request: ")
    print("\n")
    if (userSelect == "q" or userSelect == "Q"):
        print("Goodbye!")
        break
    elif (userSelect == "1"):
        showroom.showAllAutos()
    elif (userSelect == "2"):
        brand = input("Which brand do you want to query: ")
        print("Querying now...")
        time.sleep(2)
        showroom.queryAutos(brand)
        print("Queried.\n")
    elif (userSelect == "3"):
        brand = input("Brand: ")
        model = input("Model: ")
        year = int(input("Year: "))
        price = int(input("Price: "))
        hp = int(input("HP: "))
        transmission = input("Transmission: ")
        cc = int(input("CC: "))
        newAuto = Automobile(brand, model, year, price, hp, transmission, cc)
        print("Adding now...")
        time.sleep(2)
        showroom.addAuto(newAuto)
        print("Added.\n")
    elif (userSelect == "4"):
        brand = input("Brand: ")
        model = input("Model: ")
        year = int(input("Year: "))
        answerIs = input("Do you want to continue deleting process? Y/N: ")
        if (answerIs == "Y" or answerIs == "y"):
            print("Deleting now...")
            time.sleep(2)
            showroom.deleteAuto(brand, model, year)
            print("Deleted.\n")
    elif (userSelect == "5"):
        brand = input("Brand: ")
        model = input("Model: ")
        year = input("Year: ")
        cc = int(input("CC: "))
        showroom.raisePrice(brand, model, year, cc)
        print("Raising now....")
        time.sleep(2)
        print("Raised.\n")
    elif (userSelect == "6"):
        brand = input("Brand: ")
        model = input("Model: ")
        year = input("Year: ")
        cc = int(input("CC: "))
        showroom.reducePrice(brand, model, year, cc)
        print("Reducing now....")
        time.sleep(2)
        print("Reduced.\n")
    else:
        print("Invalid request!\n")