a, b, c = map(int, input().split(maxsplit=3))

m = ((a + b) + abs(a-b)) / 2

# if m > c:
#     print(f"{m:.0f} eh o maior")
# else:
#     print(f"{c:.0f} eh o maior")

print(f"{(((m + c) + abs(m - c)) / 2):.0f} eh o maior")
