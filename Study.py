groupmates = [
    {
        "name": "Марти",
        "surname": "Шароков",
        "exams": ["Вышмат", "web", "ИН"],
        "marks": [4, 2, 5]
    },
    {
        "name": "Алекс",
        "surname": "Львов",
        "exams": ["WEB", "История", "ИНО"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Глория",
        "surname": "Бегемотова",
        "exams": ["АиГ", "Рус", "ИКГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Мелман",
        "surname": "Жиравьёв",
        "exams": ["ЗИЗ", "web", "ИН"],
        "marks": [5, 3, 5]
    },
    {
        "name": "Тугарин",
        "surname": "Змейков",
        "exams": ["Философия", "История", "ИНО"],
        "marks": [5, 5, 5]
    },
]

def filter_students(studennts, middle):
    print(u"Имя".ljust(15), u"Фамилия".ljust(15), u"Экзамены".ljust(35), u"Оценки".ljust(15), u"Средний балл".ljust(15))
    for student in studennts:
        sum = 0
        for mark in student["marks"]:
            sum += mark
        average = sum/len(student["marks"])
        if(round(average, 2) > middle):
            print(student["name"].ljust(15), student["surname"].ljust(15), str(student["exams"]).ljust(35),
                  str(student["marks"]).ljust(20), str(round(average, 2)).ljust(15))
mid = float(input("Средний балл: "))
filter_students(groupmates, mid)
