MenuList = []
PriceList = []

def ShowBill():
    TotalPrice = 0
    print("-----FOOD CENTER-----")
    for number in range(len(MenuList)):
        print(MenuList[number],PriceList[number])
        TotalPrice += int(PriceList[number])
    print(("TOTAL:",TotalPrice),"(THB)")

while True:
    MenuName = input("Please Enter Menu: ")
    if (MenuName.lower()) == "exit":
        break

    else:
        MenuPrice = input("Price: ")
        MenuList.append(MenuName)
        PriceList.append(MenuPrice)
ShowBill()
