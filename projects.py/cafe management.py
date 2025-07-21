print("welcome to our resturant!",end=" ")
print("Here is the menu sir ")

from tabulate import tabulate

rows = [
    ["Pizza",240], 
    ["Burger",80,] ,
    ["Chowmein",80] ,
    ["Oreo Shake",120],
    ["Pav Bhaji",70],
    ["Garlic Bread",80],
    ["Pineapple Pastry",50],
    ["Snack Roll",40],
    ["Coffee",55],
    ["Tea",30] ,
    ["Cold Coffe",100] ,       
    ["Dosa",90],
    ["Mango Mojito",100],
    ["Cheeze Overloaded Pizza",100]
]

head=["Items","Price"]

print(tabulate(
    tabular_data=rows,
    headers=head,
    tablefmt="double_grid")
)
menu = {
    "Pizza":240, 
    "Burger":80 ,
    "Chowmein":80,
    "Oreo Shake":120,
    "Pav Bhaji":70,
    "Garlic Bread":80,
    "Pineapple Pastry":50,
    "Snack Roll":40,
    "Coffee":55,
    "Tea":30 ,
    "Cold Coffe":100 ,       
    "Dosa":90,
    "Mango Mojito":100,
    "Cheeze Overloaded Pizza":100
}


bill=0
item_1=input("please give your order ")
if item_1 in menu:
    print("here is your order sir ")
    bill = bill + menu[item_1]
else:
    print("please give correct order")

another_order=input("any other thing you want to order sir? (yes/no) ")
if another_order=="yes":
    item_2=input("what's the next order sir ")
    if item_2 in menu:
        print("here is your next order sir")
        bill = bill + menu[item_2]
    if item_2=="no":
        print("give me bill")
    else:
       print("please give correct order sir ")
print("your bill sir " , bill)