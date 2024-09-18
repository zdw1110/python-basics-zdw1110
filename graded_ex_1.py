products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))

def display_products(products_list):
    for idx, (product, price) in enumerate(products_list, start=1):
        print(f"{idx}. {product} - ${price}")

def display_categories():
    print("Categories:")
    for idx, category in enumerate(products.keys(), start=1):
        print(f"{idx}. {category}")
    try:
        category_index = int(input("Please select a category by number: ")) - 1
        if 0 <= category_index < len(products):
            return category_index
        else:
            print("Invalid category number. Try again.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    for item in cart:
        product_name, price, quantity = item
        item_total = price * quantity
        print(f"{product_name} - ${price} x {quantity} = ${item_total}")
        total_cost += item_total
    print(f"Total cost: ${total_cost}")
    return total_cost


def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}\nEmail: {email}")
    print("Items Purchased:")
    for product_name, price, quantity in cart:
        print(f"{quantity} x {product_name} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)


def validate_email(email):
    return "@" in email and email.count("@") == 1

def main():
    cart = []
    
    while True:
        name = input("Enter your name (first and last name): ")
        if validate_name(name):
            break
        print("Invalid name. Please enter a valid first and last name.")
    
    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            break
        print("Invalid email. Please enter a valid email.")

    while True:
        category_index = display_categories()
        if category_index is None:
            continue
        
        selected_category = list(products.keys())[category_index]
        products_list = products[selected_category]
        
        while True:
            display_products(products_list)
            
            print("\n1. Select a product to buy")
            print("2. Sort products by price")
            print("3. Go back to categories")
            print("4. Finish shopping")
            
            choice = input("Select an option: ")
            
            if choice == '1': 
                try:
                    product_choice = int(input("Enter the product number: ")) - 1
                    if 0 <= product_choice < len(products_list):
                        product = products_list[product_choice]
                        quantity = int(input(f"How many {product[0]}s would you like to buy? "))
                        if quantity > 0:
                            add_to_cart(cart, product, quantity)
                        else:
                            print("Invalid quantity.")
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
            elif choice == '2':  
                sort_order = input("Enter 1 for ascending or 2 for descending: ")
                if sort_order == '1':
                    products_list = display_sorted_products(products_list, "asc")
                elif sort_order == '2':
                    products_list = display_sorted_products(products_list, "desc")
                else:
                    print("Invalid sort order.")
                    
            elif choice == '3':  
                break
                
            elif choice == '4':  
                if cart:
                    display_cart(cart)
                    address = input("Enter your delivery address: ")
                    total_cost = display_cart(cart)
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something next time!")
                return
            
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()