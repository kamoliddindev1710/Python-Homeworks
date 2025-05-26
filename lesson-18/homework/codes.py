# Homework 2
import pandas as pd
from datetime import datetime

data = {
    "id": [332289, 2051744, 2225995, 5486226, 5515021],
    "creationdate": [
        "2008-12-01 21:24:44",
        "2010-01-12 19:31:47",
        "2010-02-09 00:51:38",
        "2011-03-30 12:26:50",
        "2011-04-01 14:50:44"
    ],
    "score": [3184, 420, 51, 7, 10],
    "viewcount": [5962784, 587728, 59922, 6393, 13744],
    "title": [
        "How do I change the size of figures drawn with...",
        "How to invert the x or y axis",
        "How can I create stacked line graph?",
        "Rolling median in python",
        "Compute a compounded return series in Python"
    ],
    "answercount": [14, 10, 4, 5, 3],
    "commentcount": [1, 3, 0, 4, 6],
    "favoritecount": [0.0, 0.0, 0.0, 0.0, 0.0],
    "quest_name": ["tatwright", "DarkAnt", "David Underhill", "yueerhu", "Jason Strimpel"],
    "quest_rep": [37837.0, 4211.0, 15936.0, 175.0, 14916.0],
    "ans_name": [None, "Demitri", "doug", "Mike Pennington", "Mike Pennington"],
    "ans_rep": [None, 13369.0, 69290.0, 42288.0, 42288.0]
}
 # Data dicti Dataframega aylantirildi
df=pd.DataFrame(data)

# CSV faylga yozish
df.to_csv('stackoverflow_data.csv', index=False)


# Dataframe modulidan kerakli ma'lumotlar olindi
fixed_year=datetime(year=2014,month=1,day=1,hour=0,minute=0,second=0)
fixed_year=datetime.strftime(fixed_year,'%Y %m %d %H %M %S')

# 2014 yildan kichiklari saralandi
criteria_1=df['creationdate'] < fixed_year
# print(df[criteria_1])

# Baholari 50 dan kattalar chiqarildi
criteria_2=df['score'].gt(50)
# print(df[criteria_2])

# Baholari 50 dan katta va 100 dan kichiklari chiqarildi
criteria_3=df['score'].between(50,100, inclusive="neither")
# print(df[criteria_3])


# Scott Boston tomoidan berilgan barcha javoblar chiqarildi
criteria_4=df['ans_name']=='Scott Boston'
# print(df[criteria_4])


# Hamma javob bergan savollar chiqarildi
criteria_5=df['answercount'].ge(5)
# print(df[criteria_5])

# Muddati 2014 yil Mart va Oktyabr oyida,javob beruvchi Unutba va bahosi 5 dan kichik bo'lgan rowlar ajratildi
df['creationdate'] = pd.to_datetime(df['creationdate'])
start_date = '2014-03-01'
end_date = '2014-10-31'
part_1=df['creationdate'].between(start_date,end_date,inclusive="both")
part_2=df['ans_name']=='Unutbu'
part_3=df['score'].lt(5)
criteria_6=part_1 & part_2 & part_3
# print(df[criteria_6])

# Bahosi 5 va 10 ning orasida so'ngra viewcounti 10000 dan yuqori bo'lgan rowlar chiqarildi
t1=df['score'].between(5,10,inclusive="both")
t2=df['viewcount'].gt(10000)
criteria_7=t1 | t2
# print(df[criteria_7])

# Javob beruvchining ismi Scott Boston bo'lmaganlar chiqarildi
criteria_8=df["ans_name"]!='Scott Boston'
# print(df[criteria_8])

# Homework 3
import pandas as pd

# Ma'lumotlarni dict ko‘rinishida berish
data = {
    "PassengerId": [1, 2, 3, 4, 5],
    "Survived": [0, 1, 1, 1, 0],
    "Pclass": [3, 1, 3, 1, 3],
    "Name": [
        "Braund, Mr. Owen Harris",
        "Cumings, Mrs. John Bradley (Florence Briggs Th.)",
        "Heikkinen, Miss. Laina",
        "Futrelle, Mrs. Jacques Heath (Lily May Peel)",
        "Allen, Mr. William Henry"
    ],
    "Sex": ["male", "female", "female", "female", "male"],
    "Age": [22.0, 38.0, 26.0, 35.0, 35.0],
    "SibSp": [1, 1, 0, 1, 0],
    "Parch": [0, 0, 0, 0, 0],
    "Ticket": ["A/5 21171", "PC 17599", "STON/O2. 3101282", "113803", "373450"],
    "Fare": [7.25, 71.2833, 7.925, 53.1, 8.05],
    "Cabin": [None, "C85", None, "C123", None],
    "Embarked": ["S", "C", "S", "S", "S"]
}

# DataFrame yaratish
titanic_df = pd.DataFrame(data)

# CSV faylga yozish
titanic_df.to_csv("titanic.csv", index=False)

# Jinis ayol kishi va yoshi 20 va 30 ning rasida bo'lgan kishilar chiqdi
a1=titanic_df['Sex']=='female'
a2=titanic_df['Age'].between(20,30,inclusive="both")
answer_1=a1 & a2
# print(titanic_df[answer_1])

# 100 $ dan ko'p to'laganlar kelib chiqdi
answer_2=titanic_df['Fare'].gt(100)
# print(titanic_df[answer_2])

# Tirik qolgan,aka uka va opa singillari,ota onasi bo'lmaganlar chiqarildi
b1=titanic_df['Survived']==1
b2=titanic_df['SibSp']==0
b3=titanic_df['Parch']==0
answer_3=b1 & b2 & b3
# print(titanic_df[answer_3])

# Embarked C bo'lgan va 50$ dan ko'p to'laganlar chiqarildi
c1=titanic_df['Embarked']=='C'
c2=titanic_df['Fare'].gt(50)
answer_4=c1 & c2
# print(titanic_df[answer_4])

# Aka ukalari va ota onasi bo'lganlar chiqarildi
d1=titanic_df['SibSp']==1
d2=titanic_df['Parch']==1
answer_5=d1 & d2
# print(titanic_df[answer_5])

# 15 yosh va undan kichik bo'lgan va tiriklar chiqarildi
e1=titanic_df["Age"].lt(15)
e2=titanic_df['Survived']==0
answer_6=e1 & e2
# print(titanic_df[answer_6])

# 200$ dan ko'p to'lagan kishilar chiqdi
answer_7=titanic_df['Fare'].gt(200)
# print(titanic_df.loc[answer_7,['Name','Cabin','Fare']])

# PassengerId si toq bo'lganlar chiqdi
answer_8=titanic_df['PassengerId']%2!=0
# print(titanic_df[answer_8])

# Har bir ticket qiymatining takrorlanmaganlarini ajratish
answer_9 = ~titanic_df.duplicated(subset='Ticket', keep=False)

# Faqat 'Name' ustunini chiqarish
# print(titanic_df.loc[answer_8, 'Name'])

# Ismida Miss bo'lgan va Pclassi 1 bo'lganlar chiqarildi
f1=titanic_df['Name'].str.contains('Miss')
f2=titanic_df['Pclass']==1
answer_10=f1 & f2
print(titanic_df.loc[answer_10,['Name','Pclass']])
