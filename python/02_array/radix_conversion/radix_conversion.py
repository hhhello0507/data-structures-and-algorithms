# @x - 변환할 수
# @n - 진법
# d - 결과값
def convert(x, n):
    result = []
    nLst = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if x == 0:
        result.append(nLst[0])
    else:
        while x != 0:
            result.append(nLst[x % n])
            x //= n

    return ''.join([*reversed(result)])

print(convert(28, 16)) # 1C
