from pathlib import Path
import csv

def calculate_highest_overhead():
    # Create a file to csv file
    fp = Path.cwd()/"C:/kelly/TEAM C/overheads-day-90.csv"

    # Initialize variables for total overheads, highest expense, and highest amount
    total_overheads = 0
    highest_expense = ""
    highest_amount = 0

    # Read the CSV file
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            # Extract category and amount from the row
            category, amount_str = row

            # Convert any integer to a float
            amount = float(amount_str)
            # Add the amount to the total overheads
            total_overheads += amount
            # If amount is more than the highest_amount
            if amount > highest_amount:
                highest_amount = amount
                highest_expense = category

    # Calculate the percentage
    highest_percentage = (highest_amount / total_overheads) * 100 if total_overheads > 0 else 0

    # Format and return the output
    return f"[HIGHEST OVERHEAD] {highest_expense}: {highest_percentage:.2f}%"

# Usage
output = calculate_highest_overhead()
print(output)
