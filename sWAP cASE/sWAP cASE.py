def swap_case(s):
    # because strings are immutable
    newStr = ""
    
    for c in s:
        if c.isupper():
            newStr += c.lower()
        elif c.islower():
            newStr += c.upper()
        else:
            newStr += c
    return newStr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
