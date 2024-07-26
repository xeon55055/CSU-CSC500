# Assignment 7- Jonathan

# Three dictionaries for course information
course_room = {
    'CSC101': 3004,
    'CSC102': 4501,
    'CSC103': 6755,
    'NET110': 1244,
    'COM241': 1411
}

course_instructor = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

course_time = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# Get Course Info Custom Function
def get_course_info(course_number):
    if course_number in course_room:
        room = course_room[course_number]
        instructor = course_instructor[course_number]
        time = course_time[course_number]
        print(f"Room Number: {room}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {time}")
    else:
        print("Course not found")


# Main function
course_number = input("Enter a course number (e.g., CSC103): ")
get_course_info(course_number)

