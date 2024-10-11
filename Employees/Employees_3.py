import openpyxl
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



df = pd.read_csv(r"profeshion.csv")
print("OK")

def count_st(df):
    counts = df['Стать'].value_counts()
    print(counts)
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    x_data = [i for i in range(len(counts.values))]
    plt.bar(x_data, counts.values,color=colors)
    plt.xticks(x_data,counts.keys(),rotation=45)
    plt.ylabel("Кількість")
    plt.show()
# plt.bar(counts)
# plt.show()


def count_age(df):
    age_count = {
        'younger_18': 0,
        '18-45': 0,
        '45-70': 0,
        'older_70': 0
    }
    for index, row in df.iterrows():
        try:
            birth = datetime.strptime(row['Дата народження'].split()[0], '%Y-%m-%d')
        except ValueError:
            print(f"Помилка у форматі дати для рядка {index}: {row['Дата народження']}")
            continue
        age = datetime.now().year - birth.year - ((datetime.now().month, datetime.now().day) < (birth.month, birth.day))
        if age < 18:
            age_count['younger_18'] +=1
        elif 18 <= age <= 45:
            age_count['18-45'] +=1
        elif 45 < age <= 70:
            age_count['45-70'] +=1
        else:
            age_count['older_70'] +=1

    for category, count in age_count.items():
        print(f"{category}: {count}")

    plt.title('Кількість робітників за віковими категоріямі')
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    plt.bar(age_count.keys(), age_count.values(),color=colors)
    plt.xticks("Категорії")
    plt.ylabel("Кількість")
    plt.show()

def count_peopl(df):
    age_count = {
        'younger_18': {'Чоловік': 0, 'Жінка': 0},
        '18-45': {'Чоловік': 0, 'Жінка': 0},
        '45-70': {'Чоловік': 0, 'Жінка': 0},
        'older_70': {'Чоловік': 0, 'Жінка': 0}
    }

    # Підрахунок кількості людей за віковими категоріями та статтю
    for index, row in df.iterrows():
        try:
            birth = datetime.strptime(row['Дата народження'].split()[0], '%Y-%m-%d')
        except ValueError:
            print(f"Помилка у форматі дати для рядка {index}: {row['Дата народження']}")
            continue

        age = datetime.now().year - birth.year - ((datetime.now().month, datetime.now().day) < (birth.month, birth.day))
        gender = row['Стать']  # Чоловік або Жінка

        if age < 18:
            age_count['younger_18'][gender] += 1
        elif 18 <= age <= 45:
            age_count['18-45'][gender] += 1
        elif 45 < age <= 70:
            age_count['45-70'][gender] += 1
        else:
            age_count['older_70'][gender] += 1

    # Виведення результатів підрахунку
    for category, counts in age_count.items():
        print(f"{category}:")
        for gender, count in counts.items():
            print(f"  {gender}: {count}")

    categories = ['younger_18', '18-45', '45-70', 'older_70']
    men_counts = [age_count[cat]['Чоловік'] for cat in categories]
    women_counts = [age_count[cat]['Жінка'] for cat in categories]

    # Побудова графіка
    x = np.arange(len(categories))  # мітки на осі x
    width = 0.35  # ширина стовпців

    fig, ax = plt.subplots()

    rects1 = ax.bar(x - width/2, men_counts, width, label='Чоловіки', color='blue')
    rects2 = ax.bar(x + width/2, women_counts, width, label='Жінки', color='red')

    # Додавання підписів
    ax.set_ylabel('Кількість')
    ax.set_title('Кількість співробітників за віковими категоріями та статтю')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()

    # Додавання підписів над стовпцями
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    # Відображення графіка
    plt.show()

# Виклик функції з даними df
count_st(df)
count_age(df)
count_peopl(df)









# Виклик функції для зчитування файлу



#data['Диагноз'].value_counts()
#
# species = ("Adelie", "Chinstrap", "Gentoo")
# penguin_means = {
#     'Bill Depth': (18.35, 18.43, 14.98),
#     'Bill Length': (38.79, 48.83, 47.50),
#     'Flipper Length': (189.95, 195.82, 217.19),
# }
#
# x = np.arange(len(species))  # the label locations
# width = 0.25  # the width of the bars
# multiplier = 0
#
# fig, ax = plt.subplots(layout='constrained')
#
# for attribute, measurement in penguin_means.items():
#     offset = width * multiplier
#     rects = ax.bar(x + offset, measurement, width, label=attribute)
#     ax.bar_label(rects, padding=3)
#     multiplier += 1
#
# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Length (mm)')
# ax.set_title('Penguin attributes by species')
# ax.set_xticks(x + width, species)
# ax.legend(loc='upper left', ncols=3)
# ax.set_ylim(0, 250)
#
# plt.show()