from collections import deque

a = deque([1,2, 3])

a.popleft()
a.appendleft(100)

a.append(100)
a.pop()

b = [1, 2, 3]
print(b[2])