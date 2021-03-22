import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    test_case = input()
    # 세로를 검사하기 위해 a의 col과 row를 반전시킨 reverse_a
    a = [input() for _ in range(100)]
    reverse_a = list(map(list, zip(*a)))

    ans = 1

    def is_palindrome(s):
        if s == s[::-1]:
            return True
        return False


    for i in range(100):
        # 가로
        for start in range(100):
            # k는 문자열의 길이, 한 글자는 검사할 필요가 없다. 그래서 2 글자부터 시작.
            for k in range(2, 100-start+1):
                if is_palindrome(a[i][start:start+k]):
                    if ans < k:
                        ans = k
        # 세로
        for start in range(100):
            # k는 문자열의 길이
            for k in range(2, 100-start+1):
                if is_palindrome(''.join(reverse_a[i][start:start+k])):
                    if ans < k:
                        ans = k

    print('#{} {}'.format(tc, ans))

    # zip() 사용 예제
    # b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4,]]
    # c = list(map(list, zip(*b)))
    # print(c)
    #
    # b = ['aaaa', 'bbbb', 'cccc', 'dddd']
    # c = list(map(list, zip(*b)))
    # print(c)
