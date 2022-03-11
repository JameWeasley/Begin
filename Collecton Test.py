
ListMenu = []
ListPrice = []

def Bill():
    Totalprice = 0
    total = "Total Order"
    print(total.center(21,"-"))
    for i in range(len(ListMenu)):
        print(ListMenu[i],ListPrice[i])
        Totalprice += int(ListPrice[i])
    print("Total : ",Totalprice,"THB")

while True:
    Menu = input("Your Menu Select : ")
    if Menu.lower() == 'exit':
        break
    else:
        price = input("Price : ")
        ListMenu.append(Menu)
        ListPrice.append(price)
    
Bill()
 