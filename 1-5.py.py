import pandas as pd

# Read the CSV file with the modified date format
df = pd.read_csv("sales_data_1.csv", parse_dates=["Date"], dayfirst=True, date_parser=lambda x: pd.to_datetime(x, format="%d/%m/%y"))

overall_gross_margin = (df["Selling price"] - df["Buying price"]).sum()

vendor_profit = df.groupby("Firm bought from")["Selling price"].sum() - df.groupby("Firm bought from")["Buying price"].sum()
most_profitable_vendor = vendor_profit.idxmax()

customer_profit = df.groupby("Customer")["Selling price"].sum() - df.groupby("Customer")["Buying price"].sum()
least_profitable_customer = customer_profit.idxmin()

df["Day of Week"] = df["Date"].dt.day_name()
day_profit = df.groupby("Day of Week")["Selling price"].sum() - df.groupby("Day of Week")["Buying price"].sum()
most_profitable_day = day_profit.idxmax()
least_profitable_day = day_profit.idxmin()

print("1. Overall Gross Margin:", overall_gross_margin)
print("2. Most Profitable Vendor:", most_profitable_vendor)
print("3. Least Profitable Customer:", least_profitable_customer)
print("4. Most Profitable Day of the Week:", most_profitable_day)
print("5. Least Profitable Day of the Week:", least_profitable_day)
