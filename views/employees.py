# views/employees.py

class Employee:
    def __init__(self, name, position, phone, email, image_url, schedule):
        self.name = name
        self.position = position
        self.phone = phone
        self.email = email
        self.image_url = image_url
        self.schedule = schedule

# Приклади працівників
employees = [
    Employee("Зінчук Світлана Іванівна",
             "Директор, педіатр",
             "(097) 187-99-39",
             "olgopilspmsd@ukr.net",
             "IMG_85701.JPG",
             "Пн. - Пт. 8:00 - 15:42"),
    Employee("Пістуненко Вікторія Валеріївна",
             "Сімейний лікар",
             "(067) 011-78-66",
             "olgopilspmsd@ukr.net",
             "IMG_85531.JPG",
             "Пн. - Пт. 8:00 - 15:42"),
    Employee("Ковальчук Владислав Юрійович",
             "Сімейний лікар",
             "(098) 472-33-04",
             "olgopilspmsd@ukr.net",
             "IMG_85581.JPG",
             "Пн. - Пт. 8:00 - 15:42"),
]

class SubdivisionEmployee:
    def __init__(self, name, position, phone, location_name, location, image_url, schedule):
        self.name = name
        self.position = position
        self.phone = phone
        self.location_name = location_name
        self.location = location
        self.image_url = image_url
        self.schedule = schedule

# Приклади працівників підрозділів
subdivision_employees = [
    SubdivisionEmployee("Коваль Людмила Василівна",
                        "Медсестра",
                        "(068) 529-02-38",
                        "с. Демівка, вул. Героїв Майдану 27",
                        "https://maps.app.goo.gl/vBWmRnG5wRmSkWpo9",
                        "IMG_subdivision1.JPG",
                        "Пн. - Пт. 8:00 - 12:00"),
    SubdivisionEmployee("Тарасюк Зоя Степанівна",
                        "Медсестра", "(096) 625-08-75",
                        "с. Берізки-Чечельницькі, вул. Шевченка 24",
                        "https://maps.app.goo.gl/ys6g6k151W9AGnfM6",
                        "IMG_subdivision2.JPG",
                        "Пн. - Пт. 8:00 - 12:00"),
    SubdivisionEmployee("Бенера Віктор Васильович",
                        "Медбрат", "(099) 312-58-66",
                        "с. Любомирка, вул. Васі Курси 17",
                        "https://maps.app.goo.gl/fbPU9oLLnNQMsPSy8",
                        "IMG_subdivision3.JPG",
                        "Пн. - Пт. 8:00 - 12:00"),
    SubdivisionEmployee("Гонявчук Наталя Миколаївна",
                        "Медсестра",
                        "(098) 808-16-87",
                        "с. Стратіївка, вул. Мазурівка 10",
                        "https://maps.app.goo.gl/NXboo2bCLjodZ4fZ9",
                        "IMG_subdivision4.JPG",
                        "Пн. - Пт. 8:00 - 12:00"),
]
