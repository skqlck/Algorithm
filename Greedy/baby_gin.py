numbers = input()
numbers = list(map(int,numbers))

counts = [0]*12

for number in numbers:
    counts[number] += 1

triplet = 0
run = 0
i = 0

while i < 10:
    if counts[i] >= 3:
        triplet += 1
        counts[i] -= 3
        continue

    elif counts[i] and counts[i+1] and counts[i+2]:
        counts[i] -= 1
        counts[i+1] -= 1
        counts[i+2] -= 1
        run += 1
        continue
    i += 1
print(f"triplet : {triplet}, run : {run}")