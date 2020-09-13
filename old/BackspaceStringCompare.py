def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    if not S and not T:
        return True
    if not S:
        return not lastChar(T)
    if not T:
        return not lastChar(S)

    s = len(S) - 1
    t = len(T) - 1
    s_back_num = 0
    t_back_num = 0
    s_last = ""
    t_last = ""
    while s >= 0 or t >= 0: 
        while s >= 0:
            if S[s] == "#":
                s_back_num += 1
                s -= 1
            elif s_back_num > 0:
                s_back_num -= 1
                s -= 1
            else:
                s_last = S[s]
                print("s last:")
                print(s_last)
                break

        while t >= 0:
            if T[t] == "#":
                t_back_num += 1
                t -= 1
            elif t_back_num > 0:
                t_back_num -= 1
                t -= 1
            else:
                t_last = T[t]
                print("t last:")
                print(t_last)
                break
        if s_last != t_last:
            return False
        print("~~")
        print(s)
        print(t)
        if s != t and (s<0 or t < 0):
            return False
        else:
            s -= 1
            t -= 1
  
    return s_last == t_last

def lastChar(string):
    s = len(string) - 1
    s_back_num = 0
    while s >= 0:
        if string[s] == "#":
            s_back_num += 1
            s -= 1
        elif s_back_num > 0:
            s_back_num -= 1
            s -= 1
        else:
            return string[s]
    return ""


# a = backspaceCompare("ab#c", "ad#c")
# b = backspaceCompare("ab#c", "ad#d")


SSS = "bbbextm"
TTT = "bbb#extm"



c = backspaceCompare(SSS, TTT)
# print(a)
# print(b)
print(c)
