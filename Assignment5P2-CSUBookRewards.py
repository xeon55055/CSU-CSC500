# Ask user for number of books purchased
books_purchased = int(input("Enter the number of books you have purchased this month: "))

# Determine points based on number of books purchased
if books_purchased == 0 or books_purchased == 1:
    points_earned = 0
elif books_purchased == 2 or books_purchased == 3:
    points_earned = 5
elif books_purchased == 4 or books_purchased == 5:
    points_earned = 15
elif books_purchased == 6 or books_purchased == 7:
    points_earned = 30
elif books_purchased >= 8:
    points_earned = 60
else:
    points_earned = 0


# Print the number of points awarded
print(f"You've earned a total of {points_earned} points this month.")

