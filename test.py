from collections import Counter

# def printer():
#     a = "dog"
#     print("Hello world I am ", a)

# x_count = Counter(x)
# print(x_count)
# print(x_count.items)

# for x,y in x_count.items():
#     print(x,y)

# a = [1,2,3,4,4]
# print(max(a))

# index = 0
# k = 2

# final = max(a[index:index+k])
# print(final)


# from collections import deque

# Create a deque
# deque_obj = deque()

# # Add elements
# deque_obj.append(1)  # Add to back
# deque_obj.appendleft(2)  # Add to front
# deque_obj.append(3)

# Remove elements

# Print the remaining items in the deque
# print(list(deque_obj))  


n = 3

result = 1

for i in range(1,n+1):
    result*=i

print(result)

def rec(n):

    if n == 1:
        return 1
    return n * rec(n-1)
    




