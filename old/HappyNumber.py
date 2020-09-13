import functools

def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    return helper(n, set())

def helper(n, s):
    if n == 1:
        return True
    lis = list(str(n))
    newN = functools.reduce(lambda a, b: int(a) + int(b) * int(b), lis, 0)
    if newN == 1:
        return True
    if newN in s:
        return False
    s.add(newN)
    print(s)
    return helper(newN, s)
    


print(isHappy(19))


# ll = []
# bb = functools.reduce(lambda a, b: a + b*b, ll, 0)
# print(bb)