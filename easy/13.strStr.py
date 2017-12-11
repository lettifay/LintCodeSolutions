# 13. strStr
def strStr(source, target):
    if source == None or target == None:
        return -1
        
    for i in range(len(source) - len(target) + 1):
        if source[i:(i+len(target))] == target:
            return i
            
    return -1