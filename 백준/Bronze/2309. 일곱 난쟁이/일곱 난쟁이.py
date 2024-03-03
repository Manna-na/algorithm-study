import sys

input = sys.stdin.readline
# bingo_grid = [list(map(int, input().split())) for _ in range(5)]
dwarf_heights = [int(input()) for _ in range(9)]
total_height = sum(dwarf_heights)  # Total height of 9 dwarfs
found = False  # Flag to indicate if the correct dwarfs are found

# Try every combination of 2 dwarfs to remove
for i in range(9):
    if found:
        break
    for j in range(i + 1, 9):
        if total_height - (dwarf_heights[i] + dwarf_heights[j]) == 100:
            # Remove the two dwarfs not part of the original 7
            dwarf_heights.pop(j)
            dwarf_heights.pop(i)
            found = True
            break

# Sort the remaining dwarfs' heights
dwarf_heights.sort()
for aa in dwarf_heights:
    print(aa)