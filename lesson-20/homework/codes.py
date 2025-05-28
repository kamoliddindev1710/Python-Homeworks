import pandas as pd
import sqlite3
conn = sqlite3.connect('chinook.db')
query='Select * from Invoice'
invoice_df=pd.read_sql_query(query,conn)

# Find the total amount spent by each customer on purchases (considering invoices)
total_purchase_per_customer=invoice_df.groupby('CustomerId')['Total'].agg('sum')
# print(total_purchase_per_customer)

# Identify the top 5 customers with the highest total purchase amounts
highs_purchase_5_customers=invoice_df.groupby('CustomerId')['Total'].agg('sum').sort_values(ascending=False).head(5)
# print(highs_purchase_5_customers)

# Display the customer ID, name, and the total amount spent for the top 5 customers
query_customer='select * from customer'
customer_df=pd.read_sql_query(query_customer,conn)
new_df=invoice_df.merge(customer_df,how='inner',on='CustomerId')
info_about_5_customers=new_df.groupby(['CustomerId','FirstName'])['Total'].agg('sum').reset_index()
info_about_5_customers=info_about_5_customers.sort_values(by='Total',ascending=False).head(5)
print(info_about_5_customers[['CustomerId','FirstName','Total']])

