def sort_cards(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        input_data = file.read().splitlines()
    
    n = int(input_data[0])
    cards = input_data[1:-1]  # Список карт
    order = input_data[-1]  # Заданный порядок мастей

    # словарь для карт по мастям
    suits = {suit: [] for suit in 'pcbk'}

    # добавляем карты в словарь
    for card in cards:
        rank, suit = card.split()
        suits[suit].append(int(rank))

    # сортируем карты внутри масти
    for suit in suits:
        suits[suit].sort()

    result = []
    for suit in order:
        sorted_ranks = ' '.join(map(str, suits[suit]))
        result.append(f"{suit}: {sorted_ranks}")

    with open(output_filename, 'w') as file:
        file.write('\n'.join(result))


input_filename = "input.txt"
output_filename = "output.txt"

sort_cards(input_filename, output_filename)