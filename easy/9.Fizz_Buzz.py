# 9. Fizz Buzz
def fizzBuzz(n):
        result=[]
        for i in range(1,n+1):
            if i%3 == 0 and i%15 != 0:
                result.append("fizz")
            elif i%5 == 0 and i%15 != 0:
                result.append("buzz")
            elif i%15 == 0:
                result.append("fizz buzz")
            else:
                result.append(str(i))
        return result