menu_list = {
"pizza": 400,
"tea": 50,
"paneer tikka": 150,
"coffee": 75,
"plain dosa": 150
}

order_list={}
total_bill=0

print("=====================ShivDev hotel=======================")
print("----------------Welcome to ShivDev hotel------------------")


condition=True
print("_____________menu card______________")
while condition:
    for key,value in menu_list.items():
        print(f"          {key} :  {value}")
    
    print("Place order ")
    choice=input("Enter item name: ")
    quantity=int(input("Enter quantity: "))
    
    order_list[choice]=quantity
    total_bill+=menu_list[choice.lower()]*quantity
    
    user_wants_continue=input("Will you order more? yes/no: ")
    if user_wants_continue.lower() == "yes":
        continue
    else:
        condition=False
        
print("---------------Your order list-----------------")
for key,value in order_list.items():
    print(f"        {key}, {quantity} ")
    
print("Total bill:",total_bill)
print("Thank you")