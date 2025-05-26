from collections import deque

deque = deque([(1,2,3), (4,5,6)])

a = deque.popleft()
b = deque.popleft()

print(a)
print(b)