# Module 5 Critical Thinking Assignment Part 2
# This program asks the user to enter the number of books that they have purchased this month and then display the number of points awarded 
def points_awarded(): 
    # Asks the user to enter the number of book purchased this month 
    student_book_purchased = int(input("Enter the number of books purchased this month: "))
    # Based off of the CSU Global Bookstore book club points 
    if student_book_purchased == 0: 
        points = 0
    elif student_book_purchased == 2:
        points = 5
    elif student_book_purchased == 4:
        points = 15
    elif student_book_purchased == 6:
        points = 30
    elif student_book_purchased >= 8: 
        points = 60
    else:
        points = 0 
        print("Retry entering the number of book you have purchased this month with the digits: 0, 2, 4, 6, 8")
    
    # Display the numberof points awarded
    print(f"You have earned {points} points this month!")

# This would call the function to run the program for the second part of Module 5
points_awarded()