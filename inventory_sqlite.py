import sqlite3
connection=sqlite3.connect("inventory.db")
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER,
    total REAL
)
""")
connection.commit() 
print("created table successfully.")

def add_product():
    name=input("Enter product name : ")
    try:
        price=float(input("Enter Price : "))
    except ValueError:
        print("Please enter valid whole number")
        return
    if price < 0:
        print("Price cannot be negative.")
        return
    try:
        quantity=int(input("Enter quantity : "))
    except ValueError:
        print("Please enter valid whole number ")
        return
    if quantity<0:
        print("quantity cannot be negative.")
        return
    total=price*quantity
    print("here is the list of product")
    cursor.execute(
    "INSERT INTO  products(name,price,quantity,total) VALUES (?,?,?,?)",
    (name, price, quantity, total)
    )
    connection.commit()
print("\nAdded product successfully.")
print("-"*40)

def view_product():
    cursor.execute("SELECT * FROM products")

    products=cursor.fetchall()
    if not products:
        print("\nNo products found.")
        return
    print("\n"+"="*75)
    print("\t\t\t\tPRODUCT LIST")
    print("="*75)
    print(f"{'ID':<5}{'NAME':<20}{'PRICE':<10}{'QUANTITY':<10}{'TOTAL':<12}")
    print("-"*75)
    
    for product in products:
        print(f"{product[0]:<5}{product[1]:<20}{product[2]:<12.2f}{product[3]:<12}{product[4]:<12.2f}")
    print("="*75)  

def search_product():
    name=input("Enter product name to search : ")
    cursor.execute(
        "SELECT * FROM products WHERE name=?",
        (name,)
    )
    product=cursor.fetchone()
    if product:
        print("\n"+"="*75)
        print("\t\t\t\tSEARCH RESULT")
        print("="*75)
        print(f"{'ID':<5}{'NAME':<20}{'PRICE':<12.2f}{'QUANTITY':<12}{'TOTAL':<12}")
        print("-"*75)
        print(f"{product[0]:<5}{product[1]:<20}{product[2]:<12.2f}{product[3]:<12}{product[4]:<12.2f}")
        print("="*75)
    
    else:
        print("product not found.")

def update_product():
    name=input("Enter product name to update : ")
    try:
        new_price=float(input("Enter new price :"))
    except ValueError:
        print("please Enter valid number")
        return
    if new_price<0:
        print("price cannot be negative.")
        return
    try:
        new_quantity=int(input("Enter new quantity : "))
    except ValueError:
        print("Please enter valid number.")
        return
    if new_quantity<0:
        print("quantity cannot be negative.")
        return
    new_total=new_price *new_quantity

    cursor.execute(
        "UPDATE products SET price = ?, quantity=?, total=? WHERE name=?",
        (new_price, new_quantity, new_total, name)
    )
    connection.commit()
    print("\nProduct updated successfully!")
    print("-"*40)

def delete_product():
    name=input("Enter product name to delete : ")
    cursor.execute(
        "DELETE FROM products WHERE name=?",
        (name,)
    )
    connection.commit()
    print("\nDeleted product successfully!")
    print("-"*40)

def total_inventory_value():
    cursor.execute("SELECT SUM(total) FROM products")
    result = cursor.fetchone()
    total_value = result[0]
    print("\n"+"="*50)
    print("\t\t\t\tSEARCH RESULT")
    print("="*50)
    print(f"Total inventory value: CHF {total_value:.2f}")
    print("-"*50)
    print("\nTotal Inventory Value:",total_value,"\n")

while True:
    print("\n"+"="*40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add product")
    print("2. View product")
    print("3. Serach product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Total Inventory Value")
    print("Exit")
    choice=input("Enter choice : ")
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

    elif choice=="7":
        print("-------EXIT-------")
        break

    else:
        print("Sorry, This is invalid option.\nPlease Enter choice again.")

connection.close()
