import classMeals as c

layout = "{0:<10}{1:<10}{2:<30}"
current_order = []

def main_menu():
    while True:
        print()
        print("=" * 40)
        print(layout.format("", "Food Ordering System", ""))
        print("=" * 40)
        main_lis = ["1. Order", "2. Payment", "3. Exit"]
        for i in main_lis:
            print(layout.format("", i, ""))

        key = int(input("\n" + "Enter your choice: "))

        if key == 1:
            food_drink_order()
            break

        elif key == 2:
            pay_order()
            break

        elif key == 3:
            print()
            print("Thank you")
            break

        else:
            print()
            print("Invalid input! Please try again ")
            continue

def food_drink_order():
    while True:
        print(layout.format("", "", "-" * 21))
        print(layout.format("", "", "| FOOD & DRINK MENU |"))
        print(layout.format("", "", "-" * 21))

        partFood = read_menu_file("food-menu.txt")
        food = c.Food(partFood[0], partFood[1], partFood[2])
        foodInfo, foodPrice = food.show_food()
        print()
        partDrink = read_menu_file("drink-menu.txt")
        drink = c.Drink(partDrink[0], partDrink[1], partDrink[2])
        drinkInfo, drinkPrice = drink.show_drink()

        print("{0:<20}{1:<20}{2:<20}".format("\n" + "(U). Update", "(M). Main Menu", "(P). Payment"))
        print()

        key = str(input("Please select your choice: ")).upper()

        if (key == 'U'):
            print("\n" + "Update for: ")
            print("\n" + "(F). Food \t (D). Drink" + "\n")
            keyUpdate = str(input("Choice: ")).upper()
            if keyUpdate == 'F':
                update(foodInfo, foodPrice)
                continue

            if keyUpdate == 'D':
                update(drinkInfo, drinkPrice)
                continue

            else:
                print("Invalid input!")
                print("Proceed to order menu....." + "\n")
                continue

        if (key == 'M'):
            main_menu()
            break

        if (key == 'P'):
            pay_order()
            break

        if (key != 'U' and key != 'M' and key != 'P'):
            flag1 = get_order(key, foodInfo, foodPrice)
            flag2 = get_order(key, drinkInfo, drinkPrice)

            if flag1 is not flag2:
                pass
            else:
                print("Proceed to order menu...")
                continue
        else:
            print("Invalid input")
            continue

        keyContinue = str(input("\n" + "Continue order? (y/n) ")).upper()

        if (keyContinue == 'Y'):
            continue
        elif (keyContinue == 'N'):
            main_menu()
            break
        else:
            print("Invalid input!")
            continue

def get_order(key, lisInfo, dicPrice):
    flag = 0
    for code, name in lisInfo:
        if (key == code):
            price = dicPrice[name]
            print(layout.format("", "-" * 10, "-" * 30 ))
            print(layout.format("", "Item " , "| " + name))
            print(layout.format("", "Price", "| RM " + str(price)))
            print(layout.format("", "-" * 10, "-" * 30 ))
            print("(Q). Quantity \t (R). Return")

            key2 = str(input("\n" + "Choice: ")).upper()
            if (key2 == 'Q'):
                keyQuantity = int(input("Enter quantity: "))
                totalEachPrice = round(keyQuantity* price, 2)
                current_order.append(dicOrder(Name=name, Num=keyQuantity, Price=totalEachPrice))
                print("\n" + "You have chosen:")
                for item in current_order:
                    print (item)
                flag = 1
                break
        else:
            continue
    return flag


def update(lisInfo, dicPrice):
    keyItem = str(input("Enter code you wish to change the quantity: ")).upper()
    for code, name in lisInfo:
        if keyItem == code:
            for i in current_order:
                if i['Name'] == name:
                    keyQuantity = int(input("Enter quantity: "))
                    i['Num'] = keyQuantity
                    i['Price'] = round(keyQuantity * dicPrice[name], 2)
                    print("\n" + "You have chosen:")
                    for item in current_order:
                        print (item)
                    print("\n" + "Update success. Proceed to order menu...." + "\n")
                    flag = 1
                    break

                else:
                    continue

            break

    else:
        print("The item you choose is not in the order list. \n")

def pay_order():
    print("\n" + "Printing receipt....")
    total = 0
    layout1 = "{0:<30}{1:<10}{2:<10}"
    receipt = open("Receipt.txt", "w")
    receipt.write(layout1.format("Name", "| Num", "| Price (RM)"))
    receipt.write("\n" + "-" * 52 + "\n")
    for item in current_order:
        receipt.write(layout1.format(item['Name'] , " " * 3 + str(item['Num']) , " " * 3 + str(item['Price'])))
        receipt.write("\n")
        total =  round(total + item['Price'], 2)
    receipt.write("\n" + "=" * 52)
    receipt.write(layout1.format("\n", " " * 3 + "Total  :", " " * 3 + str(total)))
    receipt.write("\n" + "=" * 52)
    receipt.close()
    print("\n" + "Thank you for using this system!")

def read_menu_file(fileRead):
    item_code = []
    item_name = []
    item_price = []
    file = open(fileRead, "r")
    for line in file:
        data = line.split(";")
        item_code.append(data[0])
        item_name.append(data[1])
        item_price.append(float(data[2]))
    file.close()
    return item_code, item_name, item_price

def dicOrder(**order):
    return order