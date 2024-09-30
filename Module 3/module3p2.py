# Module 3 Critical Thinking Assignment Part 1
# This program sets an alarm to go off for a 24-hour clock 
# Function that does the calculation the program is being asked to do
def alarm():
    current_time = int(input("Enter the current time in hours: "))

    # This makes sure that the current time is within the 24 hour clock range 
    if current_time < 0 or current_time > 23:
        print("Time is not within the 24 hour clock range! Please try again by inserting a value between 0 to 23")
        return 
    
    # Asks for the number of hours to wait for the alarm 
    time = int(input("Set the time for the alarm to go off in: "))

    # Calculates the time the alarm to go off in within the 24-hour clock
    alarm_time = (current_time + time) % 24

    # Displays the alarm time 
    print(f"It is currently {current_time} and you set your alarm to go off in {time} hours, it will be {alarm_time}")

# This would call the function to run the program for the second part of Module 3
alarm()

