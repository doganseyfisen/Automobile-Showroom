import time

from auto_showroom import *

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
    user_select = input("Your request: ")
    print("\n")

    if user_select == "q" or user_select == "Q":
        print("Goodbye!")
        break

    elif user_select == "1":
        showroom.show_all_autos()

    elif user_select == "2":
        brand = input("Which brand do you want to query: ")
        print("Querying now...")
        time.sleep(2)
        showroom.query_autos(brand)
        print("Queried.\n")

    elif user_select == "3":
        brand = input("Brand: ")
        model = input("Model: ")
        year = int(input("Year: "))
        price = int(input("Price: "))
        hp = int(input("HP: "))
        transmission = input("Transmission: ")
        cc = int(input("CC: "))
        new_auto = Automobile(brand, model, year, price, hp, transmission, cc)
        print("Adding now...")
        time.sleep(2)
        showroom.add_auto(new_auto)
        print("Added.\n")

    elif user_select == "4":
        brand = input("Brand: ")
        model = input("Model: ")
        year = int(input("Year: "))
        answer_is = input("Do you want to continue deleting process? Y/N: ")

        if answer_is == "Y" or answer_is == "y":
            print("Deleting now...")
            time.sleep(2)
            showroom.delete_auto(brand, model, year)
            print("Deleted.\n")

    elif user_select == "5":
        brand = input("Brand: ")
        model = input("Model: ")
        year = input("Year: ")
        cc = int(input("CC: "))
        showroom.raise_price(brand, model, year, cc)
        print("Raising now....")
        time.sleep(2)
        print("Raised.\n")

    elif user_select == "6":
        brand = input("Brand: ")
        model = input("Model: ")
        year = input("Year: ")
        cc = int(input("CC: "))
        showroom.reduce_price(brand, model, year, cc)
        print("Reducing now....")
        time.sleep(2)
        print("Reduced.\n")

    else:
        print("Invalid request!\n")
