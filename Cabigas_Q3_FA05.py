import numpy as np

names = ["Paula", "Yuna", "Paolo"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

daily_totals = []

for day in range(len(days)):
    total = 0
    for person in range(len(steps)):
        total += steps[person][day]
    daily_totals.append(total)

print("Total steps per day:")
for i in range(len(days)):
    print(days[i], ":", daily_totals[i])

most_active_day_index = daily_totals.index(max(daily_totals))

print("Most active day:", days[most_active_day_index], "with", daily_totals[most_active_day_index], "steps")
