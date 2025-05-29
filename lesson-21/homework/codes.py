# Homework 1
import pandas as pd
from matplotlib import pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
# df1

# Calculate the average grade for each student
df1['Average']=(df1['Math']+df1['English']+df1['Science'])/3
df1['Average']

# Find the student with the highest average grade
highest_grade=df1.sort_values(by='Average',ascending=False).head(1)
highest_grade

# Create a new column 'Total' representing the total marks obtained by each student
df1['Total']=df1['Math']+df1['English']+df1['Science']
df1

# Plot a bar chart to visualize the average grades in each subject
plt.bar(df1['Student_ID'],df1['Average'])

# Homework 2
import pandas as pd
from matplotlib import pyplot as plt
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
df2
# Calculate the total sales for each product
total_sales=df2[['Product_A','Product_B','Product_C']].agg('sum')
total_sales

#  Find the date with the highest total sales
df2['Total_sale']=df2['Product_A']+df2['Product_B']+df2['Product_C']
High_sale_date=df2.sort_values(by='Total_sale',ascending=False).head(1)
High_sale_date['Date']

# Calculate the percentage change in sales for each product from the previous day
percentage_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
percentage_change = percentage_change.round(2)
percentage_change

# Plot a line chart to visualize the sales trends for each product over time
df2
plt.figure(figsize=(10, 6))
plt.plot(df2['Date'], df2['Product_A'], label='Product A', marker='o')
plt.plot(df2['Date'], df2['Product_B'], label='Product B', marker='s')
plt.plot(df2['Date'], df2['Product_C'], label='Product C', marker='^')

# Homework 3

import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Calculate the average salary for each department
average_salary=df3.groupby('Department')['Salary'].agg('mean')
average_salary

# Exercise 2: Find the employee with the most experience.
most_experience=df3.sort_values(by='Experience (Years)',ascending=False).head(1)
most_experience

# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.
min_salary=df3['Salary'].min()
df3['Salary Increase']=((df3['Salary']-min_salary)/df3['Salary']).round(2)
df3

# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.
department_counts = df3['Department'].value_counts()

# Plot the bar chart
plt.figure(figsize=(8, 6))
department_counts.plot(kind='bar', color='skyblue', edgecolor='black')

# Homework 4
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# Calculate the total revenue from all orders
total_revenue=df4['Total_Price'].sum()
total_revenue

# Exercise 2: Find the most ordered product
most_ordered=df4.groupby('Product')['Quantity'].agg('count')
most_ordered=most_ordered.sort_values(ascending=False).head(1)
most_ordered

# Exercise 3: Calculate the average quantity of products ordered
average_quantity=df4['Quantity'].agg('sum')/3
average_quantity

# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products
plt.figure(figsize=(8, 6))
department_counts.plot(kind='bar', color='skyblue', edgecolor='black')
