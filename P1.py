from collections import deque

bank = deque([])
bank.append("Shifat")
bank.append("Abrar")
bank.append('Walid')

print(bank)

bank.popleft()
print(bank)