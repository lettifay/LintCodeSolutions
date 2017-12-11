# 22. Flatten List
def flatten(nestedList):
    if nestedList == None:
        return []
        
    if type(nestedList) == int:
        return [nestedList]
    
    result=[]
    for i in range(len(nestedList)):
        result.extend(flatten(nestedList[i]))
    return result