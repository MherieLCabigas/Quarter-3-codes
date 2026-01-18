import numpy as np

names = ["Paula", "Yuna", "Paolo"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [4500, 5200, 4800, 5000, 5300],  
    [4000, 4100, 3900, 4200, 4600],  
    [6000, 5800, 5900, 6100, 6200]  
])

print("Daily steps (Monday to Friday):")

for i in range(len(names)):
    print(names[i], ":", steps[i])
