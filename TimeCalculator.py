# Time Calculator
# CSC500 - Criticial Assignment #3 

# Get the current time in hours 
timeNow = int(input("Enter the current time (in hours from 0 to 23): "))

# Get the number of hours to wait for alarm
numHoursWait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the alarm time by calculating the modulus
total = timeNow + numHoursWait
newTotal = total % 24

# Display the time alarm will go off
print("If it is currently {} and you set your alarm to go off in {} hours, it will be {}.".format(timeNow,numHoursWait, newTotal))

