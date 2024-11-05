def read_points(num_points):
    points = set()
    for _ in range(num_points):
        x, y = map(int, input().split())
        points.add((x, y))
    return points

n, m = map(int, input().split())

set_a = read_points(n)
set_b = read_points(m)

crossing = sorted(set_a & set_b)
diff = sorted(set_a - set_b)

def format_output(points):
    return ' '.join(f'({x}, {y})' for x, y in points) if points else 'empty'

print(format_output(crossing))
print(format_output(diff))
