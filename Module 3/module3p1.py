# Module 3 Critical Thinking Assignment Part 1
# This program calculates the total amount of a meal purchased at a restaurant. 
# Function that does the calculation the program is being asked to do
def calculate_meal_purchased():
    meal_purchased = int(input("Enter the charge for the food: $"))

    # Adds the 18% tip to the meal purchased
    tip = meal_purchased * 0.18


    # Adds the 7% sales tax to the meal purchased
    tax = meal_purchased * 0.07 

    # Calculates the total amount of a meal purchased at a restaurant 
    total_amount = meal_purchased + tip + tax

    # Displays each of these amounts and the total price 
    print("Meal Purchased: $", meal_purchased)

    # Made the tip stop after 2 decimal placements as it keeps going otherwise when most restaurants stop at two decimal places 
    print("Tip of 18%: $", round(tip,2))

    # Made the sales tax stop after 2 decimal placements as it keeps going otherwise when most restaurants stop at two decimal places
    print("Sales Tax of 7%: $", round(tax,2))
    
    print("Total Amount of a Meal Purchased: $", total_amount)

# This would call the function to run the program for the first part of Module 3 
calculate_meal_purchased()

