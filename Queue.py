from collections import deque

game = deque(["Free Fire", "PUBG", "PES 2024"])

print(game)

game.popleft()
print(game)

game.popleft()
print(game)

game.popleft()
print(game)


if not game:
    print("No games are left.")

