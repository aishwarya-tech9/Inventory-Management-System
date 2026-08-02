products=[]
def add_product():
    name=input("Enter product name : ")
    price=float(input("Enter Price : "))
    quantity=int(input("Enter quantity : "))
    total=price*quantity
    products.append({
        "name":name,
        "price":price,
        "quantity":quantity,
        "total":total
    })
    print("product added successfully")
def view_product():
    if len(products)==0:
        print("no prouduct found.")
    else:
        print("name\t\tprice\tquantity\ttotal")
        for product in products:
            print(f"{product["name"]}\t\t{product["price"]}\t{product["quantity"]}\t\t{product["total"]}")

def search_product():
    search_product=input("Search product :")
    found=False
    for product in products:
        if product["name"]==search_product:
            print("name\t\tprice\tquantity\ttotal")
            print(f"{product["name"]}\t\t{product["price"]}\t{product["quantity"]}\t\t{product["total"]}")
            found=True
            break
        if not found:
            print("not found.")
def update_product():
    update_product=input("Enter name which want to update : ")
    found=False
    for product in products:
        if product["name"]==update_product:
            print("found")  
            new_name=input("New name : ")
            new_price=float(input("New price : "))
            new_quantity=int(input("New quantity : "))
            product["name"]=new_name
            product["price"]=new_price
            product["quantity"]=new_quantity
            product["total"]=new_price*new_quantity
            print("updated successfully.")
            found=True
            break   
    if not found:
        print("not found.")
def delete_product():
    delete_product=input("Enter which want to delete : ")
    found=False
    for product in products:
        if product["name"]==delete_product:
            print("found")
            products.remove(product)
            print("deleted successfully")
            found=True
            break
        if not found:
            print("not found")
def total_inventory_value():
    total_inventory_value=0
    for product in products:
        total_inventory_value=total_inventory_value+product["price"]*product["quantity"]
    print("Total inventory value :",total_inventory_value)
def save_inventory():
    file=open("inventory.txt","w")
    print(products)
    for product in products:
        file.write(f"{product["name"]},{product["price"]},{product["quantity"]},{product["total"]}\n")
    print("Inventory save successfully")
    file.close()
def load_inventory():
    file=open("inventory.txt")
    products.clear()
    for line in file:
        name, price, quantity, total=line.strip().split(",")
        products.append({
            "name":name,
            "price":float(price),
            "quantity":int(quantity),
            "total":float(total)
        })
    file.close()
    print("Inventory load successfully")
while True:
    print("\n---------Inventory Management System---------")
    print("1. Add product")
    print("2. view product")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Total inventory product")
    print("7. Save inventory")
    print("8. Load inventory ")
    print("9. Exit")

    choice=input("choice (1-9): ")

    if choice == "1": 
        add_product()

    elif choice == "2":
        view_product()

    elif choice =="3":
        search_product()

    elif choice == "4":
        update_product()
        view_product()

    elif choice == "5":
        delete_product()
        view_product()

    elif choice == "6":
        view_product()
        total_inventory_value()
        
    elif choice == "7":
        save_inventory()

    elif choice=="8": 
        load_inventory()

    elif choice=="9":
        print("-------EXIT-------")
        break

    else:
        print("Sorry, This is invalid option.\nPlease Enter choice again.")


