from collections import Counter

# def printer():
#     a = "dog"
#     print("Hello world I am ", a)

# a = (1,1,2,3)
# print(set(a))

a = 4
print(a//2)

# for i in range(1,5+1):
#     print(i)

# for i in range(len(a)):
#     print("I am empty")

# print(len(a))
# python3 -m pytest -v tests/playground.py

# a = 0

# if a:
#     print("valid")
# else:
#     print("Invalid")

x = "aseinerks"
a = "addddaaaaae"

x_count = Counter(x)
print(x_count)
print(x_count.items)

for x,y in x_count.items():
    print(x,y)