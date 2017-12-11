# 30. Insert Interval
def insert(self, intervals, newInterval):
    if intervals == None or intervals == []:
        return [newInterval]

    results = []
    insert_p = 0 
    for i in intervals:
        if i.end < newInterval.start:
            results.append(i)
            insert_p += 1
        elif newInterval.end < i.start:
            results.append(i)
        else:
            newInterval.start = min(i.start,newInterval.start)
            newInterval.end = max(i.end,newInterval.end)
    results.insert(insert_p,newInterval)        
    return results