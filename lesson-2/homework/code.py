# Task 1
name=input("Enter the name")
year=int(input("Enter the year of your birth"))

print(f'Your name is {name} and you are {2025-year} years old')

# Task 2
txt = 'LMaasleitbtui'

car1=txt[::2]
print(car1)

car2=txt[1::2]
print(car2)

# Task 3
txt = 'MsaatmiazD'

car1 =txt[::2]
print(car1)
car2=txt[-1::-2]
print(car2)

#Task 4
txt = "I'am John. I am from London"

area1=txt[20::]
print(area1)

#Task 5
word=input("Enter the any word")
print(word[::-1])

#Task 6
word=input("Enter the word")
num=0
vowels=['a','i','u','o','e']
for x in word:
    if x.lower() in vowels:
        num+=1
print(word)
print(f'There are {num} vowels in word')

#Task 7
num=(input("Enter the numbers with , "))
num=num.split(',')
print(max(num))

#Task 8
word=input("Enter the word")

if word==word[::-1]:
    print("Palindrome")
else:
    print("Not polindrome")

#Task 9
email=input("Enter the email")
index=email.find("@")+1
print(email[index::])

#Task 10
I can't
