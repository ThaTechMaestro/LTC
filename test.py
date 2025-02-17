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

def fibonacci(nthNumber):
    a, b = 1, 1  # Line ❶
    print('a = %s, b = %s' % (a, b))
    
    for i in range(2, nthNumber):
        a, b = b, a + b  # Line ❷ - Get the next Fibonacci number
        print('a = %s, b = %s' % (a, b))
    
    return a

'''
take in a counter named 10
    decrease it in every method call
    
    Base:
        if n == 3:
            return 1,1
    a,b = fib(n-1)
    return b, a+b

I am slightly confused with the passing in of the values

    
'''
# print(fibonacci(10))

def fib(n):
    
    if n == 2:
        return 1,1
    
    a,b = fib(n-1)
    return b,a+b

a,b = fib(10)
print(b)
    




