# Store name
shop_name = "Manhattan Bean Co."

# Number of drinks sold
# Coffee + Tea + Drinking Chocolate
drinks_sold = 166000

# Price per drink
price_per_drink = 3.25

# Number of pastries sold
# Bakery category
pastries_sold = 32800

# Price per pastry
price_per_pastry = 3.40

# Revenue calculation
drink_revenue = drinks_sold * price_per_drink
pastry_revenue = pastries_sold * price_per_pastry
total_revenue = drink_revenue + pastry_revenue

# Check total revenue
if total_revenue >= 500:
    print("Excellent! Total revenue has reached or exceeded the $500 target.")
else:
    print("Total revenue has not yet reached the $500 target.")

# Print the sales analysis
print("=" * 40)
print(f"Sales Analysis Report: {shop_name}")
print("=" * 40)
print(f"Total drinks sold: {drinks_sold:,} units")
print(f"Drink revenue: ${drink_revenue:,.2f}")
print(f"Total pastries sold: {pastries_sold:,} units")
print(f"Pastry revenue: ${pastry_revenue:,.2f}")
print("-" * 40)
print(f"Total overall revenue: ${total_revenue:,.2f}")

# Data for recommendations
# 1. Sustain the growth trend: monthly transaction data (Jan-Jun 2023)
total_transactions = 149116
monthly_transactions = [17314, 16359, 21229, 25335, 33527, 35352]
months = ["January", "February", "March", "April", "May", "June"]
growth_rate = (monthly_transactions[-1] - monthly_transactions[1]) / monthly_transactions[1] * 100

# 2. Optimize the morning rush: 8-10 AM peak period data
morning_rush_transactions = 41750
morning_rush_share = morning_rush_transactions / total_transactions * 100

# 3. Increase items per transaction: order size breakdown
single_item_orders = 87159
two_item_orders = 58642
single_item_pct = single_item_orders / total_transactions * 100
two_item_pct = two_item_orders / total_transactions * 100
small_order_pct = (single_item_orders + two_item_orders) / total_transactions * 100

# Print supporting data for each recommendation
print("\n" + "=" * 40)
print("Data Supporting Recommendations")
print("=" * 40)

print("\n1. Sustain the growth trend")
for month, count in zip(months, monthly_transactions):
    print(f"   {month}: {count:,} transactions")
print(f"   Feb-to-Jun growth: {growth_rate:.1f}%")

print("\n2. Optimize the morning rush")
print(f"   Total transactions: {total_transactions:,}")
print(f"   8-10 AM peak transactions: {morning_rush_transactions:,}")
print(f"    Peak period share: {morning_rush_share:.1f}% of all transactions")

print("\n3. Increase items per transaction")
print(f"   1-item orders: {single_item_orders:,} ({single_item_pct:.1f}%)")
print(f"   2-item orders: {two_item_orders:,} ({two_item_pct:.1f}%)")
print(f"   1-2 item orders total: {small_order_pct:.1f}% of all orders")
print("   Most customers buy 1 or 2 items — strong upsell opportunity.")

# Print the contents of the written text file
with open("assignment1_salesAnalysis/sales_analysis.txt", "r", encoding="utf-8") as file: 
    content = file.read()
print(content)
