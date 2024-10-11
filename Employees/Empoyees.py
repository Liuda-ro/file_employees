from faker import Faker
import csv
import random
from datetime import datetime, timedelta

fake = Faker(locale = 'uk_UA')


#по батькові
n_m3 = ["Вікторович","Михайлович","Олександрович", "Анатолійович", "Дмитрович","Вадимович","Юрійович","Петрович","Максимович","Олегович","Ільїч","Артемович","Сергійович","Назарович","Володимирович","Георгійович","Григорович","Данилович", "Іванович","Костянтинович"]
n_f3 = ["Вікторівна","Михайлівна","Олександрівна", "Анатоліївна", "Дмитрівна","Вадимівна","Юріївна","Петрівна","Максимівна","Олегівна","Ільївна","Артемівна","Сергіївна","Назарівна","Володимирівна","Георгіївна","Григорівна","Даниліївна", "Іванівна","Костянтинівна"]


#випадкова дата народження, модулы faker для дати не працюють
def generate_random_date():
    start_date = datetime(1938, 1, 1)
    end_date = datetime(2008, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date


data = ["Прізвище", "Ім'я", "Побатькові", "Стать", "Дата народження", "Посада", "Місто проживання", "Адреса", "Телефон", "Email"]

#стать
osntext =[]
for _ in range(2000):
    gender = random.choices(["M", "F"], weights=[60, 40])[0]

    if gender == "M":
        sname = fake.first_name_male()
        lastn = fake.last_name_male()
        po_b = random.choice(n_m3)
        stat = "Чоловік"
    else:
        sname = fake.first_name_female()
        lastn = fake.last_name_female()
        po_b = random.choice(n_f3)
        stat = "Жінка"

    p1 = fake.job()
    c1 = fake.city()
    a1 = fake.address()
    t1 = fake.phone_number()
    e1 = fake.email()
    ran_d = generate_random_date()

    osntext.append([lastn,sname,po_b,stat,ran_d,p1,c1,a1,t1,e1])


def File_CSV(filename):
   try:
       with open(filename, "w", newline='', encoding='utf-8') as file:
           print("Файл створений;)")
           writer = csv.writer(file)
           writer.writerow(data)
           writer.writerows(osntext)
   except Exception as e:
       print(f"Помилка при створенні файлу: {e}")

File_CSV("profeshion.csv")










# def read_csv(filename):
#     try:
#         with open(filename, "r", encoding='utf-8') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 print(row)
#     except Exception as e:
#         print(f"Помилка при відкритті файлу: {e}")
#
# # Виклик функції для зчитування файлу
# read_csv("profeshion.csv")








