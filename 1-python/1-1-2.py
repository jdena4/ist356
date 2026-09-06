# Let' write a program to divide up the check among diners in a party.

# Write a program to input the amount of a restaurant check, tip %, and number of diners

# The program should output the total amount with tip, and the amount each diner owes.

check_amount = float(input("Enter the amount of the restaurant check: "))
tip_percentage = float(input("Enter the tip percentage (as a whole number): "))
number_of_diners = int(input("Enter the number of diners: "))

# Calculate the total amount with tip
tip_amount = check_amount * (tip_percentage / 100)
total_amount = check_amount + tip_amount

# Calculate the amount each diner owes
amount_per_diner = total_amount / number_of_diners

# Output the results
print(f"Total amount with tip: ${total_amount:.2f}")
print(f"Amount each diner owes: ${amount_per_diner:.2f}")

