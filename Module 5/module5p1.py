# Module 5 Critical Thinking Assignment Part 1
# This program uses nested loops to collect data and calculate the average rainfall over a period of years
def average_rainfall_years():
    # The program should first ask for the number of years 
    years = int(input("The number of years? "))
    # the total inches of the rain fall 
    inches = 0
    # the total number of months 
    months = years * 12 
    # The outer loop will iterate once for each year 
    for years in range(1, years + 1):
        print(f"Year {years}:")
        # The inner loop will iterate twelve times once for each month 
        for month in range(1, 13):
            # Each iteration of the inner loop will ask the user for the inches of rainfall for that month 
            rainfall = int(input(f"How many inches of rainfall for month {month}: "))
            inches += rainfall

    # Calculate the average rainfall over a period of years 
    if months <= 0: 
        average_rainfall = 0
    else: 
        average_rainfall = inches/months 

    # The program should display the number of months, the total inches of rainfall and the average rainfall per month for the entire period 
    print("Number of months: ", months)
    print("Total of inches of rain fall: ", round(inches,2))
    print("The average rainfall per month for the entire period: ", round(average_rainfall,2))

# This would call the function to run the program for the first part of Module 5
average_rainfall_years()