import json

people = [
    {"Height": 175, "Gender": "Male"},
    {"Height": 168, "Gender": "Female"},
    {"Height": 180, "Gender": "Male"},
    {"Height": 160, "Gender": "Female"},
    {"Height": 185, "Gender": "Male"},
    {"Height": 170, "Gender": "Female"},
    {"Height": 176, "Gender": "Male"},
    {"Height": 165, "Gender": "Female"},
    {"Height": 179, "Gender": "Male"},
    {"Height": 155, "Gender": "Female"}
]

jsonData = json.dumps(people, indent=4) 
with open('data.json', 'wt') as file:
    file.write(jsonData)

while True:
    print("\n1 - Додати дані")
    print("2 - Переглянути дані")
    print("3 - Обчислити середній зріст чоловіків")
    print("4 - Пошук за полем")
    print("5 - Вихід")
    
    choice = input("Виберіть опцію: ")
    
    if choice == "1":
        height = input("Введіть зріст (в см): ")
        gender = input("Введіть стать (Male/Female): ")
        
        people.append({"Height": int(height), "Gender": gender})
        
        jsonData = json.dumps(people, indent=4)
        with open('data.json', 'wt') as file:
            file.write(jsonData)
    
    if choice == "2":
        with open("data.json", "r") as file:
            data = json.load(file)
            print("Данні з файлу:")
            for person in data:
                print(f"Зріст: {person['Height']} см, Стать: {person['Gender']}")
    
    if choice == "3":
        male_heights = [person['Height'] for person in people if person['Gender'] == 'Male']
        if male_heights:
            avg_height = sum(male_heights) / len(male_heights)
            print(f"Середній зріст чоловіків: {avg_height:.2f} см")
        else:
            print("Дані для чоловіків відсутні.")
    
    if choice == "4":
        field = input("Введіть поле для пошуку (Height/Gender): ").capitalize()
        value = input(f"Введіть значення для {field}: ").capitalize()
        
        result = [person for person in people if person[field] == value]
        if result:
            for person in result:
                print(f"Знайдено: Зріст: {person['Height']} см, Стать: {person['Gender']}")
        else:
            print(f"Не знайдено даних для {field} = {value}.")
    
    if choice == "5":
        print("Вихід з програми...")
        quit() 