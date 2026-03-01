# ExamTaskC3. На вход подаются сведения о клиентах фитнес-центра. В первой строке указывается целое число N,
# а каждая из последующих N строк имеет формат <Продолжительность занятий (в часах)> <Код клиента> <Год> <Номер месяца>
# Все данные целочисленные. Значение года лежит в диапазоне от 2000 до 2010, код клиента — в диапазоне 10–99,
# продолжительность занятий — в диапазоне 1–30. Найти строку исходных данных с минимальной продолжительностью занятий.
# Вывести эту продолжительность, а также соответствующие ей год и номер месяца (в указанном порядке).
# Если имеется несколько строк с минимальной продолжительностью, то вывести данные, соответствующие самой ранней дате.

class ClientActivity:
    def __init__(self, duration, client_id, year, month):
        self.duration = duration
        self.client_id = client_id
        self.year = year
        self.month = month

    def __lt__(self, other):
        if self.duration != other.duration:
            return self.duration < other.duration
        return (self.year, self.month) < (other.year, other.month)

    def __str__(self):
        return f"Продолжительность: {self.duration}\n Код клиента: {self.client_id}\n Год: {self.year}\n Месяц: {self.month}"


def find_min_activity(data):
    clients = [ClientActivity(*entry) for entry in data]
    min_activity = min(clients)
    return min_activity

data = [
    (3, 29, 2009, 7),
    (5, 20, 2005, 6),
    (3, 15, 2004, 12),
    (3, 10, 2003, 5),
    (1, 25, 2007, 3),
    (3, 30, 2005, 1)
]

result = find_min_activity(data)
print("\nМинимальная активность клиента:")
print(result)
