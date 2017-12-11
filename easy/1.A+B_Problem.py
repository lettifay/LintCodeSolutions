# 1. A + B Problem
# more detail: https://stackoverflow.com/questions/30696484/a-b-without-arithmetic-operators-python-vs-c
def aplusb(self, a, b):
    import ctypes
    a = ctypes.c_int32(a).value
    b = ctypes.c_int32(b).value
    while b != 0:
        carry = ctypes.c_int32(a & b).value
        a = ctypes.c_int32(a ^ b).value
        b = ctypes.c_int32(carry << 1).value
    return a