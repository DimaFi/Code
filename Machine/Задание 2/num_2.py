import random
import string

def generate_id():
    """Генерирует случайное пятизначное число с хотя бы одной четной цифрой."""
    while True:
        id = ''.join(random.choices(string.digits, k=5)) #5 цифр    
        if any(int(digit) % 2 == 0 for digit in id):
            return id

def generate_login():
    """Генерирует случайную последовательность из 6 букв, содержащую ровно три согласные."""
    vowels = 'aeiou'  # Гласные
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))  # Согласные
    
    chosen_vowels = random.sample(vowels, 3)
    chosen_consonants = random.sample(consonants, 3)
    
    login = chosen_vowels + chosen_consonants
    random.shuffle(login) #перемешать
    return ''.join(login)


def generate_password():        
    """
    Генерирует пароль из 10 символов, содержащий хотя бы одну большую букву, одну цифру,
    и заканчивающийся строчной буквой.
    """
    while True:
        letters = random.sample(string.ascii_letters + string.digits, 9)
        ending = random.choice(string.ascii_lowercase)
        password = ''.join(letters) + ending
        if (any(char.isupper() for char in password) and 
            any(char.isdigit() for char in password)):
            return password

def generate_unique_entries(n):
    """
    Генерирует список из N троек (id, логин, пароль), где id, логины и пароли уникальны.
    """
    unique_ids = set()
    unique_logins = set()
    unique_passwords = set()
    
    entries = []
    while len(entries) < n:
        id = generate_id()
        login = generate_login()
        password = generate_password()
        
        if id not in unique_ids and login not in unique_logins and password not in unique_passwords:
            entries.append((id, login, password))
            unique_ids.add(id)
            unique_logins.add(login)
            unique_passwords.add(password)
    
    return entries

n = 5
entries = generate_unique_entries(n)
for entry in entries:
    print(entry)
