def solution(n):
    answer = ''
    tmp = ''
    nums124 = [4, 1, 2]
    while n > 0:
        tmp += str(nums124[n % 3])
        if n % 3 == 0:
            n -= 1
        n //= 3
    answer = tmp[::-1]
    # tmp = tmp[::-1]
    # return tmp

    return answer
