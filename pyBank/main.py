import os as os
import pandas as pd

# Create file path
file_path = "C:\\Users\\andre\\Documents\\WashU\\WASHSTL201806DATA4-Class-Repository-DATA\\Week 3 - Python\\Homework\\PyBank\\Resources\\budget_data.csv"

# Import CSV file as Pandas dataframe
df = pd.read_csv(file_path)

# Look at the data structure
df.head()

# Calculate the number of months in the dataset
number_of_months = len(df["Date"].unique())
number_of_months

# Calculate the total P&L by adding up the monthlies
pnl = df["Revenue"].sum()
print(pnl)

# Create a new column that calculates the monthly change in P&L
df["Monthly Revenue Change"] = df["Revenue"].diff()
df.head()
df.tail()

# Calculate the average monthly change in P&L
average_pnl_change = df["Monthly Revenue Change"].mean()
print(average_pnl_change)

# Calculate the smallest and largest monthly changes in P&L
greatest_increase = df["Monthly Revenue Change"].max()
greatest_decrease = df["Monthly Revenue Change"].min()
print(greatest_increase)
print(greatest_decrease)

# Print a summary of the calculations
print("Financial Analysis")
print("------------------------------------------------------------")
print("Total Months: " + str(number_of_months))
print("Total: $" + str(pnl))
print("Average Monthly Change: $" + str(average_pnl_change))
print("Greatest Increase in Profits: $" + str(greatest_increase))
print("Greatest Decrease in Profits: $" + str(greatest_decrease))

# Create a text file with the summary and save it
with open("pyBank_Summary.txt", "w") as text_file:
    print(f"Financial Analysis", file=text_file)
    print(f"------------------------------------------------------------", file=text_file)
    print(f"Total Months: {str(number_of_months)}", file=text_file)
    print(f"Total: $ {str(pnl)}", file=text_file)
    print(f"Average Monthly Change: $ {str(average_pnl_change)}", file=text_file)
    print(f"Greatest Increase in Profits: $ {str(greatest_increase)}", file=text_file)
    print(f"Greatest Decrease in Profits: $ {str(greatest_decrease)}", file=text_file)
    