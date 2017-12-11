# 8. Rotate String
def rotateString(str, offset):
    if len(str) == 0:
        return str
    n = offset % len(str)
    tmp = str[-n:]+str[:-n]
    for i in range(len(str)):
        str[i] = tmp[i]
    return str