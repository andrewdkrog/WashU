import os as os
import pandas as pd

file_path = "C:\\Users\\andre\\Documents\\WashU\\WASHSTL201806DATA4-Class-Repository-DATA\\Week 3 - Python\\Homework\\PyBank\\Resources\\budget_data.csv"
df = pd.read_csv(file_path)

df.head()
number_of_months = len(df["Date"].unique())
number_of_months

pnl = df["Revenue"].sum()
print(pnl)

df["Monthly Revenue Change"] = df["Revenue"].diff()
df.head()
df.tail()
average_pnl_change = df["Monthly Revenue Change"].mean()
print(average_pnl_change)

greatest_increase = df["Monthly Revenue Change"].max()
greatest_decrease = df["Monthly Revenue Change"].min()
print(greatest_increase)
print(greatest_decrease)

print("Financial Analysis")
print("------------------------------------------------------------")
print("Total Months: " + str(number_of_months))
print("Total: $" + str(pnl))
print("Average Monthly Change: $" + str(average_pnl_change))
print("Greatest Increase in Profits: $" + str(greatest_increase))
print("Greatest Decrease in Profits: $" + str(greatest_decrease))
