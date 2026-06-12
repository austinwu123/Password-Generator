count = int(input("How many times do you want to add? "))
step = float(input("What do you want to count by? "))

total = 0

for i in range(count):
    total = total + step
    print(f"Round {i + 1}: {total}")
