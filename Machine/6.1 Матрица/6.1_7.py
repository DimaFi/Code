# Шахматная доска

n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]


def count_changes_to_chessboard(start_with_dot):
    changes = 0
    for i in range(n):
        for j in range(m):
            expected = '.' if (i + j) % 2 == 0 else '*'  # Определяем ожидаемый символ
            if start_with_dot:
                expected = '.' if (i + j) % 2 == 0 else '*'  # начало с точки
            else:
                expected = '*' if (i + j) % 2 == 0 else '.'  # начало с звездочки
            if field[i][j] != expected:
                changes += 1
    return changes

# считаем кол-во замен для обоих вариантов
changes_for_start_dot = count_changes_to_chessboard(True)
changes_for_start_star = count_changes_to_chessboard(False)

print(min(changes_for_start_dot, changes_for_start_star))
