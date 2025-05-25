# Homework 1
import pandas as pd

# Ma'lumotlar dataframega aylantirildi
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Firt Name va age ustunlari nomlar mos ravishda alishtirildi
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

# Dataframening boshidan 3 qator chiqarildi
print(df.head(3))

# O'ratcha yosh topildi
mean_of_age=df['age'].mean()
print(mean_of_age)

# First_name va City nomlari chiqarildi
name_and_city=df[['first_name','City']]
print(name_and_city)

# Yangi Salary nomli ustun qo'shildi
df['Salary']=[300,200,400,600]
print(df)

# Dataframening yakuniy barcha statistikasi ko'rsatildi
info=df.describe()
print(info)


# Homework 2
import pandas as pd

# Ma'lumotlar dataframega aylantirildi
data={'Month':['Jan','Feb','Mar','Apr'],'Sales':[5000,6000,7500,8000],'Expenses':[3000,3500,4000,4500]}
df=pd.DataFrame(data)
print(df)

# Sales va Expenses ustunlarining maksimum qiymatlari topildi va chiqarildi
max_sales=df['Sales'].max()
max_expenses=df['Expenses'].max()
print(f'Max Sales: {max_sales} \nMax Expenses: {max_expenses}')

# Sales va Expenses ustunlarining minimum qiymatlari topildi va chiqarildi
min_sales=df['Sales'].min()
min_expenses=df['Expenses'].min()
print(f'Min Sales: {min_sales} \nMin Expenses:{min_expenses}')


# Sales va Expenses ustunlarining o'rtacha  qiymatlari topildi va chiqarildi
avergae_sales=df['Sales'].mean()
average_expenses=df['Expenses'].mean()
print(f'Avergage Sales: {avergae_sales} \nAverage Expenses:{average_expenses}')


# Homework 3
import pandas as pd

# Ma'lumotlar dataframega aylantirildi
data={'Category':['Rent','Utilities','Groceries','Entertainment'],'January':[1200,200,300,150],'February':[1300,220,320,160],'March':[1400,240,330,170],'April':[1500,250,350,180]}
df=pd.DataFrame(data)
# print(df)

# Category ustunining unique malumotlari ajratib olindi
categories=df['Category'].unique()

# df Dataframening Category ustuni index qilib o'zgartirildi
changed_df=df.set_index('Category')

#Har bir category uchun malumotlar chiqarildi
for category in categories:
    row = changed_df.loc[category]
    max_value = row.max()
    min_value = row.min()
    average_value = row.mean()

    print(f"Max for {category}: {max_value}") # Har bir category uchun max qiymat
    print(f"Min for {category}: {min_value}") # Har bir category uchun min qiymat
    print(f"Average for {category}: {average_value}\n") # Har bir category uchun o'rtacha qiymat



