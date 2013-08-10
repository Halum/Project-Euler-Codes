def count( num ):
    ans = 0
    length = len(num)
    try:
        for i in range(0, length):
            ans += int(num[i])
        return  ans
    except TypeError as err:
        print('the error is: ' + str(err))


print(count(str(2**100)))
