# Homework 1
import pandas as pd

df=pd.read_csv('sales_data.csv')

grouped=df.groupby('Category')

# Task 1
# Total quantity sold
total_sold=grouped['Quantity'].agg('sum')
print(total_sold)

# Average price per unit
average_price=grouped['Price'].agg('mean')
print(average_price)

# Maximum quantity sold in a single transaction.
max_transaction=grouped['Price'].agg('max')
print(max_transaction)

#Task 2
# Identify the top-selling product in each category based on the total quantity sold
top_selling=grouped[['Product','Quantity']].agg('max')
print(top_selling)


# Task 3
# Find the date on which the highest total sales (quantity * price) occurred

# Quantity va Price ni int ga o‘tkazamiz
df['Quantity'] = df['Quantity'].astype(int)
df['Price'] = df['Price'].astype(int)

# Har bir qator uchun Total_Sales ni hisoblaymiz
df['Total_Sales'] = df['Quantity'] * df['Price']

# Har bir sana bo‘yicha jami Total_Sales ni yig‘amiz
daily_sales = df.groupby('Date')['Total_Sales'].sum()

# Eng katta jami savdoni topamiz
max_sales = daily_sales.max()

# Eng katta jami savdo bo‘lgan sana(s) ni topamiz
max_sales_dates = daily_sales[daily_sales == max_sales].index.tolist()

print("Eng yuqori jami savdo bo‘lgan sana(s):", max_sales_dates)
print("Savdo summasi:", max_sales)


# Homework 2
import pandas as pd
df=pd.read_csv('customer_orders.csv')

grouped=df.groupby('CustomerID')

# filter out customers who have made less than 20 orders
less_20_orders=grouped['Quantity'].agg('sum')
less_20_orders=less_20_orders[less_20_orders<20]
# print(less_20_orders)

# Identify customers who have ordered products with an average price per unit greater than $120.

# 1. Quantity va Price ustunlarini kerakli turga o'zgartiramiz (ixtiyoriy, agar kerak bo‘lsa)
df['Quantity'] = df['Quantity'].astype(int)
df['Price'] = df['Price'].astype(float)

# 2. Har bir customer bo'yicha o'rtacha narxni hisoblaymiz
avg_price_per_customer = df.groupby('CustomerID')['Price'].mean()

# 3. $120 dan yuqori o'rtacha narxga ega bo'lgan mijozlarni aniqlaymiz
customers_above_120 = avg_price_per_customer[avg_price_per_customer > 120]

# 4. Natijani chiqaramiz
# print(customers_above_120)


# Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 unit

total_quantity_and_price=df.groupby('Product')[['Quantity','Price']].agg({'Quantity':'sum','Price':'sum'})
total_quantity_and_price=total_quantity_and_price[total_quantity_and_price['Quantity']<5]
print(total_quantity_and_price)



# Homework 3
import sqlite3
import pandas as pd

# 1. SQLite bazasiga ulanish
conn = sqlite3.connect('population.db')

# 2. SQL so'rovda CASE WHEN yordamida SalaryBand ustunini qo'shamiz
query = """
SELECT *,
  CASE 
    WHEN salary <= 200000 THEN 'Band1'
    WHEN salary <= 400000 THEN 'Band2'
    WHEN salary <= 600000 THEN 'Band3'
    WHEN salary <= 800000 THEN 'Band4'
    WHEN salary <= 1000000 THEN 'Band5'
    WHEN salary <= 1200000 THEN 'Band6'
    WHEN salary <= 1400000 THEN 'Band7'
    WHEN salary <= 1600000 THEN 'Band8'
    WHEN salary <= 1800000 THEN 'Band9'
    ELSE 'Band10'
  END AS SalaryBand
FROM population
"""

# 3. So‘rovni bajarib, natijani DataFrame ko‘rinishida olish
population_df = pd.read_sql_query(query, conn)

# 4. Bog‘lanishni yopish
conn.close()

# 5. Natijani ko‘rish
# print(population_df.head())

def per_category(s):
    return (s / total_population) * 100

# Umumiy aholining soni (id bo‘yicha emas, real soni bo‘lishi kerak)
total_population = len(population_df)

# Har bir SalaryBand uchun odamlar soni
grouped = population_df['SalaryBand'].value_counts()

# Har bir toifa bo‘yicha foiz
percentage = grouped.apply(per_category)

# Natijani chiqarish
# print(percentage)

# Average salary in each salary category
average_salary=population_df.groupby('SalaryBand')['salary'].agg('mean')
# print(average_salary)

# Median salary in each salary category
median_salary=population_df.groupby('SalaryBand')['salary'].agg('median')
# print(median_salary)

# Number of population in each salary category
number_population_category=population_df['SalaryBand'].value_counts()
# print(number_population_category)

# Har bir State uchun o'rtacha odamlar soni
population_each_state=population_df.groupby('state')['state'].value_counts()
percentage_state=population_each_state.apply(per_category)
# print(percentage_state)

# Median population in each state
average_state=population_df.groupby('state')['salary'].agg('mean')
# print(average_state)

# Median population in each state
median_state=population_df.groupby('state')['salary'].agg('median')
# print(median_state)


# Har bir State uchun  odamlar soni
numeber_each_state=population_df.groupby('state')['state'].value_counts()
# print(numeber_each_state)
