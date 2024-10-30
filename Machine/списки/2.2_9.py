def classify_vowels_consonants(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'}
    
    result = []
    for i, char in enumerate(s):
        if char in vowels:
            result.append('V')
        elif char in consonants:
            result.append('C')
        elif char == 'y':
            # Проверка правила для 'y'
            if i == 0 or s[i - 1] in consonants:
                result.append('V')
            else:
                result.append('C')
        else:
            result.append('C')
    
    return ''.join(result)

s = input().strip()
print(classify_vowels_consonants(s))
