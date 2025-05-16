#task 1
import sqlite3

with sqlite3.connect('Table.db') as connection:
    cursor=connection.cursor()
    create_table="""Create Table Roster(
    Name Text,
    Species Text,
    Age INT);"""
    cursor.execute(create_table)
    connection.commit()


#task 2
import sqlite3
insert_query=(
('Benjamin Sisko',	'Human',	40),
('Jadzia Dax',	'Trill',	300),
('Kira Nerys',	'Bajoran',	29)
)


connection=sqlite3.connect('Table.db')
cursor=connection.cursor()
cursor.executemany('insert into Roster values(?,?,?)',insert_query)
connection.commit()
connection.close()


#task 3
import sqlite3

connection=sqlite3.connect('Table.db')
cursor=connection.cursor()
update_query="""Update  Roster
Set Name='Ezri Dax' 
where Name='Jadzia Dax' """
cursor.execute(update_query)
connection.commit()
connection.close()


#task 4
import sqlite3

connection=sqlite3.connect('Table.db')
cursor=connection.cursor()
display_query="""Select * from Roster where Species='Bajoran'"""
result=cursor.execute(display_query)
connection.commit()
print(result.fetchall())
connection.close()
