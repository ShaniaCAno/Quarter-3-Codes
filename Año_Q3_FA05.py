# Names of participants
names = ["Aston", "Marvoun", "Jane"]

# 2D array of daily steps (rows = people, columns = days)
steps = [
    [4500, 5200, 4800, 5000, 5300],  # Aston
    [4000, 4100, 3900, 4200, 4600],  # Marvoun
    [6000, 5800, 5900, 6100, 6200]   # Jane
]

# Number of days (columns)
num_days = len(steps[0])

# Calculate total steps per day
day_totals = []
for day in range(num_days):
    total = sum(steps[person][day] for person in range(len(steps)))
    day_totals.append(total)
    print(f"Day {day+1} - Total Steps: {total}")

# Identify the most active day
max_total = max(day_totals)
max_day = day_totals.index(max_total) + 1
print(f"\nMost active day: Day {max_day} with {max_total} steps")
