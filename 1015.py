x1, y1 = map(float, input().split(maxsplit=2))
x2, y2 = map(float, input().split(maxsplit=2))

print(f"{(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)):.4f}")