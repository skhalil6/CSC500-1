# Module 8: Portfolio Project
# Module 4: Portfolio Milestone 
# Step 1: Build the ItemToPurchase class 
class ItemToPurchase: 
    # default constructor 
    def __init__(self, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    # a method for printing data members 
    # example of print_item_cost() output: Bottled Water 10 @ $1 = $10
    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${cost}")

    # a method for printing item description 
    def print_item_description(self):
        print(f"{self.item_name} : {self.item_description}")

# Module 6: Portfolio Milestone 
# Step 4: Build the ShoppingCart class 
class ShoppingCart: 
    # default constrcutor 
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything 
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    # removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything 
    def remove_item(self, ItemName):
        for item in self.cart_items: 
            if item.item_name == ItemName:
                self.cart_items.remove(item)
                return
        # if item name cannot be found, output this message: Item not found in cart. Nothing removed. 
        print("Item not found in cart. Nothing removed")

    # modifies an item's description, price and/or quantity. Has parameter ItemToPurchase. Does not return anything 
    def modify_item(self, ItemToPurchase):
        # if item can be found (by name) in cart, check if parameter has default values for description, price and quantity. If not, modify item in cart.
        for item in self.cart_items: 
            if item.item_name == ItemToPurchase.item_name:
                if ItemToPurchase.item_description != "none":
                    item.item_description = ItemToPurchase.item_description
                if ItemToPurchase.item_price != 0.0: 
                    item.item_price = ItemToPurchase.item_price
                if ItemToPurchase.item_quantity != 0: 
                    item.item_quantity = ItemToPurchase.item_quantity
                return
        # if item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
        print("Item not found in cart. Nothing modified.")

    # Returns quantity of all items in cart. Has no parameters 
    def get_num_items_in_cart(self):
        quantity = 0
        for item in self.cart_items:
            quantity += item.item_quantity
        return quantity
    
    # Determines and returns the total cost of items in cart. Has no parameters
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity 
        return total_cost
        
    # outputs total of objects in cart. 
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of items: {self.get_num_items_in_cart()}")
        # if cart is empty, output this message: SHOPPING CART IS EMPTY 
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else: 
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

    # Outputs each item's description 
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

# Step 5 and Step 6: Implementing the print_menu() function and implementing Output shopping cart menu option 
# print_menu() has a ShoppingCart parameter and outputs a menu of options to manipulate the shopping cart. 
def print_menu(shopping_cart):
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

    user_input = ""
    while user_input != "q":
        user_input = input("Choose an option:\n")
        # Step 8: implement Add item to cart menu option 
        if user_input == "a":
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(item_name, item_description, item_price, item_quantity) # creating an item 
            shopping_cart.add_item(item) # adding item to cart 
        # Step 9: implement remove item menu option 
        elif user_input == "r":
            item_name = input("Enter the item name:\n")
            shopping_cart.remove_item(item_name) # removing item from cart 
        # Step 10: implement Change item quantity menu option. Hint: Make new ItemToPurchase object before using ModifyItem() method 
        elif user_input == "c":
            item_name = input("Enter the item name:\n")
            item_quantity = int(input("Enter the new item quantity:\n"))
            changed_quantity = ItemToPurchase(item_name=item_name, item_quantity=item_quantity)
            shopping_cart.modify_item(changed_quantity) # modifies the item in cart 
        elif user_input == "i":
            shopping_cart.print_descriptions()
        elif user_input == "o":
            shopping_cart.print_total()
        elif user_input != "q":
            print("Please enter a valid input and try again.")


    

# Step 7: prompt the user for a customer's name and today's date. Output the name and date  
def main(): 
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")
    # Step 7: creating an object of type ShoppingCart 
    shopping_cart = ShoppingCart(customer_name, current_date)

    # Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class 
     # create two objects of the ItemToPurchase class 
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()
    
    # prompt the user for two items 
    print("Item 1")
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = float(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))
    firstItemCost = item1.item_price * item1.item_quantity
    shopping_cart.add_item(item1)
    print("Item 2")
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = float(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))
    secondItemCost = item2.item_price * item2.item_quantity
    shopping_cart.add_item(item2)

    # Step 3: Add the costs of the two items together and output the total cost 
    total_cost = firstItemCost + secondItemCost
    print("\nTOTAL COST")
    # outputs the two items cost 
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"Total: ${total_cost}")
    
    print_menu(shopping_cart)
    
 
# this would call the function to run the program for Module 4
main()