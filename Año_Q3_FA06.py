names = ["Aston", "Marvoun", "Jane"]

# 2D array of daily steps (rows = people, columns = days)
steps = [
    [4500, 5200, 4800, 5000, 5300],  # Aston
    [4000, 4100, 3900, 4200, 4600],  # Marvoun
    [6000, 5800, 5900, 6100, 6200]   # Jane
]

totals = []
for i, row in enumerate(steps):
    total = sum(row)
    totals.append(total)
    print(f"{names[i]} - Total Steps: {total}")

max_total = max(totals)
min_total = min(totals)
max_index = totals.index(max_total)
min_index = totals.index(min_total)

print(f"\nPerson with highest steps: {names[max_index]} ({max_total})")
print(f"Person with lowest steps: {names[min_index]} ({min_total})")

difference = max_total - min_total
print(f"Difference between highest and lowest: {difference}")
