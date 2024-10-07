# Module 4: Portfolio Milestone 
# Step 1: Build the ItemToPurchase class 
class ItemToPurchase: 
    # default constructor 
    def  __init__(self): 
        # initialize item's name to none (string)
        self.item_name = "none"
        # initialize item's price (float)
        self.item_price = 0.0
        # initialize item's quantity to 0 (integer)
        self.item_quantity = 0

    # a method for printing data members 
    # example of print_item_cost() output: Bottled Water 10 @ $1 = $10
    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${cost}")


# Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class 
def main(): 
    # create two objects of the ItemToPurchase class 
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()
    
    # prompt the user for two items 
    print("Item 1")
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = float(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))
    firstItemCost = item1.item_price * item1.item_quantity
    print("Item 2")
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = float(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))
    secondItemCost = item2.item_price * item2.item_quantity

    # Step 3: Add the costs of the two items together and output the total cost 
    total_cost = firstItemCost + secondItemCost
    print("\nTOTAL COST")
    # outputs the two items cost 
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"Total: ${total_cost}")

# This would call the function to run the program for Module 4
main()


