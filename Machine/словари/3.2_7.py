N = int(input().strip())

votes = {}

for _ in range(N):
    vote = input().strip()
    votes[vote] = votes.get(vote, 0) + 1

# сортируем по кол-ву голосов, а после по алфавиту
sorted_countries = sorted(votes.items(), key=lambda x: (-x[1], x[0]))

for vote, count in sorted_countries:
    print(vote, count)
