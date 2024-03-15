class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.w = weather

    def print_it(self):
        print(self.date, self.day, self.w)


n = int(input())
rainy_days = []

for _ in range(n):
    date, day, weather = input().split()
    if weather == 'Rain':
        rainy_days.append(Forecast(date, day, weather))


rainy_days = sorted(rainy_days, key = lambda x: x.date)
rainy_days[0].print_it()