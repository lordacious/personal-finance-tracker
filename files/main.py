import sys
from datetime import datetime

import pandas as pd

import matplotlib.pyplot as plt


#add transactions and request username
def user_input():
    current_date=datetime.now().strftime("%d/%m/%Y")
    income=float(input("Enter your income "))
    savings=float(input("How much did you save "))
    rent=float(input("Rent: "))
    transport=float(input("Transport "))
    shopping=float(input("Shopping "))
    miscellaneous=float(input("Miscelleneous e.g gave money to charity "))
    entertainment=float(input("Entertainment e.g did you have drinks or go out? "))
    expenses= rent + transport + shopping + miscellaneous + entertainment
    print("You spent "+ str(expenses))
    balance=income-expenses-savings
#   print("Your remaining balance is:",round(balance,2))
#   print("Date of transaction:",current_date)
#user_data=user_input() #call the function and store data
#print(user_data)

#Return a dictionary of daily data
    return{
        "date":current_date,
        "income":income,
        "savings":savings,
        "expenses":expenses,
        "balance":round(balance,2)
    }

monthly_data=[]
while True:
    #Get the data and add it to the list
    daily_data=user_input()
    monthly_data.append(daily_data)
    #ask user if they want to continue
    next_day=input("Do you want to enter data for another day?(Y/N):").strip().lower()
    if next_day!="y":
        break

def analyze_monthly_data(data):
    total_income=sum(day["income"]for day in data)
    total_savings=sum(day["savings"]for day in data)
    total_expenses=sum(day["expenses"]for day in data)
    total_balance=sum(day["balance"]for day in data)

    print("\n---Monthly data analysis---")
    print(f"Total income:{total_income}")
    print(f"Total Savings:{total_savings}")
    print(f"Total Expenses:{total_expenses}")
    print(f"End of Month Balance:{total_balance}")
    print("\n Daily Breakdown")
    for day in data:
        print(f"Date:{day['date']}, Balance:{day['balance']}")

analyze_monthly_data(monthly_data)

#ssave data to csv file
df=pd.DataFrame(monthly_data)
df.to_csv("monthly_finance_tracker.csv", index=False)
print("Data saved to monthly_finance_tracker.csv ")

#display graph
def tracker_graph(data):
   dates=[day["date"]for day in data]
   balances=[day["balance"]for day in data]

   plt.figure(figsize=(10,5))
   plt.plot(dates, balances, marker="o")
   plt.xlabel("Date")
   plt.ylabel("Balance")
   plt.title("Monthly Finance Tracker")
   plt.xticks(rotation=45)
   plt.show()
   
   save_to_csv=input("Do you want to save the graph to a file?(Y/N):").strip().lower()
   if save_to_csv=="y":
       plt.savefig("monthly_finance_tracker.png")
       print("Graph saved to monthly_finance_tracker.png")
tracker_graph(monthly_data)





#view transactions by date or category
#data analysis: monthly summary, category breakdown to show spending
##distibution by category
#data visulization use matlib for graphs
#data storage: store data in sqlite
#user authentication