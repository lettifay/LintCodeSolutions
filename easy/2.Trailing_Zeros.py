# 2. Trailing Zeros
# computes the number of trailing zeros in n factorial
def trailingZeros(self, n):
        tail = 0
        while n:
            n = n/5
            tail = tail + n
        return tail