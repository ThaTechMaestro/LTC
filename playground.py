def fact(n, depth=0):
    indent = "  " * depth
    print(f"{indent}enter fact({n})")
    if n == 1:
        print(f"{indent}base case → 1")
        return 1
    res = n * fact(n-1, depth+1)
    print(f"{indent}return {res}")
    return res


fact(5)