agents = [tuple(input().split()) for _ in range(5)]

class Agent:
    def __init__(self, name, score):
        self.name = name
        self.score = int(score)

min_score = 101
min_name = ""

for name, score in agents:
    result = Agent(name, score)
    
    if result.score < min_score:
        min_name = result.name
        min_score = result.score

print(min_name, min_score)