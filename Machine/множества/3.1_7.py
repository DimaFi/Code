def read_points(num_points):
    points = set()
    for _ in range(num_points):
        x, y = map(int, input().split())
        points.add((x, y))
    return points

n, m = map(int, input().split())

sets = [read_points(m) for _ in range(n)]

best_point = None
max_count = 0

for point in sets[0]:
    count = sum(1 for s in sets[1:] if point in s)
    
    if count > max_count:
        best_point = point
        max_count = count


if best_point is None:
    print(-1) 
else:
    print(f"{best_point[0]} {best_point[1]}")
