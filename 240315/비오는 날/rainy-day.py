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


min_idx = 0
for i in range(1, len(rainy_days)):
    if rainy_days[min_idx].date > rainy_days[i].date:
        min_idx = i

rainy_days[min_idx].print_it()