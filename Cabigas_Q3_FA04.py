import numpy as np

names = ["Paula", "Yuna", "Paolo"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
])

totals = [sum(person) for person in steps]

highest_total = max(totals)
lowest_total = min(totals)

highest_index = totals.index(highest_total)

print("Total steps per person:")
for i in range(len(names)):
    print(names[i], ":", totals[i])
    

print("Highest total steps:", names[highest_index], "with", highest_total)
print("Difference between highest and lowest total:", highest_total - lowest_total)
