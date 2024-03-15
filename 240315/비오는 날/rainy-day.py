class Forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.w = weather

    def print_it(self):
        print(self.date, self.day, self.w)

n = int(input())
ans = Forecast("9999-99-99", "", "")
for _ in range(n):
    date, day, weather = tuple(input().split())

    f = Forecast(date, day, weather)
    if weather == "Rain":
        if ans.date >= f.date:
            ans = f

ans.print_it()