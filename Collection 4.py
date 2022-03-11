Menu_Select = {'Hotdog':30, 'Burger':35, 'Water':10, 'Salmon':45}
Menulist = []


def bill():
    totalprice = 0
    text = "Total"
    print(text.center(21,"="))
    for x in range(len(Menulist)):
        print(Menulist[x][0],Menulist[x][1])
        totalprice += (Menulist[x][1])
    print("Total : ", totalprice , "THB !!")

while True:
    Menu = input("What your select : ")
    if Menu.lower() == 'exit':
        break
    else:
        Menulist.append([Menu,Menu_Select[Menu.capitalize()]])


bill()