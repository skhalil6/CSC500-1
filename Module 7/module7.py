# Module 7 Critical Thinking Assignment 
# This program creates 3 dictionaries which revolve around courses, room numbers, instructors and meeting time. 
# After the three dictionaries are created, the program lets the user enter a course number to which then it would display the corresponding room number, instructor and meeting time 

# Key-Value Pairs: Room Number 
room_number = {
    "CSC101" : "3004",
    "CSC102" : "4501",
    "CSC103" : "6755",
    "NET110" : "1244", 
    "COM241" : "1411"
}

# Key-Value Pairs: Instructors 
instructors = {
    "CSC101" : "Haynes",
    "CSC102" : "Alvarado",
    "CSC103" : "Rich",
    "NET110" : "Burke", 
    "COM241" : "Lee"
}

# Key-Value Pairs: Meeting Time 
meeting_time = {
    "CSC101" : "8:00 a.m.",
    "CSC102" : "9:00 a.m.",
    "CSC103" : "10:00 a.m.",
    "NET110" : "11:00 a.m.", 
    "COM241" : "1:00 p.m."
}

# Function that asks for the user input and then display the outcome 
def course_number():
    course = input("Enter a course number: ")
    if course in room_number: 
        room = room_number[course]
        instructor = instructors[course]
        time = meeting_time[course]

        print(f"Room Number: {room}")
        print(f"Instructor: {instructor}")
        print(f"Meeting time: {time}")
    else:
        print(f"Course does not exist. Please try again!")

# This would call the function to run the program for Module 7 
course_number()