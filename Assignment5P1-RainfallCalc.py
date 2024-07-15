# Prompt user for the number of years
years = int(input("Enter number of years: "))

# Initialize the total_rainfall and total_month counter
total_rainfall = 0
total_months = 0

for year in range(1, years + 1):
    print(f"Year {year}")
    for month in range(1, 13):
        rainfall = float(input(f"Enter the amount of rainfall (in inches) for month {month}: "))
        total_rainfall = total_rainfall + rainfall
        total_months += 1

# Calculate average rainfall with division by 0 error handling
if total_months > 0:
    average_rainfall = total_rainfall / total_months
else:
    average_rainfall = 0

# Print the results
print("\nRainfall Stats:")
print(f"Total number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
