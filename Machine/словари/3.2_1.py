roman_simv = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

letter = input().strip().upper()

print(roman_simv.get(letter, 0))
