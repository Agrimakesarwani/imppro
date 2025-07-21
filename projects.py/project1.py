# resturant order project


menu = {"Pizza": 90,
     "Burger":30,
     "Dosa":80,
     "Idli":50,
     "Salad":35,
     "Coffee":100,
     "Shake":90
}
print("Welcome to our resturant!", end =" ")
print("here is our resturant's menu ")
print("Pizza:\trs.90\nBurger:\trs.30\nDosa:\trs.80\nIdli:\trs.50\nSalad:\trs.35\nCoffee:\trs.100\nShake:\trs.90\n")

bill=0
item_1=input("please give your order ")
if item_1 in menu:
    print("here is your order sir ")
    bill = bill + menu[item_1]
else:
    print("invalid")

another_order=input("any other thing you want to order sir? (yes/no) ")
if another_order=="yes":
    item_2=input("what's the next order sir ")
    if item_2 in menu:
        print("here is your next order sir")
        bill = bill + menu[item_2]
    else:
       print("give me bill")
print("your bill sir " , bill)