def read_points(num_points):
    points = set()
    for _ in range(num_points):
        x, y = map(int, input().split())
        points.add((x, y))
    return points

n, m = map(int, input().split())

first_set = [tuple(map(int, input().split())) for _ in range(m)]


sets = [read_points(m) for _ in range(n-1)]

best_point = None
max_count = 0

for point in first_set:
    count = sum(1 for s in sets if point in s)
    
    if count > max_count:
        best_point = point
        max_count = count


if best_point is None:
    print(-1) 
else:
    print(f"{best_point[0]} {best_point[1]}")
