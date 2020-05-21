def substrCount(n, s):
    res = n

    spcCnt = 0
    currCnt = 0
    prevCnt = 0
    prevPrevCnt = 0

    for i in range(1, n):
        prev = s[i - 1]
        curr = s[i]

        if prev == curr:
            currCnt += 1
            res += currCnt

            if spcCnt > 0:
                spcCnt -= 1
                res += 1
        else:
            currCnt = 0
            if i > 1 and s[i - 2] == curr:
                spcCnt = prevPrevCnt
                res += 1
            else:
                spcCnt = 0

        if i > 1:
            prevPrevCnt = prevCnt

        prevCnt = currCnt

    return res


substrCount()
