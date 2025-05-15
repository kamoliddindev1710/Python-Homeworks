#task 1
import json
with open('student.json') as f:
   text=json.load(f)

print(text)

#task 2
import requests
import json
API_key ='b66059b18d9ead8010980220c3533c4d'
lat = 41
lon = 69
url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
response=requests.get(url)

d1=response.json()


with open('from_url_to_js.json','w') as f:
     json.dump(d1,f,indent=4)

with open('from_url_to_js.json') as f2:
 text=json.load(f2)

print(text['main'])


#task 3
import json

filename = 'books.json'


try:
    with open(filename, 'r') as f:
        book_list = json.load(f)
except:
    book_list = {}

def add_book():
    name = input("Kitob nomi: ")
    if name in book_list:
        print("Bu kitob allaqachon mavjud.")
    else:
        price = input("Narxi: ")
        if price.isdigit():
            book_list[name] = int(price)
            print("Kitob qo‘shildi.")
        else:
            print("Narx noto‘g‘ri.")

def update_book():
    name = input("Kitob nomi: ")
    if name in book_list:
        price = input("Yangi narx: ")
        if price.isdigit():
            book_list[name] = int(price)
            print("Kitob yangilandi.")
        else:
            print("Narx noto‘g‘ri.")
    else:
        print("Bu kitob topilmadi.")

def remove_book():
    name = input("Kitob nomi: ")
    if name in book_list:
        del book_list[name]
        print("Kitob o‘chirildi.")
    else:
        print("Bu kitob mavjud emas.")

def show_books():
    if book_list:
        print("Kitoblar ro‘yxati:")
        for name, price in book_list.items():
            print(f"- {name}: {price} so'm")
    else:
        print("Kitoblar ro‘yxati bo‘sh.")

# Asosiy menyu
while True:
    print("\n1. Kitob qo‘shish")
    print("2. Kitob yangilash")
    print("3. Kitob o‘chirish")
    print("4. Barcha kitoblarni ko‘rish")
    print("5. Chiqish")

    choice = input("Tanlang (1-5): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        remove_book()
    elif choice == '4':
        show_books()
    elif choice == '5':
        # 3. Dasturdan chiqishda faylga yozish
        with open(filename, 'w') as f:
            json.dump(book_list, f, indent=4)
        print("Ma'lumotlar saqlandi. Chiqildi.")
        break
    else:
        print("Noto‘g‘ri tanlov.")


#task 4
import requests
import json

yourkey = '544cd3fd'
url1 = 'http://www.omdbapi.com/?i=tt3896198&apikey=544cd3fd'

response = requests.get(url1)
d1 = response.json()

with open('movie.json', 'w') as f:
    json.dump(d1, f, indent=4)

with open('movie.json') as f2:
    text = json.load(f2)


# Film janrlarini listga ajratamiz
lst = text["Genre"].split(', ')
print("Film janrlari:", lst)

user_genre = input("Qaysi janrni tanlaysiz? ").strip()

if user_genre in lst:
    print(f"Tavsiya qilinadigan film: {text['Title']} (Janr: {text['Genre']})")
else:
    print(f"Uzr, tanlagan janringiz ({user_genre}) bu filmda yo'q.")
