def swap_case(s):
    new=""
    for i in range(len(s)):
        if s[i]==s[i].lower():
            upper = s[i].upper()
            new+=upper

        elif s[i]==s[i].upper():
            lower = s[i].lower()
            new+=lower
    return new

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)